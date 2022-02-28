from . import models
from django.contrib import auth
from rest_framework.exceptions import ValidationError

User = auth.get_user_model()


class UserLogin():

    def check_user_login(self, username: str, password: str, user_type: str):
        try:
            if user_type == "admin":
                data = models.UserProfileDetails.objects.select_related(
                    "user").get(
                        user__username=username, user__is_superuser=True)
                if not data.user.check_password(password):
                    raise ValidationError(["password not valid"])
                else:
                    return data
            else:
                data = models.UserProfileDetails.objects.select_related(
                    "user").get(
                        user__username=username, user__is_staff=True)
                if not data.user.check_password(password):
                    raise ValidationError(["password not valid"])
                else:
                    return data
        except Exception:
            raise ValidationError(["username or password not valid"])
