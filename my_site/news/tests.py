from django.test import TestCase, Client
from news import models
from django.utils.timezone import now


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = models.Category.objects.create(
            title='Категория 11'
        )
        self.news = models.News.objects.create(
            title='Новость 22',
            content='Очень важная срочная новость!',
            created_at=now(),
            uploaded_at=now(),
            category=self.category
        )

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_detail(self):
        response = self.client.get(f'/news/{self.news.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_category(self):
        response = self.client.get(f'/category/{self.category.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_list(self):
        response = self.client.get('/news/')
        self.assertEqual(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEqual(response.status_code, 302)

    def test_form(self):
        response = self.client.get('/form_example/')
        self.assertEqual(response.status_code, 200)
