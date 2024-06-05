import flet as ft

def main(page:ft.Page):

    def mostrar_datos(e: ft.ControlEvent):
        etiqueta.visible = True
        page.update()

    def mostrar_posgrados(e:ft.ControlEvent):
        lista_posgrado = [ft.dropdown.Option("Doctorado Interinstitucional en Ciencias de la Computación"),
                ft.dropdown.Option("Doctorado en Ciencias de la Computación"),
                ft.dropdown.Option("Maestría en Administración de Tecnologías de la Información"),
                ft.dropdown.Option("Maestría en Tecnologías para el Aprendizaje y el Conocimiento"),
                ft.dropdown.Option("Maestría en Ciencias de la Computación"),
                ft.dropdown.Option("Doctorado en Gestión de Tecnologías de la Información")]
        drpPosgrado.options = lista_posgrado
        drpPosgrado.update()         

    def cerrar_ventana(e:ft.ControlEvent):
        page.window_close()    
            
    def baja_posgrado(e:ft.ControlEvent):
        error = None
        if drpDivision.value is None:
            error = "Selecciona la División"
        elif drpPosgrado.value is None:
            error = "Selecciona el Posgrado"
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
    drpDivision = ft.Dropdown(label="Seleccione su división", options=division, on_change=mostrar_posgrados)

    posgrado = [ft.dropdown.Option("Ciencias De La Computación"),
                ft.dropdown.Option("Tecnologías De La Información")]
    drpPosgrado = ft.Dropdown(label="Seleccione el posgrado", on_change=mostrar_datos)

    etiqueta = ft.Text("¿Seguro que desea dar de baja este Programa?", size=18, visible=False)
    filaEtiqueta = ft.Row([etiqueta], alignment="center")

    btnBaja = ft.ElevatedButton("Dar De Baja", icon="delete", 
                                bgcolor="white",  
                                color="black",                                
                                icon_color="orange",
                                on_click=baja_posgrado)
    btnCancelar = ft.ElevatedButton("Cancelar", 
                                bgcolor="white",  
                                color="black",
                                icon="close", 
                                icon_color="red400", 
                                on_click=cerrar_ventana)

    rowBotones = ft.Row([btnBaja, btnCancelar], alignment="center")
    
    columna = ft.Column([drpDivision,drpPosgrado,filaEtiqueta,rowBotones])
    return columna    


if __name__ == "__main__":
    ft.app(target=main)
