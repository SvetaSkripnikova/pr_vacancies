from django.shortcuts import render
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


class DetailCompanyView(DetailView):
    model = Company

    def get_context_data(self, **kwargs):
        context = super(DetailCompanyView, self).get_context_data(**kwargs)
        context["company_list"] = Company.objects.all()
        context["vacancies"] = Vacancy.objects.filter(company__id=self.kwargs["pk"])
        context["speciality_list"] = Specialty.objects.all()
        return context

def company_view(request):
    return render(request, 'company.html')

def category_view(request):
    return render(request, 'vacancies.html')

