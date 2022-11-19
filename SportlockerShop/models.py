from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    contraseña=models.CharField(max_length=15)
    email=models.EmailField()

class Ropa(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    cantidad=models.IntegerField()
    imagen=models.TextField(default="")


class Compra(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    ropa=models.ManyToManyField(Ropa)
    fechaDeCompra=models.DateField()

class Camiseta(Ropa):
    talla=models.CharField(max_length=2)


class Zapatilla(Ropa):
    talla=models.IntegerField()

class Sudadera(Ropa):
    conCapucha=models.BooleanField()
    talla=models.CharField(max_length=2)
