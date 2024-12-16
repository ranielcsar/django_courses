from django.urls import path
from login.views import signup, register_user, login_view, logout

urlpatterns = [
    path(
        "",
        login_view,
        name="login",
    ),
    path(
        "cadastrar/",
        signup,
        name="cadastrar",
    ),
    path(
        "register_user/",
        register_user,
        name="register_user",
    ),
]
