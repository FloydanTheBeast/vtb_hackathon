from django.db import models
from django.contrib.auth.models import User
import phone_field

genders = [('male', 'male'), ('female', 'female'), ('unknown', 'unknown')]


# Create your models here.

class SearchHistory(models.Model):
    response = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} {self.response}"


class LoanHistory(models.Model):
    response = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} {self.response}"


class ExtraUserData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='', blank=True)
    income_amount = models.IntegerField(default=0, blank=True)
    birth_date_time = models.CharField(default='', max_length=100, blank=True)
    birth_place = models.CharField(default='', max_length=100, blank=True)
    family_name = models.CharField(default='', max_length=100, blank=True)
    first_name = models.CharField(default='', max_length=100, blank=True)
    gender = models.CharField(default=genders[2], max_length=100, choices=genders, blank=True)
    middle_name = models.CharField(default='', max_length=100, blank=True)
    nationality_country_code = models.CharField(default='', max_length=100, blank=True)
    phone = phone_field.PhoneField(default='', blank=True)
