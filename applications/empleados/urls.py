from django.urls import path, re_path

from . import views
app_name = 'empleados_app'

urlpatterns = [
    
    path (
        'api/employee/list/',
          views.EmpleadoListApiView.as_view(), 
          name='list_employee'
    ),
    path (
        'api/employee/listId/<str:codigo>/',
          views.EmpleadoByIdListApiView.as_view(), 
          name='list_employee'
    ),
    
]