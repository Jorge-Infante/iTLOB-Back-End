from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView
    
    )

#Modelo empleado
from . models import Empleado
#Serializador para modelo empleado
from . serializers import EmpleadoSerializer

class EmpleadoListApiView(ListAPIView):
    """Vista para Leer lista de objetos cempleado (R)"""
    serializer_class = EmpleadoSerializer
    def get_queryset(self):
        return Empleado.objects.all()

class EmpleadoByIdListApiView(ListAPIView):
    """Vista para Leer lista de objetos cempleado (R)"""
    serializer_class = EmpleadoSerializer

    def get_queryset(self):
        id_empleado =self.kwargs['codigo']
        if id_empleado==' ':
            return Empleado.objects.all()
        else:
            lista = Empleado.objects.filter(
                id=id_empleado
            )

            return lista
