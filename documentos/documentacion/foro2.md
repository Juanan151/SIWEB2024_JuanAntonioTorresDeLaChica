### Documentación del Script `renderComments`

#### Descripción General:
El script `renderComments` se encarga de visualizar comentarios de usuarios en una sección específica de la página del foro. Cada comentario es representado en una tarjeta que incluye un ícono de usuario, el nombre del usuario, el volumen del manga comentado y el texto del comentario.

#### Detalles de Implementación:

1. **Función `renderComments`**:
   - **Objetivo**: Cargar y mostrar dinámicamente los comentarios de los usuarios en la página del foro.
   - **Operación**: Recorre un array predefinido de objetos `comments`, donde cada objeto representa un comentario individual y contiene propiedades como `user`, `vol` (volumen del manga comentado), y `text` (contenido del comentario).

2. **Estructura HTML de un Comentario**:
   - **Contenedor de Comentarios**: Se identifica por el ID `comments` en el DOM.
   - **Tarjeta de Comentario**: Cada comentario se encapsula dentro de una tarjeta (`card`), que a su vez contiene:
     - **Ícono de Usuario**: Un ícono representativo (`bi bi-person-circle`) con un tamaño de 50px que simboliza al usuario que ha hecho el comentario.
     - **Información del Usuario y Volumen**: Muestra el nombre del usuario y el volumen del manga al que se refiere el comentario.
     - **Texto del Comentario**: El contenido del comentario propiamente dicho.

3. **Inserción de Comentarios**:
   - **Método**: Utiliza `innerHTML` para añadir cada comentario generado al contenedor de comentarios.
   - **Formato de Datos**: Asume que el array `comments` está disponible y correctamente formateado con todos los campos necesarios para cada comentario.

4. **Eventos**:
   - **Evento de Carga de Contenido**: La función `renderComments` se invoca automáticamente cuando el evento `DOMContentLoaded` se dispara, asegurando que los comentarios se rendericen tan pronto como el contenido del DOM esté completamente cargado.

