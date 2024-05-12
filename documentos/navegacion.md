_[Documentación principal](/Documentacion.md)_
---

# NAVEGACIÓN

**Barra de Navegación:**
- **Tipo y Estructura:** La barra de navegación es de tipo **horizontal**, extendiéndose a lo ancho de la parte superior de todas las páginas del sitio web. Esta estructura permite una fácil accesibilidad y visibilidad de las opciones de navegación desde cualquier página.
- **Implementación:** Utiliza **Flexbox**, una técnica de diseño CSS moderna que facilita la disposición de elementos en una línea o en un bloque, dependiendo del tamaño de la pantalla. Esto hace que la barra de navegación sea completamente responsiva y se ajuste a diferentes dispositivos y orientaciones de pantalla.
- **Elementos Incluidos:**
  - **Logotipo:** Ubicado en el extremo izquierdo, sirve como enlace de retorno al inicio.
  - **Enlaces de Navegación:** Enlaces directos a `Inicio`, `Tienda`, `Foro`, y `Contacto y Nosotros`, distribuidos de manera uniforme a lo largo de la barra.
  - **Icono de Usuario:** Colocado hacia el extremo derecho, con un menú desplegable que aparece al hacer clic, permitiendo el ingreso y visualización del nombre del usuario.
  - **Icono de Carrito:** También hacia el extremo derecho, muestra un resumen emergente del carrito de compras al interactuar.

**Interacción y Funcionalidad:**
- **Popup de Usuario:** Al hacer clic en el icono de usuario, se despliega un formulario en un pequeño popup de tipo **modal**, que permite al usuario "iniciar sesión" de manera simulada ingresando su nombre.
- **Manejo de Sesión:** Incluye un botón para "cerrar sesión" que, al ser utilizado, limpia la información de la sesión simulada y actualiza la interfaz para mostrar el formulario de inicio de sesión nuevamente.
- **Estilos Visuales:** La barra de navegación utiliza un esquema de colores que coincide con el diseño general del sitio, ofreciendo una experiencia de usuario coherente y estéticamente agradable.

**Página Principal (Inicio):**
- **Carrusel de Imágenes:** Implementado con **Bootstrap Carousel**, proporciona una transición automática y también responde a interacciones del usuario, mostrando productos destacados o promociones.
- **Secciones de Enlace Rápido:** Accesos directos a áreas de interés como nuevos productos y bestsellers, facilitando la navegación intuitiva para los usuarios.

**Página de la Tienda:**
- **Filtros de Búsqueda:** Implementados con controles de formulario HTML y manipulación de DOM con JavaScript, permiten la filtración dinámica de productos basada en categorías y etiquetas como género o demografía.
