from django.contrib.auth.models import Group, User #importa los modelos Group y user
from django.db import models #importa los metodos necesarios para trabajar con modellos

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre Proveedor')
    apellido = models.CharField(max_length=100, null=True, blank=True, verbose_name='Apellido Proveedor')
    celular = models.IntegerField()
    empresa = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre empresa')
    descripcion=models.CharField(max_length=250, null=True, blank=True, verbose_name='Descripcion de los productos')   
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['nombre']   
    def __str__(self):
        return self.proveedor_name

def custom_upload_to(instance, filename):
    return 'product/' + filename



class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
    product_image = models.CharField(max_length=240, null=True, blank=True)
    product_state = models.CharField(max_length=100, null=True, blank=True, default='No')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']
    
    def __str__(self):
        return self.product_name
    
class Proyecto(models.Model):
    proveedor=models.ManyToManyField(Proveedor)
    nombre = models.CharField(max_length=240, null=True, blank=True)
    descripcion = models.CharField(max_length=240, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['nombre']
    
    def __str__(self):
        return self.proyecto_name
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    proveedor=models.ManyToManyField(Proveedor)
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    talla = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre


