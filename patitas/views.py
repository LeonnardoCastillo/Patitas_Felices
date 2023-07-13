from django.shortcuts import render, redirect
from .models import Stock, Boleta, detalle_boleta
from .forms import StockForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from patitas.compra import Carrito

# Create your views here.

def Inicio(request):
    return render(request, 'Inicio.html')

def organizacion(request):
    return render(request,'organizacion.html')

def Productos(request):
    jardin = Stock.objects.all()
    datos = {
        'jardin': jardin
    }
    return render(request,'Productos.html', datos)

def Formulario(request):
    return render(request,'Formulario.html')

def Api(request):
    return render(request,'Api.html')

@login_required
def Ver(request):
    patitas = Stock.objects.all()
    datos = {
        'jardin': patitas
    }
    return render(request,'Stock.html', datos)

@login_required
def crear(request):
    if request.method=="POST":
        stockForm = StockForm(request.POST, request.FILES)
        if stockForm.is_valid():
            stockForm.save()     #similar al insert
            return redirect('Ver')
    else:
        stockForm=StockForm()
    return render(request, 'crear.html', {'stock_Form':stockForm})


@login_required
def eliminar(request, id):
    stockEliminado = Stock.objects.get(code=id) #obtenemos un objeto por su id
    stockEliminado.delete()
    return redirect ('Ver')


@login_required
def modificar(request, id):
    stockModificado=Stock.objects.get(code=id)
    datos = {
        'form' : StockForm(instance=stockModificado)
    }
    if request.method=='POST':
        formulario = StockForm(data=request.POST, files=request.FILES,instance=stockModificado)
        if formulario.is_valid:
            formulario.save()
            return redirect('Ver')
    return render(request, 'modificar.html', datos)


def registrar(request):
    data={
        'form':RegistroUserForm()
    }
    if request.method=="POST":
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], 
                    password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect ('Inicio')
        data["form"] = formulario
    return render(request, 'registration/registrar.html',data)

def tienda(request):
    jardin = Stock.objects.all()
    datos={
        'jardin':jardin
    }
    return render(request, 'tienda.html', datos)

def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    patitas = Stock.objects.get(code=id)
    carrito_compra.agregar(patitas=patitas)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    patitas = Stock.objects.get(codee=id)
    carrito_compra.eliminar(patitas=patitas)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    patitas = Stock.objects.get(code=id)
    carrito_compra.restar(patitas=patitas)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Stock.objects.get(code = value['patitas_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)