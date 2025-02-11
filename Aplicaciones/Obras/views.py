from django.shortcuts import render, redirect
from .models import Carretera, Constructora, Presupuesto,Proyecto
from django.contrib import messages  # Para mostrar mensajes de error o éxito

def index(request):
    return render(request, 'index.html')

# Vistas para las constructoras
def listar_constructoras(request):
    constructoras = Constructora.objects.all()  # Obtiene todas las constructoras
    return render(request, 'listar_constructora.html', {'constructoras': constructoras})



def crear_constructora(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        representante = request.POST.get('representante')

        if not nombre or not direccion or not telefono or not representante:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'crear_constructora.html')

        Constructora.objects.create(
            nombre=nombre,
            direccion=direccion,
            telefono=telefono,
            representante=representante
        )
        messages.success(request, "Constructora creada exitosamente.")
        return redirect('listar_constructoras')

    return render(request, 'crear_constructora.html')

def editar_constructora(request, pk):
    constructora = Constructora.objects.filter(pk=pk).first()

    if not constructora:
        return redirect('listar_constructoras')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        representante = request.POST.get('representante')

        if not nombre or not direccion or not telefono or not representante:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'editar_constructora.html', {'constructora': constructora})

        constructora.nombre = nombre
        constructora.direccion = direccion
        constructora.telefono = telefono
        constructora.representante = representante
        constructora.save()

        messages.success(request, "Constructora actualizada exitosamente.")
        return redirect('listar_constructoras')

    return render(request, 'editar_constructora.html', {'constructora': constructora})

def eliminar_constructora(request, pk):
    constructora = Constructora.objects.filter(pk=pk).first()

    if constructora:
        constructora.delete()
        messages.success(request, "Constructora eliminada exitosamente.")
    else:
        messages.error(request, "La constructora no existe.")

    return redirect('listar_constructoras')

# Vistas para las carreteras
def listar_carreteras(request):
    carreteras = Carretera.objects.all()
    return render(request, 'listar_carretera.html', {'carreteras': carreteras})

def crear_carretera(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        longitud = request.POST.get('longitud')
        fecha_fin_estimada = request.POST.get('fecha_fin_estimada')

        if not nombre or not ubicacion or not longitud or not fecha_fin_estimada:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'crear_carretera.html')

        try:
            longitud = float(longitud)
        except ValueError:
            messages.error(request, "La longitud debe ser un número válido.")
            return render(request, 'crear_carretera.html')

        Carretera.objects.create(
            nombre=nombre,
            ubicacion=ubicacion,
            longitud=longitud,
            fecha_fin_estimada=fecha_fin_estimada
        )
        messages.success(request, "Carretera creada exitosamente.")
        return redirect('listar_carreteras')

    return render(request, 'crear_carretera.html')

def editar_carretera(request, pk):
    carretera = Carretera.objects.filter(pk=pk).first()

    if not carretera:
        return redirect('listar_carreteras')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        ubicacion = request.POST.get('ubicacion')
        longitud = request.POST.get('longitud')
        fecha_fin_estimada = request.POST.get('fecha_fin_estimada')

        if not nombre or not ubicacion or not longitud or not fecha_fin_estimada:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'editar_carretera.html', {'carretera': carretera})

        try:
            longitud = float(longitud)
        except ValueError:
            messages.error(request, "La longitud debe ser un número válido.")
            return render(request, 'editar_carretera.html', {'carretera': carretera})

        carretera.nombre = nombre
        carretera.ubicacion = ubicacion
        carretera.longitud = longitud
        carretera.fecha_fin_estimada = fecha_fin_estimada
        carretera.save()

        messages.success(request, "Carretera actualizada exitosamente.")
        return redirect('listar_carreteras')

    return render(request, 'editar_carretera.html', {'carretera': carretera})

def eliminar_carretera(request, pk):
    carretera = Carretera.objects.filter(pk=pk).first()

    if carretera:
        carretera.delete()
        messages.success(request, "Carretera eliminada exitosamente.")
    else:
        messages.error(request, "La carretera no existe.")

    return redirect('listar_carreteras')


# Vistas para los presupuestos
def listar_presupuestos(request):
    presupuestos = Presupuesto.objects.all()
    return render(request, 'listar_presupuesto.html', {'presupuestos': presupuestos})

def crear_presupuesto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        monto = request.POST.get('monto')
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')

        if not nombre or not monto or not fecha or not descripcion:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'crear_presupuesto.html')

        Presupuesto.objects.create(
            nombre=nombre,
            monto=monto,
            fecha=fecha,
            descripcion=descripcion
        )
        messages.success(request, "Presupuesto creado exitosamente.")
        return redirect('listar_presupuestos')

    return render(request, 'crear_presupuesto.html')

