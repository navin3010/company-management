from django.db import models
from django.contrib import auth
from company_employee_app import models as company_models

User = auth.get_user_model()


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    team_lead = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    client_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    company = models.ForeignKey(
         company_models.Company, on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "project"
