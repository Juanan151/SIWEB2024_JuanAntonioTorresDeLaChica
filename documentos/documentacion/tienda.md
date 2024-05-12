_[Documentación principal](/Documentacion.md)_
--- 

### Estructura General del Documento HTML

**Doctype y Configuración del Lenguaje:**
- `<!doctype html>`: Declara que el documento es HTML5.
- `<html lang="es">`: Establece el idioma del documento como español, adecuado para la accesibilidad y SEO.

**Cabecera (Head):**
- `<meta charset="UTF-8" />`: Establece la codificación de caracteres para el contenido.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Asegura una visualización adecuada en dispositivos de diferentes tamaños, crucial para el diseño responsivo.
- **Links a recursos CSS:**
  - Hoja de estilos personalizada: Define los estilos específicos del sitio.
  - Bootstrap Icons: Proporciona iconos estilizados y accesibles.

### Cuerpo del Documento (Body)

**Encabezado (Header):**
- **Barra de Navegación:**
  - Utiliza componentes de Bootstrap para una barra de navegación responsiva que incluye:
    - Logotipo de la editorial, que también funciona como enlace a la página de inicio.
    - Botón de navegación tipo hamburguesa para dispositivos móviles que controla la visibilidad del menú de navegación desplegable.
    - Enlaces de navegación que dirigen a las principales secciones del sitio: Inicio, Tienda, Foro, y Contacto y Nosotros.
    - Formulario de búsqueda integrado para facilitar la búsqueda de libros específicos directamente desde cualquier página.
    - Icono de carrito de compras que muestra el número de artículos en el carrito, ofreciendo acceso rápido al carrito de compras.
    - Icono de usuario que despliega un formulario emergente para iniciar sesión o registrarse en el sitio.

**Contenido Principal (Main):**
- **Filtros de Búsqueda:**
  - Paneles de filtros para refinar la búsqueda de productos basados en demografía y género, utilizando checkboxes para una selección múltiple fácil.
- **Contenedor de Productos:**
  - Área dinámica donde se visualizan los productos. Esta sección está diseñada para adaptarse según los filtros aplicados, mostrando los productos en un layout responsivo.
  
**Pie de Página (Footer):**
- Proporciona información de derechos de autor y un cierre visual cohesivo para la página, manteniendo una estética uniforme en todo el sitio.

### Scripts:
- **Bootstrap Bundle:** Incluye todas las funcionalidades de JavaScript necesarias para los componentes interactivos de Bootstrap.
- **Scripts Personalizados:**
  - `tienda.js`: Gestiona la lógica específica para la página de la tienda, incluyendo la filtración y visualización de productos.
  - `compra.js`: Controla las interacciones relacionadas con el carrito de compras.
  - `usu.js`: Administra las funcionalidades relacionadas con la gestión de usuarios.

