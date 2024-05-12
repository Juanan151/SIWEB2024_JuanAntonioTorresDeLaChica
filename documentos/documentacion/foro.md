_[Documentación principal](/Documentacion.md)_
--- 

### Estructura General del Documento HTML

**Doctype y Configuración de Lenguaje:**
- `<!doctype html>`: Declara el documento como HTML5.
- `<html lang="es">`: Establece el idioma del documento en español.

**Cabecera (Head):**
- `<meta charset="UTF-8" />`: Define la codificación de caracteres UTF-8.
- `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`: Asegura que la página es responsiva y se ve bien en todos los dispositivos.
- **Estilos:**
  - Bootstrap 4.5.2: Framework CSS para estilos prediseñados y responsividad.
  - Bootstrap Icons: Provee iconografía.
  - Custom CSS: Enlace a una hoja de estilos personalizados para ajustes específicos del diseño del sitio.

### Cuerpo del Documento (Body)

**Encabezado (Header):**
- **Barra de Navegación:**
  - Incluye logotipo, botón de menú tipo hamburguesa para dispositivos móviles, y enlaces de navegación para las páginas principales del sitio (Inicio, Tienda, Foro, Contacto y Nosotros).
  - Formulario de búsqueda integrado para facilitar la búsqueda directa desde cualquier página.
  - Icono de carrito de compras que muestra el número de ítems agregados.
  - Icono de usuario que despliega un formulario emergente para inicio de sesión o registro.

**Contenido Principal (Main):**
- **Sección del Carrito de Compras:**
  - Contiene un desplegable con los ítems seleccionados, el subtotal de la compra y un botón para proceder al checkout.
- **Foro de Discusión:**
  - Presenta una sección dedicada a comentarios de usuarios sobre diversos temas relacionados con mangas. Los comentarios se cargan dinámicamente en la página, facilitando la interacción y participación de la comunidad.

**Pie de Página (Footer):**
- Incluye información de derechos de autor y está diseñado con un fondo oscuro y texto claro, proporcionando consistencia visual y estructural al final de la página.

### Scripts Incluidos
- **jQuery:** Utilizado para funciones básicas de manipulación del DOM y eventos.
- **Bootstrap Bundle:** Incluye Popper.js, necesario para los componentes de Bootstrap que requieren JavaScript, como los tooltips y popovers.
- **Scripts Personalizados:**
  - `foro.js`: Gestiona la carga y visualización de los comentarios en el foro.
  - `compra.js`: Controla la funcionalidad relacionada con el carrito de compras.
  - `usu.js`: Maneja la interacción del usuario con el sitio, incluyendo la gestión del formulario de inicio de sesión.

