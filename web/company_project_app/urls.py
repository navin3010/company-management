from django.urls import path
from company_project_app import views


urlpatterns = [
    path("project/", views.ProjectAPI.as_view(), name="project"),
]
