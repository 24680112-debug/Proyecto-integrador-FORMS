import flet as ft
import re  

def main(page: ft.Page):
    # ---------------- CONFIGURACIÓN DE PÁGINA ----------------
    page.title = "Registro de Estudiantes - TAP"
    page.bgcolor = "#FDFBE3"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT

    def validar_escribiendo(e):
        if e.control.value: 
            e.control.border_color = "black"
            e.control.border_width = 1
            if hasattr(e.control, "helper_text"):
                e.control.helper_text = ""
        page.update()

    txt_nombre = ft.TextField(
        label="Nombre", border_color="black", bgcolor="white", 
        filled=True, fill_color="white", color="black", 
        on_change=validar_escribiendo, expand=True
    )
    txt_control = ft.TextField(
        label="Número de control", border_color="black", bgcolor="white", 
        filled=True, fill_color="white", color="black", 
        on_change=validar_escribiendo, expand=True
    )
    txt_email = ft.TextField(
        label="Email", border_color="black", bgcolor="white", 
        filled=True, fill_color="white", color="black", 
        on_change=validar_escribiendo, expand=True
    )

    # DROPDOWNS (Configurados para evitar el TypeError)
    dd_carrera = ft.Dropdown(
        label="Carrera", 
        expand=True, 
        border_color="black",
        bgcolor="white",
        filled=True,
        fill_color="white",
        color="black",
        options=[
            ft.dropdown.Option("Ingeniería en Sistemas Computacionales"),
            ft.dropdown.Option("Ingeniería Civil"),
            ft.dropdown.Option("Ingeniería Industrial"),
            ft.dropdown.Option("Ingeniería en Gestión Empresarial"),
            ft.dropdown.Option("Ingeniería Mecátronica"),
            ft.dropdown.Option("Ingeniería Electrónica"),
        ]
    )
    dd_carrera.on_change = validar_escribiendo 

    dd_semestre = ft.Dropdown(
        label="Semestre", 
        expand=True, 
        border_color="black",
        bgcolor="white",
        filled=True,
        fill_color="white",
        color="black",
        options=[ft.dropdown.Option(str(i)) for i in range(1, 13)]
    )
    dd_semestre.on_change = validar_escribiendo 

    # RADIO BUTTONS GÉNERO
    genero_group = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Masculino", label="Masculino", fill_color="black"),
            ft.Radio(value="Femenino", label="Femenino", fill_color="black"),
            ft.Radio(value="Otro", label="Otro", fill_color="black"),
        ])
    )

    txt_resultado = ft.Text("", weight=ft.FontWeight.BOLD, selectable=True)

    def es_email_valido(email):
        return re.match(r"^[a-z0-9.]+@[a-z0-9]+\.[a-z]+", email.lower())

    def enviar_click(e):
        campos = [txt_nombre, txt_control, txt_email, dd_carrera, dd_semestre]
        errores = 0

        for campo in campos:
            if not campo.value:
                campo.border_color = "red" 
                campo.border_width = 3
                errores += 1
            else:
                campo.border_color = "green"
                campo.border_width = 1

        if txt_email.value and not es_email_valido(txt_email.value):
            txt_email.border_color = "red"
            txt_email.helper_text = "Formato de correo no válido"
            errores += 1

        if errores == 0 and genero_group.value:
            resumen = (
                f" REGISTRO EXITOSO:\n"
                f"• Estudiante: {txt_nombre.value}\n"
                f"• No. Control: {txt_control.value}\n"
                f"• Email: {txt_email.value}\n"
                f"• Carrera: {dd_carrera.value}\n"
                f"• Semestre: {dd_semestre.value}º\n"
                f"• Género: {genero_group.value}"
            )
            
            txt_resultado.value = resumen
            txt_resultado.color = "green"

            txt_nombre.value = ""
            txt_control.value = ""
            txt_email.value = ""
            dd_carrera.value = None    
            dd_semestre.value = None   
            genero_group.value = None 
            
            for campo in campos:
                campo.border_color = "black"
                campo.border_width = 1
            
            txt_nombre.focus()
            
        elif not genero_group.value and errores == 0:
            txt_resultado.value = "Por favor selecciona un género"
            txt_resultado.color = "red"
        else:
            txt_resultado.value = "Revisa los campos marcados en rojo"
            txt_resultado.color = "red"
        
        page.update()

    btn_enviar = ft.FilledButton(
        content=ft.Text("REGISTRAR ESTUDIANTE", size=16, weight="bold"),
        style=ft.ButtonStyle(bgcolor=ft.Colors.BLUE_300, color="white"),
        width=400,
        on_click=enviar_click
    )

    page.add(
        ft.Column([
            txt_nombre,
            txt_control,
            txt_email,
            ft.Row([dd_carrera, dd_semestre], spacing=10),
            ft.Text("Género:", color="#4D2A32", weight=ft.FontWeight.BOLD),
            genero_group,
            ft.Divider(height=10, color="transparent"),
            btn_enviar,
            txt_resultado
        ], spacing=15)
    )

# EJECUCIÓN
if __name__ == "__main__":
    ft.run(main)