from company_employee_app import models as company_models
from company_project_app import models
from django.core import exceptions
from rest_framework import serializers


class ProjectController():

    def add_project(
        self, team_lead_id: int, project_name: str, client_name: str,
            category: str, company: company_models.Company, is_active=True):
        try:
            return models.Project.objects.create(
                team_lead_id=team_lead_id, project_name=project_name,
                client_name=client_name, category=category,
                company=company, is_active=is_active
            )
        except exceptions:
            raise serializers.ValidationError({
                "result": False,
                "msg": "Project is not created check for the data"
            }, code="validation_error")

    def update_project(
        self, team_lead_id: int, project_name: str,
        client_name: str, category: str,
            company: company_models.Company, get_project_data: models.Project):
        get_project_data.team_lead_id = team_lead_id
        get_project_data.project_name = project_name
        get_project_data.client_name = client_name
        get_project_data.category = category
        get_project_data.company = company
        return get_project_data

    def delete_project(self, get_project_data_by_id: models.Project):
        get_project_data_by_id.is_active = False
        get_project_data_by_id.save()
