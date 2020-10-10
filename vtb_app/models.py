from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class SearchHistory(models.Model):
    car = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} {self.car}"
