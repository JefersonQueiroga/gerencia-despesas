from django.core.paginator import Paginator
from django.db.models import Sum
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import CategoriaForm, DespesaForm, DespesaFiltroForm
from .models import Categoria, Despesa


def index(request):
    totais = Despesa.objects.aggregate(total=Sum("valor"))
    ultimas_despesas = Despesa.objects.select_related("categoria").all()[:5]
    contexto = {
        "total_despesas": Despesa.objects.count(),
        "valor_total": totais["total"] or 0,
        "total_categorias": Categoria.objects.count(),
        "ultimas_despesas": ultimas_despesas,
    }
    return render(request, "gerencia/index.html", contexto)


def listar_despesas(request):
    despesas = Despesa.objects.select_related("categoria").all()

    form = DespesaFiltroForm(request.GET or None)

    if form.is_valid():
        titulo = form.cleaned_data.get("titulo")
        data_inicio = form.cleaned_data.get("data_inicio")
        data_fim = form.cleaned_data.get("data_fim")

        if titulo:
            despesas = despesas.filter(titulo__icontains=titulo)

        if data_inicio:
            despesas = despesas.filter(data__gte=data_inicio)

        if data_fim:
            despesas = despesas.filter(data__lte=data_fim)

    paginator = Paginator(despesas, 10)
    pagina = request.GET.get("page")
    page_obj = paginator.get_page(pagina)

    contexto = {"despesas": page_obj, "page_obj": page_obj, "form": form}
    return render(request, "gerencia/despesas/lista.html", contexto)


def criar_despesa(request):
    if request.method == "POST":
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("gerencia:lista_despesas"))
    else:
        form = DespesaForm()
    return render(request, "gerencia/despesas/formulario.html", {"form": form})


def editar_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    if request.method == "POST":
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect(reverse("gerencia:lista_despesas"))
    else:
        form = DespesaForm(instance=despesa)
    return render(
        request,
        "gerencia/despesas/formulario.html",
        {"form": form, "despesa": despesa},
    )


def excluir_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    if request.method == "POST":
        despesa.delete()
        return redirect(reverse("gerencia:lista_despesas"))
    return render(
        request,
        "gerencia/despesas/confirma_exclusao.html",
        {"despesa": despesa},
    )


def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(
        request,
        "gerencia/categorias/lista.html",
        {"categorias": categorias},
    )


def criar_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("gerencia:lista_categorias"))
    else:
        form = CategoriaForm()
    return render(
        request,
        "gerencia/categorias/formulario.html",
        {"form": form},
    )


def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect(reverse("gerencia:lista_categorias"))
    else:
        form = CategoriaForm(instance=categoria)
    return render(
        request,
        "gerencia/categorias/formulario.html",
        {"form": form, "categoria": categoria},
    )


def excluir_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == "POST":
        categoria.delete()
        return redirect(reverse("gerencia:lista_categorias"))
    return render(
        request,
        "gerencia/categorias/confirma_exclusao.html",
        {"categoria": categoria},
    )
