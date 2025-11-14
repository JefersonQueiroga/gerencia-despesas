from django import forms

from .models import Categoria, Despesa


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            widget = field.widget
            base_css = widget.attrs.get("class", "")
            if isinstance(widget, forms.Select):
                css_class = "form-select"
            elif isinstance(widget, forms.CheckboxInput):
                css_class = "form-check-input"
            else:
                css_class = "form-control"
            widget.attrs["class"] = f"{base_css} {css_class}".strip()


class CategoriaForm(BootstrapModelForm):
    class Meta:
        model = Categoria
        fields = ["nome", "descricao"]


class DespesaForm(BootstrapModelForm):
    class Meta:
        model = Despesa
        fields = ["titulo", "categoria", "valor", "data", "observacoes"]
        widgets = {
            "data": forms.DateInput(attrs={"type": "date"}),
        }
