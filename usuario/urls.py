from django.urls import path

from . import views

app_name = "usuario"

urlpatterns = [
    path("cadastro/", views.cadastro_usuario, name="cadastro"),
    path("login/", views.login_usuario, name="login"),
    path("perfil/", views.editar_perfil, name="editar_perfil"),
]
