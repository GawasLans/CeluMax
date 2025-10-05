// static/js/carrusel.js

document.addEventListener('DOMContentLoaded', () => {

    function slideCarousel(button, direction) {
        const categoryId = button.dataset.categoryId;
        const wrapper = document.getElementById(`carousel-${categoryId}`);
        
        if (!wrapper) return;

        // Leemos el desplazamiento actual (índice del primer producto visible)
        let currentSlide = parseInt(wrapper.dataset.slide || 0);

        // Número total de productos
        const totalCards = wrapper.querySelectorAll('.producto-card').length;
        
        // Obtenemos el ancho de una tarjeta y del contenedor para calcular cuántas caben
        const cardElement = wrapper.querySelector('.producto-card');
        if (!cardElement) return; // Salir si no hay tarjetas
        
        const cardWidth = cardElement.offsetWidth;
        const containerWidth = wrapper.closest('.carousel-container').offsetWidth;
        
        // Calculamos cuántas tarjetas son visibles (para la lógica de límite)
        // Usamos Math.round() para evitar errores por subpíxeles
        const cardsVisible = Math.round(containerWidth / cardWidth);

        // =======================================================
        // 🚨 CLAVE: Mover de uno en uno (direction * 1) 🚨
        // =======================================================
        let newSlide = currentSlide + direction; 

        // El desplazamiento máximo es el índice del primer producto que queda cortado.
        // Si tienes 12 productos y 6 son visibles, el último índice que puedes tener
        // para que el último producto quede completo es 12 - 6 = 6.
        const maxSlide = totalCards - cardsVisible;
        
        // Lógica de límites
        if (newSlide < 0) {
            newSlide = 0; // No deslizar más a la izquierda
        } else if (newSlide > maxSlide) {
            // Aseguramos que no se deslice más allá del final
            newSlide = maxSlide; 
        }

        // Si cardsVisible es mayor o igual a totalCards (ej: solo 4 productos y caben 6),
        // el maxSlide es negativo o cero. En ese caso, newSlide siempre es 0.
        if (cardsVisible >= totalCards) {
             newSlide = 0;
        }

        // Guardamos el nuevo estado
        wrapper.dataset.slide = newSlide;

        // Calculamos el valor de traslación en píxeles
        const translateValue = newSlide * cardWidth; 
        
        // Aplicamos la transformación CSS para mover el carrusel
        wrapper.style.transform = `translateX(-${translateValue}px)`;
        
        // Ocultar/mostrar flechas cuando llega al límite (mejorando la visibilidad)
        const prevBtn = button.closest('.carousel-wrapper-full').querySelector('.prev-btn');
        const nextBtn = button.closest('.carousel-wrapper-full').querySelector('.next-btn');
        
        if (prevBtn) {
            prevBtn.style.visibility = (newSlide === 0) ? 'hidden' : 'visible';
        }
        if (nextBtn) {
            // Si maxSlide es <= 0, significa que caben todos, ocultamos la flecha "siguiente"
            if (maxSlide <= 0) {
                 nextBtn.style.visibility = 'hidden';
            } else {
                 nextBtn.style.visibility = (newSlide >= maxSlide) ? 'hidden' : 'visible';
            }
        }
    }

    // Inicializar listeners
    document.querySelectorAll('.next-btn').forEach(button => {
        button.addEventListener('click', () => slideCarousel(button, 1)); // direction = +1 (adelante)
    });

    document.querySelectorAll('.prev-btn').forEach(button => {
        button.addEventListener('click', () => slideCarousel(button, -1)); // direction = -1 (atrás)
    });
    
    // Función para inicializar y recalcular el estado en el redimensionamiento
    function initializeCarouselState() {
        document.querySelectorAll('.productos-carousel-wrapper').forEach(wrapper => {
            wrapper.dataset.slide = 0; // Reiniciar la posición
            wrapper.style.transform = `translateX(0px)`;
            
            // Ocultar la flecha de 'Anterior' al inicio
            const prevButton = wrapper.closest('.carousel-wrapper-full').querySelector('.prev-btn');
            if (prevButton) {
                prevButton.style.visibility = 'hidden';
            }
            
            // Forzar la verificación de la flecha 'Siguiente' si caben todos
            const nextButton = wrapper.closest('.carousel-wrapper-full').querySelector('.next-btn');
            if (nextButton) {
                // Usamos una tarjeta ficticia para el cálculo inicial
                const mockButton = { dataset: { categoryId: wrapper.id.replace('carousel-', '') } };
                slideCarousel(mockButton, 0); // Llama a la lógica de límites sin mover
            }
        });
    }
    
    // Inicializar al cargar y al redimensionar la ventana (para mantener el responsive)
    initializeCarouselState();
    window.addEventListener('resize', initializeCarouselState);

});