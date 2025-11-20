from django.db import models


class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=100, unique=True)
    descricao = models.TextField("Descrição", blank=True)

    class Meta:
        ordering = ("nome",)
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self) -> str:
        return self.nome


class Despesa(models.Model):
    titulo = models.CharField("Título", max_length=150)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="despesas",
        verbose_name="Categoria",
    )
    valor = models.DecimalField("Valor", max_digits=10, decimal_places=2)
    data = models.DateField("Data da despesa")
    observacoes = models.TextField("Observações", blank=True)
    ativo = models.BooleanField("Ativo", default=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
    atualizado_em = models.DateTimeField("Atualizado em", auto_now=True)

    class Meta:
        ordering = ("-data", "-id")
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"

    def __str__(self) -> str:
        return f"{self.titulo} ({self.valor})"
