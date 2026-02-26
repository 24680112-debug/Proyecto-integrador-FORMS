# Proyecto-integrador-FORMS
Explicación del proyecto integrador de la unidad 1. 

A partir del código proporcionado por el profesor, se hicieron unas mejoras al código para su resultado final.

A continuación se explicara el paso a paso de como funciona el código en flet sobre un formulario de estudiantes que contiene los campos de: Nombre, No. de control, Email, Carrera, Semestre, Género y el botón de enviar.
Los cuales contengan estos parámetros:
* No enviar entradas vacías.
* Validar formato de email.
* Se incluyen control

## 1. Preparación y Configuración del Entorno
Antes de dibujar cualquier cosa, definimos las reglas del juego y el estilo visual.
```bash
import flet as ft
import re  

def main(page: ft.Page):
    page.title = "Registro de Estudiantes - TAP"
    page.bgcolor = "#FDFBE3"  # Un color crema suave para no cansar la vista
    page.padding = 30         # Espacio entre el borde de la ventana y el contenido
    page.theme_mode = ft.ThemeMode.LIGHT
```
* import re: Importamos el motor de Expresiones Regulares. Es una herramienta de búsqueda de patrones que usaremos para validar el email más adelante.

* page: ft.Page: En Flet, la "página" es el contenedor raíz. Cualquier cambio que queramos que el usuario vea debe terminar en un page.update().


## 2. Definición de los Componentes de Entrada (UI)
Aquí creamos los objetos. Nota que aún no aparecen en pantalla, solo están guardados en variables.
```bash
# Campos de texto con estilo personalizado
txt_nombre = ft.TextField(
    label="Nombre", 
    border_color="black", 
    bgcolor="white", 
    filled=True, 
    on_change=validar_escribiendo, # Evento: se activa al teclear
    expand=True # Permite que el campo crezca para llenar el espacio
)

# Menú desplegable para el semestre usando un ciclo (range)
dd_semestre = ft.Dropdown(
    label="Semestre", 
    options=[ft.dropdown.Option(str(i)) for i in range(1, 13)] # Crea opciones del 1 al 12
)
```
* on_change: Este es un "event listener". Cada vez que el usuario presiona una tecla, Python llama a la función validar_escribiendo.

* expand=True: Es vital para el diseño responsivo; le dice al componente que ocupe todo el ancho disponible dentro de su fila o columna.


## 3. La Lógica de Validación "En Vivo"
Esta función es lo que hace que la aplicación se sienta profesional y reactiva.
```bash
def validar_escribiendo(e):
    if e.control.value: # 'e.control' es el componente que disparó el evento
        e.control.border_color = "black"
        e.control.border_width = 1
        if hasattr(e.control, "helper_text"):
            e.control.helper_text = ""
    page.update() # Refresca la interfaz para mostrar el cambio de color
```
* e.control: Flet nos pasa un objeto e que contiene quién causó el evento. Así no tenemos que escribir una función diferente para cada cuadro de texto.


## 4. El Procesamiento de Datos (enviar_click)
Este es el algoritmo principal. Se divide en Validación, Cálculo de Errores y Salida.
```bash
def es_email_valido(email):
    # Verifica que el texto tenga formato: algo @ algo . algo
    return re.match(r"^[a-z0-9.]+@[a-z0-9]+\.[a-z]+", email.lower())

def enviar_click(e):
    campos = [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]
    errores = 0

    # 1. Validación de campos vacíos
    for campo in campos:
        if not campo.value:
            campo.border_color = "red" 
            campo.border_width = 3
            errores += 1
```
* Algoritmo de Error: Inicializamos errores = 0. Si al final del ciclo este número es mayor a cero, detenemos el registro.

* Feedback Visual: Cambiamos el border_width a 3 para que el error sea muy evidente visualmente.


## 5. Renderizado y Layout (El Ensamblaje)
Flet usa un sistema de cajas (Columnas y Filas).
```bash
page.add(
    ft.Column([
        txt_nombre,
        txt_control,
        txt_email,
        # Fila para poner dos elementos juntos
        ft.Row([dd_carrera, dd_semestre], spacing=10), 
        ft.Text("Género:", weight=ft.FontWeight.BOLD),
        genero_group,
        btn_enviar,
        txt_resultado
    ], spacing=15)
)
```
* ft.Column: Los elementos dentro de los corchetes [] se apilan verticalmente.

* ft.Row: Se usa aquí para que la Carrera y el Semestre compartan el mismo renglón, lo cual es un estándar en formularios de ingeniería.


### Resumen del Flujo de Datos
1. Usuario interactúa con los componentes de la interfaz.

2. validar_escribiendo limpia advertencias previas en tiempo real.

3. enviar_click actúa como filtro de seguridad (revisa vacíos y formato de email).

4. txt_resultado muestra el veredicto final (Éxito o Error).


## RESULTADO

<img width="1262" height="432" alt="Captura de pantalla 2026-02-24 202955" src="https://github.com/user-attachments/assets/1e0c2307-17df-4232-935b-f6fda7398739" />

<img width="1256" height="459" alt="Captura de pantalla 2026-02-25 212551" src="https://github.com/user-attachments/assets/05b1abcf-d719-422e-9268-2c9e386a0cfa" />

<img width="328" height="167" alt="Captura de pantalla 2026-02-25 212613" src="https://github.com/user-attachments/assets/01b71648-8629-483f-bc0a-0a887961eda9" />
