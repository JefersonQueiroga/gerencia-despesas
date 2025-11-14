from django.urls import path

from . import views

app_name = "gerencia"

urlpatterns = [
    path("", views.index, name="index"),
    path("despesas/", views.listar_despesas, name="lista_despesas"),
    path("despesas/nova/", views.criar_despesa, name="criar_despesa"),
    path("despesas/<int:despesa_id>/editar/", views.editar_despesa, name="editar_despesa"),
    path(
        "despesas/<int:despesa_id>/excluir/",
        views.excluir_despesa,
        name="excluir_despesa",
    ),
    path("categorias/", views.listar_categorias, name="lista_categorias"),
    path("categorias/nova/", views.criar_categoria, name="criar_categoria"),
    path(
        "categorias/<int:categoria_id>/editar/",
        views.editar_categoria,
        name="editar_categoria",
    ),
    path(
        "categorias/<int:categoria_id>/excluir/",
        views.excluir_categoria,
        name="excluir_categoria",
    ),
]
