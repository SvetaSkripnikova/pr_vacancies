"""pr_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from vacancies.views import category_view, MainView, ListVacanciesView, DetailVacancyView, \
    DetailCompanyView

urlpatterns = [
    path('', MainView.as_view(), name="main"),
    path('vacancies/', ListVacanciesView.as_view(), name="vacancies"),
    path('vacancies/<int:pk>', DetailVacancyView.as_view(), name="vacancy_detail"),
    path('companies/<int:pk>', DetailCompanyView.as_view(), name="company_detail"),
    path('vacancies/cat/<str:cat>/', category_view)
]
