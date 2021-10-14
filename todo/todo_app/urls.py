from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('hapus/<delete_id>',views.delete, name='hapus'),
    path('login/',views.masuk, name='login'),
    path('logout/',views.keluar, name='logout'),
    path('register/',views.daftar, name='register'),
    path('daftar/',views.buat, name='daftar'),
    
]