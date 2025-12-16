from django.contrib import admin
from django.urls import path
from catalogo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.landing_catalogo, name='landing_catalogo'),

    path('carrito/', views.carrito, name='carrito'),
    path('agregar_carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('aumentar/<int:producto_id>/', views.aumentar, name='aumentar'),
    path('disminuir/<int:producto_id>/', views.disminuir, name='disminuir'),
    path('eliminar/<int:producto_id>/', views.eliminar, name='eliminar'),
    path('vaciar_carrito/', views.vaciar_carrito, name='vaciar_carrito'),
]