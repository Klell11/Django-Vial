from django.shortcuts import render, redirect
from .models import Carretera
from django.contrib import messages  # Para mostrar mensajes de error o éxito


def index(request):
    return render(request, 'index.html')
# Vista para listar las carreteras
def listar_carreteras(request):
    carreteras = Carretera.objects.all()
    return render(request, 'listar_carretera.html', {'carreteras': carreteras})

# Vista para crear una nueva carretera
def crear_carretera(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        longitud = request.POST.get('longitud')
        fecha_fin_estimada = request.POST.get('fecha_fin_estimada')

        # Validación simple para verificar que los campos no estén vacíos
        if not nombre or not ubicacion or not longitud or not fecha_fin_estimada:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'crear_carretera.html')

        try:
            longitud = float(longitud)  # Asegurarse de que longitud es un número
        except ValueError:
            messages.error(request, "La longitud debe ser un número válido.")
            return render(request, 'crear_carretera.html')

        # Crear la carretera
        Carretera.objects.create(
            nombre=nombre,
            ubicacion=ubicacion,
            longitud=longitud,
            fecha_fin_estimada=fecha_fin_estimada
        )
        messages.success(request, "Carretera creada exitosamente.")
        return redirect('listar_carreteras')

    return render(request, 'crear_carretera.html')

# Vista para editar una carretera
def editar_carretera(request, pk):
    carretera = Carretera.objects.filter(pk=pk).first()

    if not carretera:
        return redirect('listar_carreteras')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        longitud = request.POST.get('longitud')
        fecha_fin_estimada = request.POST.get('fecha_fin_estimada')

        # Validación para asegurarse de que los campos no estén vacíos
        if not nombre or not ubicacion or not longitud or not fecha_fin_estimada:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'editar_carretera.html', {'carretera': carretera})

        try:
            longitud = float(longitud)  # Validar que longitud es un número
        except ValueError:
            messages.error(request, "La longitud debe ser un número válido.")
            return render(request, 'editar_carretera.html', {'carretera': carretera})

        # Actualizar la carretera
        carretera.nombre = nombre
        carretera.ubicacion = ubicacion
        carretera.longitud = longitud
        carretera.fecha_fin_estimada = fecha_fin_estimada
        carretera.save()

        messages.success(request, "Carretera actualizada exitosamente.")
        return redirect('listar_carreteras')

    return render(request, 'editar_carretera.html', {'carretera': carretera})

# Vista para eliminar una carretera
def eliminar_carretera(request, pk):
    carretera = Carretera.objects.filter(pk=pk).first()

    if carretera:
        carretera.delete()
        messages.success(request, "Carretera eliminada exitosamente.")
    else:
        messages.error(request, "La carretera no existe.")

    return redirect('listar_carreteras')
