from company_employee_app import models
from django.contrib import auth
from rest_framework import serializers
from django.db import models as django_models

User = auth.get_user_model()


class AdminController():

    def get_company_admin_id(self, company_id: int, is_active=True):
        admin_id = models.Company.objects.get(
            id=company_id, is_active=is_active
        )
        return admin_id.admin_id

    def get_admin_id_by_emp_id(self, id: int, is_active=True):
        admin_id = models.Employee.objects.filter(
            id=id).select_related("company").annotate(
                admin_id=django_models.Subquery(
                    models.Company.objects.filter(
                        id=django_models.OuterRef(
                            "company_id"), is_active=is_active
                    ).values("admin_id")
                )
            )
        return admin_id.values("admin_id")


class EmployeeController():

    def add_employee(
        self, name: str, emp: User, company: models.Company,
            department: str, gender: int, age: int, salary: int,
            dob: str, is_active=True):
        emp_details = models.Employee.objects.create(
            name=name, emp=emp, company=company, dob=dob,
            department=department, gender=gender, age=age, salary=salary,
            is_active=is_active
        )
        emp_details.save()
        return emp_details

    def get_emp_by_id(self, id: int, is_active=True):
        try:
            return models.Employee.objects.get(id=id, is_active=is_active)
        except Exception:
            raise serializers.ValidationError(
                {
                    "result": False,
                    "msg": "Invalid employee id "
                },
                code="validation_error")

    def update_employee_details(
        self, id: int, name: str, gender: int, age: int, dob: str,
            employee_by_id: models.Employee):
        employee_by_id.id = id
        employee_by_id.name = name
        employee_by_id.gender = gender
        employee_by_id.age = age
        employee_by_id.dob = dob
        employee_by_id.save()
        return employee_by_id

    def delete_employee(self, employee_data: models.Employee):
        employee_data.is_active = False
        employee_data.save()
