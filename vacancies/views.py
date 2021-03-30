from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.db.models import Count

from .models import Company, Specialty, Vacancy
from  django.views.generic import TemplateView, ListView, DetailView

class MainView(TemplateView):
    template_name = "main.html"

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(self, **kwargs)
        context["specialities"] = Specialty.objects.annotate(vacancies_Count=Count('vacancies'))
        context["companies"] = Company.objects.annotate(vacancies_Count=Count('vacancies'))
        return context

def main_view(request):
    return render(request, 'main.html')

def vacancies_view(request):
    return render(request, 'vacancies.html')

def vacancy_view(request):
    return render(request, 'vacancy.html')

def company_view(request):
    return render(request, 'company.html')

def category_view(request):
    return render(request, 'vacancies.html')

