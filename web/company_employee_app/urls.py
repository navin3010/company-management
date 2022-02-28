from django.urls import path
from company_employee_app import views


urlpatterns = [
    path("employee/", views.EmployeeAPI.as_view(), name="employee"),

]
