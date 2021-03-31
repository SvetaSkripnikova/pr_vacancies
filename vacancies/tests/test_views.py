from django.test import TestCase, Client
from django.urls import reverse, resolve

from vacancies.models import Specialty, Company, Vacancy


class TestViews(TestCase):

    # настройка объектов
    def setUp(self):
        self.client = Client()
        self.main_url = reverse('main')
        self.vacancies_url = reverse('vacancies')

    # тест проверяет корректность открытия страницы (код 200) и соответствие представлению главной страницы
    def test_main_GET(self):
        response = self.client.get(self.main_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')

    # тест проверяет корректность открытия страницы (код 200) и соответствие представлению страницы списка вакансий
    def test_vacancies_GET(self):
        response = self.client.get(self.vacancies_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'vacancies/vacancy_list.html')
