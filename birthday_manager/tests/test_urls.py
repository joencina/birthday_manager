from django.test import TestCase
from django.urls import reverse


class IndexTest(TestCase):
    def test_index_status_code(self):
        response = self.client.get('/', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, 'birthday')


class ContactsTest(TestCase):
    def test_contacts_status_code(self):
        response = self.client.get('/contacts', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('contacts'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contacts'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')


class AddTest(TestCase):
    def test_add_status_code(self):
        response = self.client.get('/add', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('add'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'add.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/add', follow=True)
        self.assertContains(response, 'Add contact')


class SearchTest(TestCase):
    def test_add_status_code(self):
        response = self.client.get('/search', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/search', follow=True)
        self.assertContains(response, 'Search contact')