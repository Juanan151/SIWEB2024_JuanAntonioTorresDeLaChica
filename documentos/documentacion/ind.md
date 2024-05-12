### Documentación de Scripts de Carrusel

#### Descripción General:
Los scripts proporcionados están diseñados para inicializar y poblar múltiples carruseles con datos de mangas, permitiendo a los usuarios ver información básica y navegar a páginas de detalles específicas de cada volumen a través de un enlace.

#### Implementación de los Carruseles:
1. **Carrusel Principal (`multiItemCarousel`)**:
   - Se inicializa y llena con datos de mangas para mostrar 4 elementos por vista de carrusel.
   - Función: Crea un nuevo elemento `div` con clase `carousel-item` para cada grupo de 4 mangas y los inserta en el contenedor de carrusel principal.

2. **Segundo Carrusel (`secondCarouselItemsContainer`)**:
   - Similar al principal pero utilizado para una segunda instancia de visualización de carrusel en la página, mostrando diferentes mangas o el mismo set en un orden diferente.
   - Función: Repite la misma lógica que el carrusel principal pero inserta los elementos en un segundo contenedor de carrusel.

3. **Tercer Carrusel (`threeCarouselItemsContainer`)**:
   - Diseñado para mostrar 2 elementos por vista de carrusel, adecuado para destacar mangas específicos o para diferentes propósitos de visualización.
   - Función: Configurado para segmentar los mangas en pares y cada par se muestra en su propia vista dentro del carrusel.

