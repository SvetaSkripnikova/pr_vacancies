from django.contrib import admin

# Register your models here.

from django.test import TestCase

from .models import Company, Specialty, Vacancy


class ViewsTestCase(TestCase):
    # тест проверяет открытие главной страницы с кодом 200 (корректная работа)
    def test_main_loads_properly(self):
        response = self.client.get('http://127.0.0.1:8000')
        self.assertEqual(response.status_code, 200)


class SpecialtyModelTest(TestCase):

    # установка значений для проведения теста
    @classmethod
    def setUpTestData(cls):
        Specialty.objects.create(code='test', title='тесты', picture='https://raw.githubusercontent.com/kushedow/flask-html/master/Django%20Project%202/specialties/specty_backend.png')

    # тест поля проверяет значение текстовой метки (verbose_name)
    def test_code_label(self):
        # получение объекта для тестирования
        spec = Specialty.objects.get(id=1)
        # получение метаданных поля для получения необходимых значений
        field_label = spec._meta.get_field('code').verbose_name
        # сравнить значение с ожидаемым результатом
        self.assertAlmostEquals(field_label, 'code')
