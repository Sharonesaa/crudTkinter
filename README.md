![CoverImage](https://course-net.com/blog/wp-content/uploads/2022/10/61c323afb777801522775611_CRUD-Preview.png)

CRUD hace referencia a un acrónimo en el que se reúnen las primeras letras de las cuatro operaciones fundamentales de aplicaciones persistentes en sistemas de bases de datos:

Create (Crear registros)
Read bzw. Retrieve (Leer registros)
Update (Actualizar registros)
Delete bzw. Destroy (Borrar registros)

Este proyecto se creó como práctica con el objetivo de llevar acabo estas 4 operaciones fundamentales, utilizando base de datos (SQL) y el lenguaje de programación (Python).

## **Explicación**

A continuación, redactaré la elaboración de mi proyecto, explicando el paso a paso del código.

<img src="src\image0.jpg" alt="Librerias y módulos empleados">

Se importa distintos módulos de tkinter, una librería de Python que proporciona distintas herramientas para administrar ventanas, lo que se quiere lograr es poder crear, leer, actualizar y borrar registros en la base de datos a través de python y estamos empleando esta librería "tkinter".

![tkinter](https://i.ibb.co/wpgtPhc/logoPy.png)


#### **Módulos de tkinter :** ####

Tk: Es como la raíz donde todo va a comenzar “la base”, es el contenedor de todos los widgets(microaplicaciones) que forman la interfaz, no tiene tamaño propio, sino que se adapta a los widgets que contiene.

<img src="src\image1.jpg" alt="Librerias y módulos empleados">

Con el root creamos la raíz/base y luego creamos la app, finalmente el root.mainlopp() es el bucle de la app funciona igual que while True.

Aquí comenzamos a crear la ventana principal “root”, utilizamos el self porque seguro utilizaremos nuevamente esta variable en el código para ubicar elementos en esa ventana, el “title” título o etiqueta que tendrá tu ventana, “geometry” las dimensiones del espacio que ocupará y el resizable (0,0) nos permite que no se pueda modificar el tamaño de la ventana.  

<img src="src\image2.jpg" alt="Librerias y módulos empleados">

<img src="src\image3.jpg" alt="Librerias y módulos empleados">

Label:  Lo utilicé para mostrar texto estático, de ahí que se llame label o etiqueta de texto.
    
LabelFrame: Lo utilicé para mostrar texto dentro de un cuadro o dentro de una ventana.

Button: Es uno de los componentes más utilizados en el diseño de interfaces, nosotros creamos un button y le añadimos comportamiento, para esto creamos un parámetro command que ejecutará un código cuando le des click, y luego le colocamos las dimensiones que quieres que ocupe el botón.

<img src="src\image4.jpg" alt="Librerias y módulos empleados">

<img src="src\image5.jpg" alt="Librerias y módulos empleados">

Toplevel: Lo he utilizado para abrir otra ventana, una ventana secundaria.
     
StringVar: ayuda a administrar el valor de un widget, como una etiqueta o una entrada de manera mas efectiva en el caso de mi proyecto era para que solo se pudiera ingresar 1 letra sin ingresar nada solo dando click ‘F/M’.
     
Radiobutton: este módulo nos ayuda a la selección de solo un botón es decir mientras presionas un botón el otro se va deseleccionar automática.
     
Entry: nos permite ingresar cualquier texto de una línea.
     
ttk: tK temáticos.
     
DateEntry: automatiza la entrada de datos en formato de fecha.

<img src="src\image6.jpg" alt="Librerias y módulos empleados">

<img src="src\image7.jpg" alt="Librerias y módulos empleados">


Otros módulos o funciones que pueden llamar la atención que se encuentra en el desarrollo del código:
       
grid = En español grid es cuadricula y nos ayuda ubicar los datos en la grilla (fila, columna, márgenes), por ejemplo, en el código tenemos:
        
        userEntry = Entry(self.adminFrame)
        userEntry.focus()
        userEntry.grid(row=0, column=1, columnspan=2)

.focus es para que salga el símbolo titilando en Player Name que nos indica que hay que escribir ahí.

<img src="src\image9.jpg" alt="Librerias y módulos empleados">
      
En el código verán en varias ocasiones la palabra lambda, lambda no es más que una función que se utiliza cuando se quiere realizar alguna acción pequeña y concisa, en el código la utilicé mas que todo para minis funciones que recibían argumentos:

    Button(registerFrame, text='Save', command=lambda: self.register(playerName.get(), birthday.get(), sex.get(), email.get()), height=2, width=25).grid(row=5, column=0, columnspan=3, sticky=EW)
     
Destroy: Lo utilizamos para destruir ventanas desaparecerlas:

    self.editWind.destroy()

Treeview: Vista de árbol (o lista jerárquica), presenta información en modo jerárquico y, opcionalmente, en forma de tabla o grilla.

<img src="src\image10.jpg" alt="Librerias y módulos empleados">
<img src="src\image11.jpg" alt="Librerias y módulos empleados">


![mysql](https://3.bp.blogspot.com/-5YHjCuxiOfE/WvhujsArC7I/AAAAAAAADRo/OdYaCBJrxOsgzkJLcwNv0a1GS8rY5-58ACLcBGAs/s1600/python-mysql.jpg)

pymysql: es un conjunto de librerías que permiten interactuar con bases de datos en MySQL escrito completamente en Python.

En este proyecto utilizamos pymysql para trabajar con los datos de una base de datos, primero inicializamos la conexión, colocamos la dirección del servidor, datos de autenticación y nombre de la base de datos, que resulta equivalente a una futura ejecución de la consulta, procedo a la creación de un cursor y ejecución de algunas consultas mediante un parámetro que llamamos ‘query’ que estará recibiendo como resultado de funciones del código.
     
Con la función fetchall traemos los resultados de un select y con commit se hace efectiva la escritura de datos.

<img src="src\image8.jpg" alt="Librerias y módulos empleados">

![diagramas](https://www.mentesliberadas.com/wp-content/uploads/2019/09/diagramas-apps.jpg
)

# <h1 align= "center">**DIAGRAMAS** </h1>

<img src="src\diagrama_entidadrelacion.jpg" alt="Librerias y módulos empleados">
<img src="src\diagrama_diseño.jpg" alt="Librerias y módulos empleados">
<img src="src\diseñoLogico.jpg" alt="Librerias y módulos empleados">

