from django.db import models
from .categorias import Categorias
from .editora import Editora
from .autor import Autor
from uploader.models import Image

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=32, null=True, blank=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, null=True, blank=True)
    categoria = models.ForeignKey(Categorias,on_delete=models.PROTECT,related_name="livros", null=True, blank=True,)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="livros", null=True, blank=True)

    capa = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"({self.id}) {self.titulo} {self.quantidade} - {self.autor}"
