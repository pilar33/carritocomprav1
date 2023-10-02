from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from .Carrito import Carrito
from CarritoApp.models import Productos


def tienda(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Productos.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(iidproducto=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(iidproducto=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Productos.objects.get(iidproducto=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")