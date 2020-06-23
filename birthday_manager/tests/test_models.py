from django.test import TestCase
from django.utils.datetime_safe import datetime

from birthday_manager.models import Person


class TestPersonCreate(TestCase):
    def test_setup(self):
        return Person.objects.create(name='Test Person', birthday=datetime(2020, 6, 22))

    def test_name(self):
        person = self.test_setup()
        self.assertEqual(person.name, 'Test Person')

    def test_birthday(self):
        person = self.test_setup()
        self.assertEqual(person.birthday, datetime(2020, 6, 22))

    def test_str(self):
        person = self.test_setup()
        self.assertEqual(str(person), "Test Person: 6/22")