def editar_presupuesto(request, pk):
    presupuesto = Presupuesto.objects.filter(pk=pk).first()

    if not presupuesto:
        return redirect('listar_presupuestos')

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        monto = request.POST.get('monto')
        fecha = request.POST.get('fecha')
        descripcion = request.POST.get('descripcion')

        if not nombre or not monto or not fecha or not descripcion:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'editar_presupuesto.html', {'presupuesto': presupuesto})

        presupuesto.nombre = nombre
        presupuesto.monto = monto
        presupuesto.fecha = fecha
        presupuesto.descripcion = descripcion
        presupuesto.save()

        messages.success(request, "Presupuesto actualizado exitosamente.")
        return redirect('listar_presupuestos')

    return render(request, 'editar_presupuesto.html', {'presupuesto': presupuesto})

def eliminar_presupuesto(request, pk):
    presupuesto = Presupuesto.objects.filter(pk=pk).first()

    if presupuesto:
        presupuesto.delete()
        messages.success(request, "Presupuesto eliminado exitosamente.")
    else:
        messages.error(request, "El presupuesto no existe.")

    return redirect('listar_presupuestos')


# Vista para listar los proyectos
def lista_proyectos(request):
    proyectos = Proyecto.objects.all()  # Obtiene todos los proyectos
    constructoras = Constructora.objects.all()  # Obtiene todas las constructoras
    presupuestos = Presupuesto.objects.all()  # Obtiene todos los presupuestos
    carreteras = Carretera.objects.all()  # Obtiene todas las carreteras
    return render(request, 'lista_proyectos.html', {
        'proyectos': proyectos,
        'constructoras': constructoras,
        'presupuestos': presupuestos,
        'carreteras': carreteras
    })


# Vista para crear un nuevo proyecto
def crear_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        constructora_id = request.POST.get('constructora')
        presupuesto_id = request.POST.get('presupuesto')
        carretera_id = request.POST.get('carretera')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        # Verificar si todos los campos fueron completados
        if not nombre or not constructora_id or not presupuesto_id or not carretera_id or not fecha_inicio or not fecha_fin:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'crear_proyecto.html')

        # Crear el proyecto
        Proyecto.objects.create(
            nombre=nombre,
            constructora_id=constructora_id,
            presupuesto_id=presupuesto_id,
            carretera_id=carretera_id,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        messages.success(request, "Proyecto creado exitosamente.")
        return redirect('lista_proyectos')

    return render(request, 'crear_proyecto.html')


# Vista para crear un nuevo proyecto
def crear_proyecto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        constructora_id = request.POST.get('constructora')
        presupuesto_id = request.POST.get('presupuesto')
        carretera_id = request.POST.get('carretera')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')

        if not nombre or not constructora_id or not presupuesto_id or not carretera_id or not fecha_inicio or not fecha_fin:
            messages.error(request, "Todos los campos son obligatorios.")
            return render(request, 'crear_proyecto.html')

        constructora = Constructora.objects.get(id=constructora_id)
        presupuesto = Presupuesto.objects.get(id=presupuesto_id)
        carretera = Carretera.objects.get(id=carretera_id)

        Proyecto.objects.create(
            nombre=nombre,
            constructora=constructora,
            presupuesto=presupuesto,
            carretera=carretera,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin
        )
        messages.success(request, "Proyecto creado exitosamente.")
        return redirect('listar_proyectos')  # Redirige a la lista de proyectos después de crear

    constructoras = Constructora.objects.all()
    presupuestos = Presupuesto.objects.all()
    carreteras = Carretera.objects.all()
    return render(request, 'crear_proyecto.html', {
        'constructoras': constructoras,
        'presupuestos': presupuestos,
        'carreteras': carreteras
    })



def editar_proyecto(request, pk):
    try:
        proyecto = Proyecto.objects.get(pk=pk)  # Buscar el proyecto por su PK
    except Proyecto.DoesNotExist:
        # Si no existe el proyecto, redirigir a la lista de proyectos con un mensaje
        messages.error(request, "El proyecto no existe.")
        return redirect('lista_proyectos')

    if request.method == 'POST':
        # Asumimos que los campos están siendo enviados desde un formulario
        proyecto.nombre = request.POST.get('nombre')
        # Puedes agregar más campos según lo que necesites
        proyecto.save()

        messages.success(request, "Proyecto actualizado exitosamente.")
        return redirect('lista_proyectos')

    # Si es un GET, mostramos el formulario con los datos actuales del proyecto
    return render(request, 'editar_proyecto.html', {'proyecto': proyecto})


def eliminar_proyecto(request, pk):
    # Buscar el proyecto con el pk proporcionado
    proyecto = Proyecto.objects.filter(pk=pk).first()

    if proyecto:
        # Si el proyecto existe, lo eliminamos
        proyecto.delete()
        messages.success(request, "El proyecto ha sido eliminado exitosamente.")
    else:
        # Si el proyecto no existe, mostramos un mensaje de error
        messages.error(request, "El proyecto no existe.")

    return redirect('listar_proyectos')