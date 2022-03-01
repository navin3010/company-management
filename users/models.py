from django.db import models
from django.contrib import auth

User = auth.get_user_model()


class UserProfileDetails(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE
    )
    country_code = models.CharField(max_length=3)
    mobile_number = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        #unique_together = ["user"]
        db_table = "user_profile_details"
