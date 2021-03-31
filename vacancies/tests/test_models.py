from django.test import TestCase, Client
from django.urls import reverse, resolve

from vacancies.models import Specialty, Company, Vacancy


class TestModels(TestCase):

    # установка значений для проведения теста
    @classmethod
    def setUpTestData(cls):
        Specialty.objects.create(
            code='test',
            title='тесты',
            picture='https://raw.githubusercontent.com/specty_backend.png'
        )
        Company.objects.create(
            name='company',
            location='Moscow',
            logo='https://place-hold.it/100x60',
            description='description',
            employee_count='10')

    # тест поля проверяет значение текстовой метки (verbose_name)
    def test_speciality_code_label(self):
        # получение объекта для тестирования
        spec = Specialty.objects.get(id=1)
        # получение метаданных поля для получения необходимых значений
        field_label = spec._meta.get_field('code').verbose_name
        # сравнить значение с ожидаемым результатом
        self.assertAlmostEquals(field_label, 'code')

    # тест проверяет соответствие максимальной длины наименования компании 128 символам (max_length)
    def test_company_name_max_length(self):
        # получение объекта для тестирования
        company = Company.objects.get(id=1)
        # получение максимальной длины поля
        max_length = company._meta.get_field('name').max_length
        # сравнить значение с ожидаемым результатом
        self.assertEquals(max_length, 128)

    # тест проверяет наличие в модели "нужного вывода" метода (__str__)
    def test_speciality_has_str_name(self):
        # получение объекта для тестирования
        spec = Specialty.objects.get(id=1)
        # сравнить значение с ожидаемым результатом
        self.assertEqual(spec.__str__(), 'тесты')
