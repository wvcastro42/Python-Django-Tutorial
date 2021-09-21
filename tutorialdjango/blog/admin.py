from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
# exibir as colunas/campos: title', 'slug', 'author', 'created', 'updated ao listar
# AQUI dá para fazer filtros, barra de busca, mudar a ordenação dos dados
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'updated')
    prepopulated_fields = {'slug': ('title',)}