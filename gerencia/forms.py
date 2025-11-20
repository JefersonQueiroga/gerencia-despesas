from django import forms

from .models import Categoria, Despesa


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "descricao"]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "descricao": forms.Textarea(attrs={"class": "form-control"}),
        }


class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = ["titulo", "categoria", "valor", "data", "observacoes", "ativo"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "valor": forms.NumberInput(attrs={"class": "form-control"}),
            "data": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control"}),
            "ativo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class DespesaFiltroForm(forms.Form):
    titulo = forms.CharField(
        label="Título",
        max_length=150,
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Buscar por título...", "class": "form-control"}
        ),
    )
    data_inicio = forms.DateField(
        label="Data Início",
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
    data_fim = forms.DateField(
        label="Data Fim",
        required=False,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )
