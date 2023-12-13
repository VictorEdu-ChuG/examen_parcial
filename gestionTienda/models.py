from django.db import models

# Create your models here.
class Tienda(models.Model):
    direccion = models.CharField(max_length=32,blank=True,null=True)
    provincia = models.CharField(max_length=32,blank=True,null=True)
    region = models.CharField(max_length=32,blank=True,null=True)
    fecha_creacion = models.DateField()
    telefono_contacto = models.CharField(max_length=32,blank=True,null=True)

class Producto(models.Model):
    descripcion = models.CharField(max_length=32,blank=True,null=True)
    codigo = models.CharField(max_length=32,blank=True,null=True)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    tienda_relacionada = models.ForeignKey(Tienda, on_delete=models.SET_NULL,blank=True,null=True)
    