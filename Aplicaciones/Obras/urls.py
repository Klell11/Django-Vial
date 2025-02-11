from django.urls import path
from . import views

urlpatterns = [

    
    path('', views.index, name='index'),
    # Rutas para las carreteras
    path('listar/carreteras/', views.listar_carreteras, name='listar_carreteras'),
    path('crear/carretera/', views.crear_carretera, name='crear_carretera'),
    path('editar/carretera/<int:pk>/', views.editar_carretera, name='editar_carretera'),
    path('eliminar/carretera/<int:pk>/', views.eliminar_carretera, name='eliminar_carretera'),

    # Rutas para las constructoras
    path('listar/constructoras/', views.listar_constructoras, name='listar_constructoras'),
    path('crear/constructora/', views.crear_constructora, name='crear_constructora'),
    path('editar/constructora/<int:pk>/', views.editar_constructora, name='editar_constructora'),
    path('eliminar/constructora/<int:pk>/', views.eliminar_constructora, name='eliminar_constructora'),

    # Rutas para los presupuestos
    path('listar/presupuestos/', views.listar_presupuestos, name='listar_presupuestos'),
    path('crear/presupuesto/', views.crear_presupuesto, name='crear_presupuesto'),
    path('editar/presupuesto/<int:pk>/', views.editar_presupuesto, name='editar_presupuesto'),
    path('eliminar/presupuesto/<int:pk>/', views.eliminar_presupuesto, name='eliminar_presupuesto'),

# Rutas para los proyectos
    path('listar/proyectos/', views.lista_proyectos, name='listar_proyectos'),
    path('listar/proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('crear/proyecto/', views.crear_proyecto, name='crear_proyecto'),
    path('editar/proyecto/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),  # Ruta para editar
    path('eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),

   

]
