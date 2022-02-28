from django.urls import path
from users import views


urlpatterns = [
    path("signup/", views.Signup.as_view(), name="signup"),

    path("signin/", views.Signin.as_view(), name="signin"),

]
