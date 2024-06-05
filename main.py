import flet as ft

def main(page: ft.Page):
    
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Sistema De Adminstración"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
       
    txtBienvenido = ft.Text("¡Bienvenido!", size=24, text_align="center", color="green")
    txtDatos = ft.Text("Av. Universidad s/n, Zona de la Cultura, Col. Magisterial, Vhsa, Centro, Tabasco, Mex. C.P. 86040. Tel (993) 358 15 00", size=10, text_align="center", color="green",)
    
    page.add(txtBienvenido)
    page.add(txtDatos)
    page.update()    

ft.app(main, view=ft.AppView.WEB_BROWSER)
