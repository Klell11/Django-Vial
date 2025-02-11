from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('listar/', views.listar_carreteras, name='listar_carreteras'),
    path('crear/', views.crear_carretera, name='crear_carretera'),
    path('editar/<int:pk>/', views.editar_carretera, name='editar_carretera'),
    path('eliminar/<int:pk>/', views.eliminar_carretera, name='eliminar_carretera'),
]
