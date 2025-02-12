## Composite View en Python

Este proyecto implementa el patrón de diseño **Composite View** en **Python con Tkinter**, simulando una interfaz de reproducción de videos con un panel lateral de navegación, una barra de búsqueda y una galería de videos con imágenes y títulos.

## Características Principales
- **Diseño Modular:** Implementado usando clases separadas para cada componente.  
- **Patrón Composite View:** La interfaz está compuesta por vistas individuales y vistas compuestas.  
- **Soporte de Imágenes y Fallback:** Si una imagen no existe, se muestra un fondo gris con "Sin imagen".  
- **Interfaz Dinámica:** Se pueden agregar más videos sin modificar el código principal.  

## Tecnologías 
- Python 3.x
- Tkinter (para la interfaz gráfica)
- PIL (Pillow) - Para manejar imágenes

## Características del Patrón Composite View
El patrón **Composite View** permite estructurar la interfaz en vistas simples y compuestas, facilitando la organización modular del código. Sus principales características incluyen:

- **Jerarquía de Vistas:** Define una estructura donde algunas vistas actúan como contenedores de otras.
- **Modularidad:** Facilita la reutilización de componentes sin modificar la vista principal.
- **Escalabilidad:** Permite agregar nuevas vistas sin afectar el resto de la interfaz.
- **Flexibilidad:** Admite la combinación de múltiples componentes visuales en una única vista compuesta.

##  Diagrama de clases UML
![Diagrama UML](https://drive.google.com/uc?export=view&id=1zy9ULx6jP7OU-jKOj9IAAgSd5npcATG5)
