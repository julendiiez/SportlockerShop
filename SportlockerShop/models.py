from django.db import models

# Create your models here.


class Usuario(models.Model):
    nombre=models.CharField(max_length=50)
    contrasenya=models.CharField(max_length=15)
    email=models.EmailField()
    def __str__(self):
        return f"{self.nombre}"

class Ropa(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    cantidad=models.IntegerField()
    imagen1=models.TextField()
    imagen2=models.TextField()
    imagen3=models.TextField()
    articuloTop=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.nombre}"


class Compra(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    ropa=models.ManyToManyField(Ropa)
    fechaDeCompra=models.DateField()

    def __str__(self):
        return f"Compra de {self.usuario.nombre} {self.fechaDeCompra}"

class Camiseta(Ropa):
    talla=models.CharField(max_length=2)


class Zapatilla(Ropa):
    talla=models.IntegerField()

class Sudadera(Ropa):
    conCapucha=models.BooleanField()
    talla=models.CharField(max_length=2)
