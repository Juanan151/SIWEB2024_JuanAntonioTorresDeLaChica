_[Documentación principal](/Documentacion.md)_
--- 

### Estructura General del Documento HTML

**Doctype y Configuración del Lenguaje:**
- `<!doctype html>`: Declara el documento como HTML5.
- `<html lang="es">`: Establece el idioma del documento como español, lo que es esencial para la accesibilidad y los motores de búsqueda.

**Cabecera (Head):**
- `<meta charset="UTF-8" />`: Define la codificación de caracteres UTF-8, que es crucial para la correcta visualización de texto en diversos idiomas.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Asegura que la página sea responsiva y se muestre adecuadamente en todos los dispositivos.
- **Links a recursos CSS:**
  - Bootstrap Icons: Para usar iconografía moderna en la página.
  - Estilo personalizado: Link a una hoja de estilos externa para personalizar más allá de los estilos predeterminados de Bootstrap.

### Cuerpo del Documento (Body)

**Encabezado (Header):**
- **Barra de Navegación:**
  - Utiliza Bootstrap para una navegación responsiva e incluye:
    - Logo de la empresa, que sirve como enlace hacia la página de inicio.
    - Botón de tipo hamburguesa para dispositivos móviles que controla la visibilidad del menú de navegación.
    - Enlaces para navegar a las principales secciones del sitio web: Inicio, Tienda, Foro, Contacto y Nosotros.
    - Formulario de búsqueda que permite a los usuarios buscar libros directamente y enviarlos a la página de la tienda con los resultados filtrados.
    - Icono de carrito de compras que muestra visualmente la cantidad de artículos añadidos.
    - Icono de usuario que al ser clickeado muestra un formulario emergente para iniciar sesión o registrarse.

**Contenido Principal (Main):**
- **Carruseles Dinámicos:**
  - Tres carruseles diferentes (`#multiItemCarousel`, `#threeItemCarousel`, `#secondItemCarousel`) configurados con Bootstrap para mostrar libros populares, novedades y recomendados.
  - Cada carrusel tiene controles para desplazar entre los elementos mostrados.
  - La implementación dinámica asegura que los contenidos se pueden actualizar fácilmente sin cambiar el código HTML directamente.

**Pie de Página (Footer):**
- Contiene información de derechos de autor y un diseño consistente que complementa la estética general del sitio, proporcionando un cierre visual limpio y profesional al final de la página.

### Scripts:
- **Bootstrap Bundle:** Incluye todas las funcionalidades JavaScript necesarias para los componentes interactivos de Bootstrap utilizados en la página.
- **Scripts Personalizados:** `ind.js`, `compra.js`, `usu.js` para manejar las interacciones específicas de la página como la interacción con los carruseles, la gestión del carrito de compras y la funcionalidad del usuario.
