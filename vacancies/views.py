from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.db.models import Count

from .models import Company, Specialty, Vacancy
from django.views.generic import TemplateView, ListView, DetailView

class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context["specialities"] = Specialty.objects.annotate(vacancies_Count=Count('vacancies'))
        context["companies"] = Company.objects.annotate(vacancies_Count=Count('vacancies'))
        return context


class ListVacanciesView(ListView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(ListVacanciesView, self).get_context_data(**kwargs)
        context["title"] = "Все вакансии"
        context["object_list"] = Vacancy.objects.all()
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class DetailVacancyView(DetailView):
    model = Vacancy

    def get_context_data(self, **kwargs):
        context = super(DetailVacancyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class ListCategoriesView(ListView):
    model = Vacancy
    context_object_name = "vacancy_list"

    def get_context_data(self, **kwargs):
        context = super(ListCategoriesView, self).get_context_data(**kwargs)
        context["title"] = get_object_or_404(Specialty, code=self.kwargs["code"]).title
        context["object_list"] = Vacancy.objects.filter(speciality__title=context["title"])
        context["company_list"] = Company.objects.all()
        context["speciality_list"] = Specialty.objects.all()
        return context


class DetailCompanyView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(DetailCompanyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["vacancies"] = Vacancy.objects.filter(company__id=self.kwargs["pk"])
        context["speciality_list"] = Specialty.objects.all()
        return context

