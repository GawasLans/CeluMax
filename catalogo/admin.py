from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Esto define las columnas en la lista de productos
    list_display = ('nombre', 'categoria', 'subcategoria', 'precio', 'disponible')
    # Esto crea los filtros laterales
    list_filter = ('categoria', 'subcategoria', 'disponible')
    # Esto define los campos en el formulario de edición/creación
    fields = ('nombre', 'categoria', 'subcategoria', 'descripcion', 'precio', 'stock', 'imagen', 'disponible')


