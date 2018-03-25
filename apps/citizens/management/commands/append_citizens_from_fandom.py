from typing import Set

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.management.base import BaseCommand
from tqdm import tqdm

from apps.citizens.models import Citizen, Species


class Command(BaseCommand):
    help = 'Parse citizens from fandom and append to out db'
    fandom_base_url = 'http://zootopia.wikia.com'
    no_citizen_links = {
        '/wiki/Koslov%27s_Palace',
        '/wiki/Skunk_Appreciation_Parade',
        '/wiki/Hopps_family',
    }

    def handle(self, *args, **options) -> None:
        citizens = []

        for citizen_link in tqdm(self._collect_citizen_links(), disable=not settings.DEBUG):
            citizen = self._load_citizen(citizen_link)

            if citizen:
                citizens.append(citizen)

        Citizen.objects.bulk_create(citizens)

    def _collect_citizen_links(self) -> Set[str]:
        citizens_html = requests.get(f'{self.fandom_base_url}/wiki/List_of_Species_Seen_in_Zootopia').text
        citizens_soup = BeautifulSoup(citizens_html, 'html.parser')
        citizen_a_tags = citizens_soup.select('#mw-content-text li a[href^="/wiki/"]')
        citizen_links = {
            f'{self.fandom_base_url}{a_tag["href"]}'
            for a_tag in citizen_a_tags
            if not (a_tag.get('class') or '.' in a_tag['href'] or a_tag['href'] in self.no_citizen_links)
        }
        exist_citizen_links = Citizen.objects.filter(fandom_url__in=citizen_links).values_list('fandom_url', flat=True)

        return citizen_links - set(exist_citizen_links)

    def _load_citizen(self, citizen_link: str) -> Citizen:
        citizen_html = requests.get(citizen_link).text
        citizen_soup = BeautifulSoup(citizen_html, 'html.parser')
        species_el = citizen_soup.find(text='Species')
        gender_el = citizen_soup.find(text='Gender')

        if all([species_el, gender_el]):
            species_name = species_el.next_element.next_element.text.lower()
            species, created = Species.objects.get_or_create(name=species_name)

            return Citizen(
                name=citizen_soup.select_one('.pi-title').text,
                photo_url=citizen_soup.select_one('.pi-image a').get('href'),
                species=species,
                gender=gender_el.next_element.next_element.text.lower(),
                fandom_url=citizen_link
            )
