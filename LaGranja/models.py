from django.db import models

# Create your models here.



class Alimentacion(models.Model):
    descripcion =  models.TextField(null=False,verbose_name="Descripción") 
    dosis = models.TextField(null=False,verbose_name="Dosis")

    def __str__(self):
        return self.dosis
    
    class Meta:
        db_table =  "Alimentacion"
        verbose_name = "Alimentacion"
        verbose_name_plural = "Alimentaciones"
        ordering = ['id']




class Cliente(models.Model):
    cedula =  models.CharField(max_length=50, unique=True,null=False,verbose_name="Cedula")
    nombres =  models.CharField(max_length=200,null=False,verbose_name="Nombres")
    apellidos = models.CharField(max_length=400,null=False,verbose_name="Apellidos")
    direccion = models.CharField(max_length=500,null=False,verbose_name="Dirección")
    telefono = models.CharField(max_length=20, null=False, verbose_name="Teléfono")

    def __str__(self):
        return self.cedula
    

    class Meta: 
        db_table =  "clientes"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['id']




class Porcino(models.Model):
    raza = models.CharField(max_length=50, null=False, verbose_name="Raza")
    edad = models.PositiveSmallIntegerField(null=False, verbose_name="Edad")
    peso = models.FloatField(null=False, verbose_name="Peso")
    alimentacion =  models.ForeignKey(Alimentacion, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)


    def __str__(self):
        return super().__str__()
    
    class Meta: 
        db_table =  "porcinos"
        verbose_name = "Porcino"
        verbose_name_plural = "Porcinos"
        ordering = ['id']











