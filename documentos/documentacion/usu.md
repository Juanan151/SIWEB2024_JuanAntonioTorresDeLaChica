### Gestión de Sesión de Usuario en un Sitio Web

#### Funcionalidad General
- **Objetivo Principal**: Permitir a los usuarios ingresar su nombre a través de un formulario y recordar su sesión usando almacenamiento local (`localStorage`).
- **Interacciones Principales**:
  - Mostrar y ocultar el formulario de inicio de sesión.
  - Guardar y borrar el nombre del usuario del almacenamiento local.
  - Actualizar la interfaz del usuario basada en el estado de la sesión (logueado o no).

#### Detalles del Manejo de Eventos

1. **Mostrar/Ocultar Popup de Usuario**:
   - **Evento**: `click` en el icono de usuario.
   - **Acción**: Alternar la visibilidad del popup de inicio de sesión.

2. **Prevenir Cierre Involuntario del Popup**:
   - **Evento**: `click` dentro del popup.
   - **Acción**: Detener la propagación del evento para evitar que clics internos cierren el popup.

3. **Gestión del Formulario de Usuario**:
   - **Evento**: `submit` del formulario de usuario.
   - **Acción**: Prevenir el envío por defecto del formulario, obtener el valor del nombre del usuario, guardarlo en `localStorage`, y actualizar la interfaz para mostrar un saludo personalizado.

#### Funciones Clave

- **`updateUserNameDisplay`**:
  - **Descripción**: Actualiza el contenido del popup para mostrar un saludo personalizado si el usuario está logueado, o restablece el formulario de inicio de sesión si no lo está.
  - **Implementación**: Comprueba si hay un nombre guardado en `localStorage`; si lo hay, muestra el saludo y un botón de cierre de sesión; si no, muestra el formulario.

- **`updateLoginDisplay`**:
  - **Descripción**: Restablece el popup para mostrar el formulario de inicio de sesión y asigna los manejadores de eventos necesarios al formulario y al botón de cerrar sesión.
  - **Implementación**: Incluye la creación de elementos HTML para el formulario y la asignación de eventos para manejar el envío del formulario y la acción de cerrar sesión.

- **`closePopup`**:
  - **Descripción**: Cierra el popup modificando el estilo de display a 'none'.
  - **Uso**: Puede ser llamado para cerrar el popup cuando se realiza alguna acción, como completar el formulario o cerrar sesión.

