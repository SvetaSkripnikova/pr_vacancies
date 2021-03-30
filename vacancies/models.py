from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    logo = models.URLField(default='https://place-hold.it/100x60')
    description = models.CharField(max_length=3000)
    employee_count = models.IntegerField()

    def __str__(self):
        return self.name


class Specialty(models.Model):
    code = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    picture = models.URLField(default='https://place-hold.it/100x60')

    def __str__(self):
        return self.code


class Vacancy(models.Model):
    title = models.CharField(max_length=128)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=128)
    description = models.CharField(max_length=3000)
    salary_min = models.IntegerField
    salary_max = models.IntegerField
    published_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

