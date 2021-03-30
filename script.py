from django.core import management
from django.core.serializers import python

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pr_vacancies.settings")
django.setup()

from vacancies.models import Company, Specialty, Vacancy
import data as dat

for c in dat.companies:
    Company.objects.create(**c)
for s in dat.specialties:
    Specialty.objects.create(**s)
for j in dat.jobs:
    Vacancy.objects.create(
        title=j["title"],
        speciality=Specialty.objects.filter(code=j["speciality"]).first(),
        company=Company.objects.filter(id=j["company"]).first(),
        skills=j["skills"],
        description=j["description"],
        salary_min=j["salary_min"],
        salary_max=j["salary_max"],
        published_at=j["published_at"],
    )

