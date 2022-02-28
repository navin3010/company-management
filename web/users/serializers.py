from rest_framework import serializers
from django.contrib import auth
from users.models import UserProfileDetails
from django.core.validators import validate_email

User = auth.get_user_model()


def CreateUser(request, data, is_active):
    first_name = request.data.get("first_name", "")
    username = data.get("username", "")
    password = data.get("password", "")
    mobile_number = data.get("mobile_number", "")
    country_code = data.get("country_code", "")
    email = data.get("email", "")
    user_type = data.get("user_type", "")
    is_active = is_active
    if User.objects.filter(username=username).exists():
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "Username Already Present"
            },
            code="validation_error",
        )
    if not first_name:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "first_name should not be empty."
            },
            code="validation_error",
        )
    if not username:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "UserName should not be empty."
            },
            code="validation_error",
        )
    if not password:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "password should not be empty."
            },
            code="validation_error",
        )
    if not mobile_number:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "mobile number should not be empty."
            },
            code="validation_error",
        )
    if not mobile_number.isdigit():
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "mobile number should be only digit"
            },
            code="validation_error",
        )
    if not country_code:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "country code should not be empty."
            },
            code="validation_error",
        )
    if not email:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "email id should not be empty."
            },
            code="validation_error",
        )
    try:
        validate_email(email)
    except Exception:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "email id should not be empty."
            },
            code="validation_error",
        )
    if not user_type:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "email id should not be empty."
            },
            code="validation_error",
        )
    if user_type == "admin":
        user = User(
            first_name=str(first_name), username=str(username),
            email=str(email), is_active=is_active, is_superuser=True)
        user.set_password(password)
        try:
            user.save()
        except Exception:
            raise serializers.ValidationError(
                {
                    "result": False,
                    "msg": "User not saved"
                },
                code="validation_error",
            )
        user_profile(user, country_code, mobile_number, is_active)
        return user
    if user_type == "staff":
        user = User(
            first_name=str(first_name), username=str(username),
            email=str(email), is_active=is_active, is_staff=True)
        user.set_password(password)
        try:
            user.save()
        except Exception:
            raise serializers.ValidationError(
                {
                    "result": False,
                    "msg": "User not saved"
                },
                code="validation_error",
            )
        user_profile(user, country_code, mobile_number, is_active)
        return user
    else:
        raise serializers.ValidationError(
            {
                "result": False,
                "msg": "invalid user type"
            },
            code="validation_error",
        )


def user_profile(user, country_code, mobile_number, is_active=True):
    create_user_profile = UserProfileDetails(
        user=user, country_code=country_code,
        mobile_number=mobile_number, is_active=is_active)
    create_user_profile.save()
