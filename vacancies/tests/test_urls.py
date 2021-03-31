from django.test import SimpleTestCase
from django.urls import reverse, resolve

from vacancies.views import MainView, ListVacanciesView, DetailVacancyView, \
    DetailCompanyView, ListCategoriesView


class TestUrls(SimpleTestCase):

    # тест проверяет корректность представления главной страницы url-адресу
    def test_main_url(self):
        url = reverse('main')
        self.assertEquals(resolve(url).func.view_class, MainView)

    # тест проверяет корректность представления страницы списка вакансий url-адресу
    def test_vacancies_url(self):
        url = reverse('vacancies')
        self.assertEquals(resolve(url).func.view_class, ListVacanciesView)

    # тест проверяет корректность представления страницы о вакансии url-адресу
    def test_vacancy_detail_url(self):
        url = reverse('vacancy_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DetailVacancyView)

    # тест проверяет корректность представления страницы компании url-адресу
    def test_company_detail_url(self):
        url = reverse('company_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, DetailCompanyView)

    # тест проверяет корректность представления страницы категории url-адресу
    def test_categories_url(self):
        url = reverse('categories', args=['backend'])
        self.assertEquals(resolve(url).func.view_class, ListCategoriesView)
