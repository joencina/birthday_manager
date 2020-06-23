from datetime import datetime

from django.test import TestCase
from django.urls import reverse_lazy, reverse
from django.utils.timezone import tzinfo
from pytest import mark
from pytz import timezone

from birthday_manager.models import Person
from birthday_manager.views import PersonCreate, SearchView


class IndexTest(TestCase):
    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)


class TestPersonCreate(TestCase):
    @mark.django_db()
    def test_setup(self):
        return self.client.post('/add/', data={'name': 'Test Name', 'birthday': '06/22/2020'})

    def test_person_create(self):
        response = self.test_setup()
        self.assertEqual(Person.objects.last().name, 'Test Name')

    def test_person_birthday(self):
        self.test_setup()
        object_date = datetime.strftime(Person.objects.last().birthday, "%m/%d/%Y")
        posted_date = datetime.strftime(timezone('UTC').localize(datetime(2020, 6, 22)), "%m/%d/%Y")
        self.assertEqual(object_date, posted_date)


class TestSearch(TestCase):
    @mark.django_db()
    def test_setup(self):
        return self.client.post('/add/', data={'name': 'Test Name', 'birthday': '06/22/2020'})

    def test_person_search(self):
        self.test_setup()
        response = self.client.get('/found/', data={'name': 'Test Name'})
        self.assertContains(response, 'Test Name')
