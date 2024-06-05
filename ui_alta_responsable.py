import flet as ft

def main(page:ft.Page):

    def cerrar_ventana(e:ft.ControlEvent):
        page.window_close()

    def validar_campos(e:ft.ControlEvent):
        error = None
        if txtResponsable.value.strip() == "":        
            error = "Error: Introduce el número de empleado"
        elif txtNombre.value.strip() == "":
            error = "Error: Introduce el nombre del responsable"
        elif drpGrado.value is None:
            error = "Error: Selecciona el grado del responsable"
        elif txtCorreo.value.strip() == "":        
            error = "Error: Introduce el correo del responsable"
        elif drpDivision.value is None:
            error = "Error: Selecciona la división del responsable"
        else:
            guardar_datos()    
        
        if error is not None:
            snackbar = ft.SnackBar(ft.Text(error, color="black"), show_close_icon=True, bgcolor="amber")
            page.snack_bar = snackbar
            snackbar.open = True
            page.update()

    def guardar_datos():
        snackbar = ft.SnackBar(ft.Text("Datos guardados correctamente"), show_close_icon=True, bgcolor="green")
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()

    txtResponsable = ft.TextField(label="Número de empleado")
    etiqueta = ft.Text("(Todo en mayúscula)", size=12, text_align="center")
    txtNombre = ft.TextField(label="Nombre")
    
    opciones = [ft.dropdown.Option("Doctorado"),
                ft.dropdown.Option("Maestría")]
    drpGrado = ft.Dropdown(label="Seleccione su grado", options=opciones)

    txtCorreo = ft.TextField(label="Correo")
    
    division = [ft.dropdown.Option("DACA"),
                ft.dropdown.Option("DACB"),
                ft.dropdown.Option("DACBiol"),
                ft.dropdown.Option("DACEA"),
                ft.dropdown.Option("DACS"),
                ft.dropdown.Option("DACSyH"),
                ft.dropdown.Option("DACyTI"),
                ft.dropdown.Option("DAEA"),
                ft.dropdown.Option("DAIA"),
                ft.dropdown.Option("DAMC"),
                ft.dropdown.Option("DAMJM"),
                ft.dropdown.Option("DAMR")
                    ]
    drpDivision = ft.Dropdown(label="Seleccione su división", options=division)
    
    btnGuardar = ft.ElevatedButton("Guardar", icon="save", 
                                bgcolor="white",  
                                color="black",                                
                                icon_color="green400",
                                on_click=validar_campos)
    btnCancelar = ft.ElevatedButton("Cancelar", 
                                bgcolor="white",  
                                color="black",
                                icon="close", 
                                icon_color="red400",
                                on_click=cerrar_ventana)
    
    rowBotones = ft.Row([btnGuardar, btnCancelar], alignment="center")
    
    columna = ft.Column([txtResponsable,etiqueta,txtNombre,drpGrado,txtCorreo,drpDivision,rowBotones])
    return columna

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
