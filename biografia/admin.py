from django.contrib import admin
from .models import Pessoa

# Register your models here.
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criação', 'data_atualização')
    search_fields = ('nome',)

admin.site.register(Pessoa, PessoaAdmin)