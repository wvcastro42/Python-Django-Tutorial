from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True) #introducao-ao-django é um slug
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #auto_now_add adiciona a data e horário quando for criado
    updated = models.DateTimeField(auto_now=True) #salvará a data e horário da alteração

    class Meta:
        ordering = ("-created",)

    def __str__(self) -> str: #método para exibir o nome do artigo na lista de artigos
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={'slug': self.slug})