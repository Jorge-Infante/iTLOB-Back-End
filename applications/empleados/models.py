from django.db import models

class Empleado(models.Model):
    name = models.CharField('Nombre', max_length=50)
    contractTypeName = models.CharField('Nombre-tipo-contrato', max_length=50)
    roleId = models.PositiveIntegerField()
    roleName = models.CharField('Nombre rol', max_length=50)
    roleDescription = models.CharField('Rol-Descripcion', max_length=50)
    hourlySalary = models.PositiveIntegerField()
    monthlySalary = models.PositiveIntegerField()


    def __str__(self):
        return str(self.id)+ ' - '+ self.name 
