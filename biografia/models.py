from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    biografia = models.TextField()
    url_foto = models.URLField(blank=True, null=True)
    data_criação = models.DateTimeField(auto_now_add=True)
    data_atualização = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome