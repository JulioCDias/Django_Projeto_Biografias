from django.urls import path
from .views import index, list_biographies, detail_biography

urlpatterns = [
    path('', index, name='index'),
    path('lista/', list_biographies, name='lista'),
    path('detalhe/<int:pessoa_id>/', detail_biography, name='detalhe'),
]