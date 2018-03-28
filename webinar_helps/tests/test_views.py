from django.urls import reverse
from rest_framework.test import APIRequestFactory, APITestCase

from webinar_helps.tests.factories import CitizenFactory
from citizens.views import CitizenListAPIView


class TestCitizenListAPIView(APITestCase):
    def setUp(self):
        CitizenFactory.create_batch(10)
        self.factory = APIRequestFactory()

    def test_citizen_list_slow(self):
        for _ in range(800):
            resp = self.client.get(reverse('citizens'))
            self.assertEqual(len(resp.data['results']), 10)

    def test_citizen_list_fast(self):
        view = CitizenListAPIView().as_view()

        for page in range(800):
            request = self.factory.get(reverse('citizens'))
            resp = view(request)
            self.assertEqual(len(resp.data['results']), 10)
