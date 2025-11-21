from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import LoginForm, UserProfileForm, UserRegistrationForm


def cadastro_usuario(request):
    if request.user.is_authenticated:
        return redirect(reverse("gerencia:index"))

    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect(reverse("gerencia:index"))
    else:
        form = UserRegistrationForm()

    return render(request, "usuario/cadastro.html", {"form": form})


def login_usuario(request):
    if request.user.is_authenticated:
        return redirect(reverse("gerencia:index"))

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect(reverse("gerencia:index"))
    else:
        form = LoginForm()

    return render(request, "usuario/login.html", {"form": form})



@login_required
def editar_perfil(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect(reverse("usuario:editar_perfil"))
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, "usuario/editar_perfil.html", {"form": form})
