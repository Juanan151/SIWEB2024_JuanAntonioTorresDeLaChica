# Instala la biblioteca Graphviz si aún no lo has hecho
# pip install graphviz

from graphviz import Digraph

# Crea un nuevo gráfico dirigido
dot = Digraph(comment='Estructura del Sitio Web')

# Agrega nodos (secciones)
dot.node('Home')
dot.node('Catálogo')
dot.node('Detalle del Libro')
dot.node('Contacto y Nosotros')
dot.node('Foro')
dot.node('Carrito de Compras')
dot.node('Colecciones Destacadas')
dot.node('Últimas Novedades')
dot.node('Más Populares')
dot.node('Próximos Lanzamientos')
dot.node('Reseñas y Valoraciones')
dot.node('Recomendaciones Relacionadas')
dot.node('Información de la Empresa')
dot.node('Distribuidoras Registradas')
dot.node('Información Legal')
dot.node('Discusiones Activas')
dot.node('Preguntas y Respuestas')
dot.node('Solicitudes de Licencias')
dot.node('Proceso de Pago')
dot.node('Dirección de Envío')

# Conecta los nodos
dot.edges([
    ('Home', 'Catálogo'),
    ('Catálogo', 'Colecciones Destacadas'),
    ('Catálogo', 'Últimas Novedades'),
    ('Catálogo', 'Más Populares'),
    ('Catálogo', 'Próximos Lanzamientos'),
    ('Catálogo', 'Detalle del Libro'),
    ('Detalle del Libro', 'Reseñas y Valoraciones'),
    ('Detalle del Libro', 'Recomendaciones Relacionadas'),
    ('Contacto y Nosotros', 'Información de la Empresa'),
    ('Contacto y Nosotros', 'Distribuidoras Registradas'),
    ('Contacto y Nosotros', 'Información Legal'),
    ('Foro', 'Discusiones Activas'),
    ('Foro', 'Preguntas y Respuestas'),
    ('Foro', 'Solicitudes de Licencias'),
    ('Carrito de Compras', 'Proceso de Pago'),
    ('Carrito de Compras', 'Dirección de Envío'),
])

# Renderiza el gráfico en formato PNG
dot.render('web_structure', format='png')

print("El diagrama se ha generado correctamente. Puedes encontrarlo en el archivo 'web_structure.png'.")
