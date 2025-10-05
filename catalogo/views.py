from django.shortcuts import render, get_object_or_404
from .models import Producto # Asegúrate de que este import sea correcto

def lista_productos(request):
    # Definir los íconos de cada categoría
    iconos_categorias = {
        'Smartphones': 'fas fa-mobile-alt',
        'Games': 'fas fa-gamepad',
        'Informática': 'fas fa-laptop-code',
        'Electrónica': 'fas fa-tv',
        'Indumentaria o Ropa': 'fas fa-tshirt',
    }

    categorias_data_para_template = []
    
    # Lista de categorías que queremos mostrar
    nombres_categorias_a_mostrar = [
        'Smartphones', 'Games', 'Informática', 'Electrónica', 'Indumentaria o Ropa'
    ]
    
    # Eliminamos la variable cotizacion_usd_ars ya que no se usará.
    
    for nombre_categoria in nombres_categorias_a_mostrar:
        
        # OBTENER PRODUCTOS: Filtramos por el campo 'categoria' que es un CharField
        productos_categoria = Producto.objects.filter(categoria=nombre_categoria).order_by('?')[:12]

        # Procesar precios (solo ARS, ya que el precio base es ARS)
        productos_procesados = []
        for p in productos_categoria:
            
            # El precio de la DB (p.precio) se asigna directamente como precio_ars.
            p.precio_ars = p.precio
            
            # Eliminamos el cálculo de USD (p.precio_ars = p.precio * cotizacion_usd_ars)
            
            # Puedes añadir aquí lógica para ofertas, stock, etc.
            # p.es_oferta = (p.stock < 5) 
            
            productos_procesados.append(p)

        # Solo agregamos la categoría si tiene productos para evitar secciones vacías
        if productos_procesados:
            categorias_data_para_template.append({
                'nombre': nombre_categoria,
                # En lugar de 'slug', usamos el 'nombre' para filtrar en la URL
                'slug_url': nombre_categoria.lower().replace(' ', '-').replace('á', 'a'), 
                'icono_clase': iconos_categorias.get(nombre_categoria, 'fas fa-th-large'),
                'productos': productos_procesados,
            })
    
    context = {
        'titulo': 'Bienvenido a CeluMax',
        'categorias_con_productos': categorias_data_para_template,
    }
    return render(request, 'catalogo/lista_productos.html', context)


def productos_por_categoria(request, nombre_categoria_slug):
    # Convertimos el slug de vuelta al nombre real de la categoría (ej: 'smartphones' -> 'Smartphones')
    nombre_categoria = ' '.join(word.capitalize() for word in nombre_categoria_slug.split('-'))
    
    # Filtramos todos los productos para esa categoría
    productos = Producto.objects.filter(categoria=nombre_categoria).order_by('nombre')
    
    # Procesar precios (solo ARS)
    productos_procesados = []
    for p in productos:
        # El precio de la DB (p.precio) se asigna directamente como precio_ars.
        p.precio_ars = p.precio 
        productos_procesados.append(p)

    context = {
        'titulo': f'Productos de {nombre_categoria}',
        'productos': productos_procesados,
    }
    # Asegúrate de crear un template 'productos_categoria_detail.html' para esta vista
    return render(request, 'catalogo/productos_categoria_detail.html', context)

# Asegúrate de importar get_object_or_404 en la parte superior si no está.
def detalle_producto(request, pk): 
    from django.shortcuts import get_object_or_404 # Asegura que esté importado
    
    # Usamos get_object_or_404 para buscar el producto por su clave primaria (pk)
    producto = get_object_or_404(Producto, pk=pk)

    # Procesar precio (solo ARS)
    # El precio de la DB (producto.precio) se asigna directamente como producto.precio_ars.
    producto.precio_ars = producto.precio

    context = {
        'titulo': f'{producto.nombre}',
        'producto': producto,
    }
    # NOTA: Necesitas crear el template 'detalle_producto.html'
    return render(request, 'catalogo/detalle_producto.html', context)
