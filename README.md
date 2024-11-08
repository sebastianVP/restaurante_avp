# SISTEMA DE RESERVAS EN RESTAURANTES
---
Este es un proyecto para desarrollar una Aplicacion Web en Django que permita a los usuarios
seleccionar un restaurante y realizar una reserva en el restaurante de su elecion.
La interfaz deberia ser intuitiva y de facil uso. Para esto podemos usar la libreria Bootstrap.

# DESCRIPCION GENERAL
La aplicacion permite a los usuarios:
*  Ver una lista de restaurantes con sus respectivas descripciones y ubicaciones.
*  Seleeccionar un restaurante especifico y llenar un formulario de reservas con nuestro datos.
* Confirmar la reserva y ver un mensaje de exito.

# Estructura del Proyecto

El proyecto sigue la estructura estandar de Django, vamos a tener una aplicacion llamada reservations. 
Los componentes principales incluyen:
* Modelos: Representa los restaurantes y las reservas en la base de datos
* Vistas: GGestionar la logica de negocio, como lista de restaurantes y la creacion de reservas.
* URLs: Configurar las rutas para acceder a las vistas.
* Plantillas: HTML para representar los datos al usuario con una interfaz.


# Configuracion y Ejecucion del Proyecto:
* Python3.11
* django 5.1
* django Crispy from(opcional para formularios en bootstrap)