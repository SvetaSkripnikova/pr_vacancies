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
from vacancies.views import main_view, vacancies_view, category_view, vacancy_view, company_view

urlpatterns = [
    path('', main_view),
    path('vacancies/', vacancies_view),
    path('vacancies/<int:id>', vacancy_view),
    path('companies/<int:id>', company_view),
    path('vacancies/cat/<str:cat>/', category_view)
]
