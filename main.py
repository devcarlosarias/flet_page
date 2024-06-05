import flet as ft


def main(page: ft.Page):
    
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Sistema De Adminstración"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
    
    logo_ujat = ft.Image(src="icon.png", width=200)
    filaLogo = ft.Row([logo_ujat], alignment="center")



    
    txtBienvenido = ft.Text("¡Bienvenido! Hola Flet")

    contenido = ft.Column(
        [txtBienvenido,filaLogo], 
        alignment="center",
        spacing=50
    )    

    contenedorPrincipal = ft.Container(content=contenido, expand=True)
    fila = ft.Row([navRail, contenedorPrincipal], expand=True)    
    
    page.add(fila)
    page.update()    

ft.app(main, view=ft.AppView.WEB_BROWSER)
