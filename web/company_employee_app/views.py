from operator import is_
from rest_framework import views, response, status
from company_employee_app import models, controllers
from rest_framework.permissions import IsAuthenticated
from django.contrib import auth

User = auth.get_user_model()


class EmployeeAPI(views.APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        name = data.get("name", "")
        emp_id = data.get("emp_id", "")
        company_id = data.get("company_id", "")
        department = data.get("department", "")
        gender = data.get("gender", "")
        age = data.get("age", "")
        salary = data.get("salary", "")
        dob = data.get("dob", "")
        user_id = request.user.id
        if not name and str(name):
            return response.Response(
                    {
                        "result": False,
                        "msg": "Empty name or invalid format",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if not emp_id and department:
            return response.Response(
                    {
                        "result": False,
                        "msg": "Empty emp_id or department ",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if not int(gender) and department:
            return response.Response(
                    {
                        "result": False,
                        "msg": "Invalid gender type or empty department ",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if not int(age) and int(salary):
            return response.Response(
                    {
                        "result": False,
                        "msg": "Empty age or salary",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if not int(company_id):
            return response.Response(
                    {
                        "result": False,
                        "msg": "Empty age or salary",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if not dob:
            return response.Response(
                    {
                        "result": False,
                        "msg": "Empty date of birth",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if models.Employee.objects.filter(
                name=name, is_active=True).exists():
            return response.Response(
                    {
                        "result": False,
                        "msg": "Same username already present",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            company_admin_controller = controllers.AdminController()
            company_admin_id = company_admin_controller.get_company_admin_id(
                company_id=company_id, is_active=True
            )
            emp = User.objects.get(id=emp_id, is_active=True)
            company = models.Company.objects.get(id=company_id, is_active=True)
            if user_id == company_admin_id:
                add_employee_details_controller = (
                    controllers.EmployeeController())
                employee_detail = add_employee_details_controller.add_employee(
                    name=name, emp=emp, company=company, dob=dob,
                    department=department, gender=gender, age=age,
                    salary=salary, is_active=True
                )
                return response.Response(
                        {
                            "result": True,
                            "msg": "Employee Added succesfully",
                            "data": f"employe_name:{employee_detail.name}"
                        },
                        status=status.HTTP_201_CREATED,
                    )

    def put(self, request):
        data = request.data
        id = data.get("id", "")
        name = data.get("name", "")
        gender = data.get("gender", "")
        age = data.get("age", "")
        dob = data.get("dob", "")
        if not id:
            return response.Response(
                    {
                        "result": False,
                        "msg": "Empty id",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )
        get_employee_by_id_controller = controllers.EmployeeController()
        employee_by_id = get_employee_by_id_controller.get_emp_by_id(id=id)
        employee_details_update_controller = (
            controllers.EmployeeController()
        )
        updated_data = (
            employee_details_update_controller.update_employee_details(
                id=id, name=name, gender=gender, age=age, dob=dob,
                employee_by_id=employee_by_id
            )
        )
        return response.Response(
                    {
                        "result": True,
                        "msg": "Employee details updated succesfully",
                        "data": f"employe_id:{updated_data.id}"
                    },
                    status=status.HTTP_200_OK,
                )

    def delete(self, request):
        data = request.data
        id = data.get("id", "")
        user = request.user
        user_id = user.id
        company_admin_id_controller = controllers.AdminController()
        admin_id_data = company_admin_id_controller.get_admin_id_by_emp_id(
            id=id)
        admin_id = admin_id_data[0]["admin_id"]
        if admin_id == user_id:
            get_employee_by_id_controller = controllers.EmployeeController()
            employee_data = get_employee_by_id_controller.get_emp_by_id(
                id=id, is_active=True)
            delete_controller = controllers.EmployeeController()
            delete_controller.delete_employee(employee_data=employee_data)
            return response.Response(
                    {
                        "result": True,
                        "msg": "Employee Removed succesfully",
                    },
                    status=status.HTTP_200_OK,
                )
        else:
            return response.Response(
                {
                    "result": False,
                    "msg": "Only admin can remove employee",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
