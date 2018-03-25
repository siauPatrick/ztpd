import requests
from bs4 import BeautifulSoup

from apps.citizens.models import Species, Citizen


def fill_db():
    species_url = 'http://zootopia.wikia.com/wiki/List_of_Species_Seen_in_Zootopia'
    species_soup = BeautifulSoup(requests.get(species_url).text)
    no_citizen_urls = {
        '/wiki/Koslov%27s_Palace',
        '/wiki/Skunk_Appreciation_Parade',
        '/wiki/Hopps_family',
    }

    citizens = []

    for citizen_link in species_soup.select('#mw-content-text li a[href^="/wiki/"]'):
        if citizen_link.get('class') or '.' in citizen_link['href'] or citizen_link['href'] in no_citizen_urls:
            continue
        else:
            citizen_soup = BeautifulSoup(requests.get(f'http://zootopia.wikia.com{citizen_link["href"]}').text)
            print(citizen_link["href"])
            try:
                species_name = citizen_soup.find(text='Species').next_element.next_element.text.lower()
                species, created = Species.objects.get_or_create(name=species_name)
                citizen = Citizen(
                    name=citizen_soup.select_one('.pi-title').text,
                    photo_url=citizen_soup.select_one('.pi-image a').get('href'),
                    species=species,
                    gender=citizen_soup.find(text='Gender').next_element.next_element.text.lower(),
                )
                citizens.append(citizen)
            except AttributeError:
                continue

    Citizen.objects.bulk_create(citizens)
