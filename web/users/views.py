from rest_framework import views, permissions, status
from users import serializers, controllers
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class Signup(views.APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        user = serializers.CreateUser(
            request, data, is_active=True
        )
        return Response(
            {
                "result": f"sucessfully created a user = {user.username}",
                "user_id": user.id
            },
            status=status.HTTP_201_CREATED,
        )


class Signin(views.APIView):

    def post(self, request):
        data = request.data
        username = data.get("username", "")
        password = data.get("password", "")
        user_type = data.get("user_type", "")
        if not username:
            return Response(
                {
                    "result": False,
                    "msg": "Empty username"
                }
            )
        if not password:
            return Response(
                {
                    "result": False,
                    "msg": "Empty password"
                }
            )
        if not user_type:
            return Response(
                {
                    "result": False,
                    "msg": "Empty user_type"
                }
            )
        user_login = controllers.UserLogin()
        data = user_login.check_user_login(
            username=username, password=password, user_type=user_type)
        user = data.user
        token = Token.objects.get_or_create(user=user)[0]
        return Response(
            {
                "result": "success",
                "token": token.key
            },
            status=status.HTTP_200_OK
        )
