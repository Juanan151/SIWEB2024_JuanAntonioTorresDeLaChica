### Documentación del Script de Gestión del Carrito de Compras

#### Funciones y Eventos:

1. **Escucha del botón del carrito de compras**:
   - **Elemento**: `#cart-btn`
   - **Evento**: `click`
   - **Función**: `toggleCartVisibility`
   - **Descripción**: Esta función se activa al hacer clic en el botón del carrito y se encarga de mostrar u ocultar el dropdown del carrito de compras.

2. **Añadir al carrito**:
   - **Función**: `addToCart`
   - **Parámetros**: `id`, `name`, `price`, `image`
   - **Operación**: Crea un nuevo elemento de lista dentro del carrito con la imagen, nombre, precio del producto y un botón para remover el ítem.
   - **Actualizaciones**: Llama a `updateCartTotal` para recalcular el total del carrito y a `saveCartItems` para guardar el estado del carrito en el almacenamiento local.

3. **Remover ítem del carrito**:
   - **Elemento**: `.cart-items`
   - **Evento**: `click` (delegado a `.remove-item-btn`)
   - **Función**: `removeItemFromCart`
   - **Descripción**: Remueve el ítem del carrito cuando se hace clic en el botón de remover. Posteriormente actualiza el total y guarda los cambios.

4. **Actualizar el total del carrito**:
   - **Función**: `updateCartTotal`
   - **Operación**: Calcula el total del carrito sumando los precios de cada ítem y actualiza el contenido del elemento `#cart-subtotal` y el contador `#cart-count`.

5. **Guardar los ítems del carrito en el almacenamiento local**:
   - **Función**: `saveCartItems`
   - **Descripción**: Recopila los detalles de los ítems del carrito desde el DOM y los almacena en `localStorage` como un arreglo JSON.

6. **Alternancia de visibilidad del carrito**:
   - **Función**: `toggleCartVisibility`
   - **Operación**: Cambia la propiedad `display` del dropdown del carrito, alternando entre visible e invisible según su estado actual.

7. **Ajuste de posición del carrito durante el desplazamiento**:
   - **Evento**: `scroll`
   - **Función**: `adjustCartPosition`
   - **Descripción**: Ajusta la posición del dropdown del carrito en relación con el pie de página durante el desplazamiento, asegurando que no se superponga con el footer.

8. **Proceso de compra**:
   - **Elemento**: `#go-to-checkout`
   - **Evento**: `click`
   - **Descripción**: Verifica si el carrito tiene ítems y, de ser así, muestra una alerta de agradecimiento y vacía el carrito visualmente y en el almacenamiento local.
