from django.db import models
from django.conf import settings
from django.utils import timezone


class Tipo(models.Model):
    tipo = models.TextField(max_length=20)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='tipos_criados')
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.tipo

class Categoria(models.Model):
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name="categorias")
    nome = models.TextField(max_length=20)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='categorias_criadas')
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

class Secao(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="secoes")
    secao = models.TextField(max_length=20)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='secoes_criadas')
    criado_em = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.secao

class Comando(models.Model):
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE, related_name="comandos")
    comando = models.TextField(max_length=300)
    comentario = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="comandos/", blank=True, null=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comandos_criados')
    criado_em = models.DateTimeField(auto_now_add=True)
    ordem = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordem', '-criado_em']

    def __str__(self):
        return f"{self.secao}: {self.comando[:30]}..."


class Artigo(models.Model):
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE, related_name='artigos')
    titulo = models.CharField(max_length=255)
    arquivo = models.FileField(upload_to='artigos/')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='artigos_criados')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.secao})"
