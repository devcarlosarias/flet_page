import flet as ft


def main(page: ft.Page):
    
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Sistema De Adminstración"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
        
    txtBienvenido = ft.Text("¡Bienvenido!", size=24, text_align="center", width=page.window_width, color="green")
    page.add(txtBienvenido)
    page.update()    

ft.app(main, view=ft.AppView.WEB_BROWSER)
