from django.db import models


class Tipo(models.Model):
    tipo = models.TextField(max_length=20)

    def __str__(self):
        return self.tipo

class Categoria(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name="categorias")
    nome = models.TextField(max_length=20)

    def __str__(self):
        return self.nome

class Secao(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="secoes")
    secao = models.TextField(max_length=20)

    def __str__(self):
        return self.secao

class Comando(models.Model):
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE, related_name="comandos")
    comando = models.TextField(max_length=300)
    comentario = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="comandos/", blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.secao}: {self.comando[:30]}..."
