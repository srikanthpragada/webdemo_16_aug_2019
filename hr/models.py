from django.db import models


# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=30)
    job = models.CharField(max_length=10, null=True)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.fullname} - {self.job} - {self.salary}"
