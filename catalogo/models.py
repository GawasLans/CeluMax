from django.db import models

# 1. Definir las opciones para el campo 'categoria'
CATEGORIAS_PRINCIPALES = [
    ('Smartphones', 'Smartphones'),
    ('Games', 'Games'),
    ('Informática', 'Informática'),
    ('Electrónica', 'Electrónica'), # Coincide con tu valor por defecto
    ('Indumentaria o Ropa', 'Indumentaria o Ropa'),
]

# 2. Definir las opciones para el campo 'subcategoria'
SUBCATEGORIAS_CHOICES = [
    # Smartphones
    ('Celulares', 'Celulares'),
    ('Relojes Inteligentes', 'Relojes Inteligentes'),
    ('Accesorios SM', 'Accesorios'),
    # Games
    ('Consolas', 'Consolas'),
    ('Juegos', 'Juegos'),
    ('Accesorios GM', 'Accesorios'),
    # Informática
    ('Hardware', 'Hardware'),
    ('Perifericos', 'Perifericos'),
    # Electrónica
    ('TV, Audio y Video', 'TV, Audio y Video'),
    ('Teléfonos', 'Teléfonos'),
    ('Seguridad', 'Seguridad'),
    ('Fotografia y Filmacion', 'Fotografia y Filmacion'),
    # Indumentaria o Ropa
    ('Remeras', 'Remeras'),
    ('Pantalones', 'Pantalones'),
    ('Zapatillas', 'Zapatillas'),
    ('Gorras', 'Gorras'),
]

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    
    # CAMBIO: Usamos choices para la categoría principal
    categoria = models.CharField(
        max_length=100, 
        choices=CATEGORIAS_PRINCIPALES, 
        default='Electrónica'
    ) 
    
    # CAMBIO: NUEVO CAMPO para la subcategoría
    subcategoria = models.CharField(
        max_length=100, 
        choices=SUBCATEGORIAS_CHOICES, 
        blank=True, 
        null=True
    )
    
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    disponible = models.BooleanField(default=True)
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
