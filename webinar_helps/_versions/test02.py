from django.db import connection
from django.urls import reverse
from rest_framework.test import APITestCase

from citizens.models import Citizen
from webinar_helps.tests.factories import CitizenFactory


class TestCitizenListAPIView(APITestCase):
    def setUp(self):
        self.citizen_judy = CitizenFactory(
            name='Judy Hopps',
            species__name='rabbit',
            gender=Citizen.GENDER.female,
            photo_url='https://vignette.wikia.nocookie.net/zootopia/images/4/45/Judy_Standing_Render.png',
            fandom_url='http://zootopia.wikia.com/wiki/Judy_Hopps'
        )
        self.citizen_nick = CitizenFactory(
            name='Nick Wilde',
            species__name='fox',
            gender=Citizen.GENDER.male,
            photo_url='https://vignette.wikia.nocookie.net/zootopia/images/3/3e/Nick_Sly_Fox_Render.png',
            fandom_url='http://zootopia.wikia.com/wiki/Nick_Wilde'
        )

        self.exp_citizens = [
            {
                'name': 'Judy Hopps',
                'species': 'Rabbit',
                'gender': 'female',
                'photo_url': 'https://vignette.wikia.nocookie.net/zootopia/images/4/45/Judy_Standing_Render.png',
                'fandom_url': 'http://zootopia.wikia.com/wiki/Judy_Hopps'
            },
            {
                'name': 'Nick Wilde',
                'species': 'Fox',
                'gender': 'male',
                'photo_url': 'https://vignette.wikia.nocookie.net/zootopia/images/3/3e/Nick_Sly_Fox_Render.png',
                'fandom_url': 'http://zootopia.wikia.com/wiki/Nick_Wilde'
            }
        ]

    def test_citizen_list(self):
        resp = self.client.get(reverse('citizens'))
        self.assertListEqual(self.exp_citizens, resp.data['results'])

    def test_missing_species(self):
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM citizens_species WHERE id = %s', [self.citizen_nick.species_id])

        self.exp_citizens[1]['species'] = None

        resp = self.client.get(reverse('citizens'))
        self.assertListEqual(self.exp_citizens, resp.data['results'])
