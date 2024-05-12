### Documentación de Scripts de Tienda en Línea

#### Evento de Clic en el Contenedor de Productos
- **Propósito**: Detecta clics en el contenedor de productos y añade productos al carrito si se clickea el botón correspondiente.
- **Función**: `eventListener` que revisa si el elemento clickeado es un botón de "Añadir al carrito", y de ser así, extrae la información del producto (ID, nombre, precio, imagen) y llama a la función `addToCart`.

#### Renderizado de Productos
- **Función `renderProducts`**:
  - **Descripción**: Limpia el contenedor de productos y lo llena con tarjetas de productos que contienen información relevante como imagen, nombre, precio y botones interactivos.
  - **Dinámica de Filas**: Asegura que cada fila contenga hasta tres productos. Crea una nueva fila después de cada tercero producto.
  - **Estructura de Tarjetas**: Cada tarjeta de producto contiene una imagen, título, precio y botones para más información y para añadir al carrito.

#### Filtrado de Productos
- **Función `applyFilters`**:
  - **Recopilación de Filtros**: Obtiene los valores de los checkboxes seleccionados tanto para demografías como géneros.
  - **Filtrado de Productos**: Filtra el array de productos basándose en demografías y géneros seleccionados y luego renderiza los productos filtrados.

#### Búsqueda de Productos
- **Función `filterBooks`**:
  - **Propósito**: Filtra los productos basándose en una cadena de búsqueda que compara el nombre del producto.
  - **Activación**: Se activa al cargar la página, verificando si hay un parámetro de búsqueda en la URL.

#### Interacción con la URL
- **Manejo de Parámetros URL**:
  - Examina si hay un parámetro de búsqueda en la URL al cargar la página. Si existe, llama a `filterBooks` con el valor de búsqueda; de lo contrario, renderiza todos los productos.
