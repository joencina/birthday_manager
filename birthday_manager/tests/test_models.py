from django.test import TestCase
from django.utils.datetime_safe import datetime

from birthday_manager.models import Person


class TestPersonCreate(TestCase):
    # Test if you can create an object and it works
    def setUp(self) -> None:
        self.person = Person.objects.create(name='Test Person', birthday=datetime(2020, 6, 22))

    def test_name(self):
        self.assertEqual(self.person.name, 'Test Person')

    def test_birthday(self):
        self.assertEqual(self.person.birthday, datetime(2020, 6, 22))

    def test_str(self):
        self.assertEqual(str(self.person), "Test Person: 6/22")

# TODO: Multiple assertions per test is fine