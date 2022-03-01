#from asyncio import exceptions
from rest_framework import views, response, status, serializers
from company_project_app import controllers
from company_employee_app import models as company_models
from company_project_app import models as models


class ProjectAPI(views.APIView):

    def post(self, request):
        data = request.data
        team_lead_id = data.get("team_lead_id", "")
        project_name = data.get("project_name", "")
        client_name = data.get("client_name", "")
        category = data.get("category", "")
        company_id = data.get("company_id", "")
        if not team_lead_id and project_name:
            return response.Response(
                {
                    "result": False,
                    "msg": "Empty team_lead_id or project_name",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        if not client_name and company_id:
            return response.Response(
                {
                    "result": False,
                    "msg": "Empty client_name or company",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        if not category:
            return response.Response(
                {
                    "result": False,
                    "msg": "Empty category",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        if models.Project.objects.filter(
            project_name=project_name, category=category,
                is_active=True).exists():
            return response.Response(
                {
                    "result": False,
                    "msg": "Project already added",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            add_project_controller = controllers.ProjectController()
            company = company_models.Company.objects.get(id=company_id)
            add_project_data = add_project_controller.add_project(
                team_lead_id=team_lead_id, project_name=project_name,
                client_name=client_name, category=category,
                company=company, is_active=True
            )
            return response.Response(
                    {
                        "result": True,
                        "msg": "Project created succesfully",
                        "data": f"projct_id: {add_project_data.id}"
                    }, status=status.HTTP_201_CREATED
                )

    def put(self, request):
        data = request.data
        id = data.get("id", "")
        team_lead_id = data.get("team_lead_id", "")
        project_name = data.get("project_name", "")
        client_name = data.get("client_name", "")
        category = data.get("category", "")
        company_id = data.get("company_id", "")
        if not id:
            return response.Response(
                {
                    "result": False,
                    "msg": "Empty id",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        get_project_data = models.Project.objects.get(id=id, is_active=True)
        company = company_models.Company.objects.get(
            id=company_id, is_active=True)
        update_project_data_controller = controllers.ProjectController()
        updated_project_data = update_project_data_controller.update_project(
            team_lead_id=team_lead_id, project_name=project_name,
            client_name=client_name, category=category, company=company,
            get_project_data=get_project_data)
        return response.Response(
                    {
                        "result": True,
                        "msg": "Project updated succesfully",
                        "data": f"projct_id: {updated_project_data.id}"
                    }, status=status.HTTP_200_OK
                )

    def delete(self, request):
        data = request.data
        id = data.get("id", "")
        if not id:
            return response.Response(
                {
                    "result": False,
                    "msg": "Empty id",
                }, status=status.HTTP_400_BAD_REQUEST
            )
        try:
            get_project_data_by_id = models.Project.objects.get(
                id=id, is_active=True
            )
        except Exception:
            raise serializers.ValidationError(
                {
                    "result": False,
                    "msg": "Invalid id or data not present"
                }, code="validation_error")
        delete_project_controller = controllers.ProjectController()
        delete_project_controller.delete_project(
            get_project_data_by_id=get_project_data_by_id)
        return response.Response(
                    {
                        "result": True,
                        "msg": "Project updated succesfully",
                        "data": "Project has been deleted"
                    }, status=status.HTTP_200_OK
                )
