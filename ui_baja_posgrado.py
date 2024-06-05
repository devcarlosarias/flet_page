import flet as ft

def main(page:ft.Page):

    def mostrar_datos(e: ft.ControlEvent):
        etiqueta.visible = True
        page.update()

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

    division = [ft.dropdown.Option("DACyTI"),
                ft.dropdown.Option("DAEA")]
    drpDivision = ft.Dropdown(label="Seleccione su división", options=division)

    posgrado = [ft.dropdown.Option("Ciencias De La Computación"),
                ft.dropdown.Option("Tecnologías De La Información")]
    drpPosgrado = ft.Dropdown(label="Seleccione el posgrado", options=posgrado, on_change=mostrar_datos)

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