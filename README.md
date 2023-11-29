# Proyecto_Final


Nombres: Javier Poblete, Joaquin Cantero <br>
Asignatura: Programacion 2 <br>
Profesor: Ignacio Lincolao <br>
Seccion 2 <br>



# Descripcion
El siguiente proyecto busca crear un Programa Interactivo que represente un Ecosistema, Con sus Animales, Plantas, Eventos Climaticos, Interacciones etc.
Se busca Ofrecer una representacion realista de como es el Ciclo de la vida y la reproduccion, y las diversas interacciones entre la flora y fauna. <br>
El simulador posibilitará que los organismos interactúen, teniendo atributos como velocidad, vida y energía, así como comportamientos como explorar, cazar, reproducirse y morir. Se diseño para adaptarse a distintos biomas y condiciones del entorno, siendo lo suficientemente flexible para ello. <br>

Ademas, hay tambien un "Panel de control" que permite al usuario la Inyeccion de diversos eventos climaticos ya asignados en el programa, y tambien obtener informacion de la Flora y Fauna existene en el ecosistema




# Recursos Usados

- Se utilizo el Lenguaje de programacion "Python" para poder hacer posible esta propuesta
![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/7c609436-8ad1-4f55-985d-9760378d6d24)

- Ademas se utilizo la libreria "Pygame" para poder definir a los Animales como los "Sprites", que basicamente son imagenes que se mueven a lo largo del programa
![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/02363d86-c794-4145-93fd-98b8d09297d7)



# Requisitos Minimos

- Tener Visual Studio Code Instalado 
- Tener instalado el Python 3.11.4 instalado (Junto con la libreria Pygame)


# Guia de Instalacion

- Primero nos Metemos al siguiente link para descargar el Visual Studio Code:
https://code.visualstudio.com/download

![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/eb5013ba-6d10-4beb-ae3d-53d1a2b005d7)


Una vez ahi, debemos seleccionar nuestro Sistema Operativo, En nuestro caso fue Windows, Esperan a que se descargue y despues lo instalan. Nosotros no lo descargamos porque ya lo tenemos.


- Luego tenemos que instalar el Python 3.11.4:
  https://www.python.org/downloads/release/python-3114/ <br>
  Entran al link y deben bajar hasta este apartado

  ![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/7bdb5c64-71e8-4938-80c3-63c1f59f37ee)

- Y bueno pues, Dependiendo de el sistema operativo que eligieron, Deben pinchar en el "Installer", dependiendom si es 64 o 32 bits, En nuestro caso pusimos el Windows Installer 64


-Luego ahora si podemos descargar el proyecto (Ojo, primero hay que instalar el pygame para correrlo pero eso ya lo cubriremos mas abajo)
Para eso seleccionan "Code" y luego "Download ZIP"

![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/458468a5-3682-4ff5-a80f-ef568141fd5c)

y lo extraen donde ustedes Quieran


- Luego, abren el Visual Studio Code y presionan donde dice "File" o "Archivo" y luego en "Abrir Carpeta" o "Open Folder" y buscan la carpeta del proyecto y la seleccionan

  ![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/37a5a650-c40b-4cbd-9042-7cb856753743)



  una vez esten en la carpeta, Presionan donde dice "Terminal" y luego "New Terminal"

    ![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/f80c1c53-6e6b-4d13-ba60-198c092dc584)

  Luego Escriben "Pip3 install pygame" y le dan en enter, esperan a que termine la instalacion
  

-Y Listo, ya estaria instalado el programa, solo le dan en el boton de ![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/a026585b-6452-499b-821e-993ff35343c3) y ya esta


# Manual de Uso 

![image](https://github.com/javierrrp/Proyecto_Final/assets/135164108/a7fb7ad0-65c4-47fb-bb3d-18d9fd48e57a)

- El programa Tiene un  Panel de control que permite la inyeccion de eventos climaticos, como lluvia o tormenta, si uno presiona uno de esos botones, uno de esos eventos ocurrira.
Ademas se tiene un monitoreo de los animales vivos y muertos, lo mismo con las plantas, cada vez  que un animal muera, el animal se agregara al conteo que se tiene.


- Hay una cuenta de ciclos en el codigo en el bucle principal, cuando hayan 1440 ciclos, una variable llamada "hora" aumentara, y segun la hora, el fondo de la matriz ira cambiando (Ej si es noche, sera oscura la matriz)

- Por cada ciclo, la vida de los animales ira disminuyendo un 0.01, y cuando la vida de los animales sea menor o igual a 0, el animal dejara de moverse, y entra en descomposicion... Sumado a eso, se agrega el animal muerto al contador de animales muertos.










