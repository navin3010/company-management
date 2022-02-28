from django.db import models
from django.contrib import auth

User = auth.get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    admin = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "company_name"


class Employee(models.Model):
    emp = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    CHOICES = ((1, "MALE"), (2, "FEMALE"), (3, "TRANSGENDER"))
    gender = models.IntegerField(
        default=None, choices=CHOICES
    )
    age = models.IntegerField()
    salary = models.IntegerField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "employee_details"
