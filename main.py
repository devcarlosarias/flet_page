import flet as ft

def main(page: ft.Page):
    
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Sistema De Adminstración"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
       
    logo_ujat = ft.Image(src="https://raw.githubusercontent.com/vjcarlosedit/flet_page/main/assets/logo-ujat.png", width=250)
    filaLogo = ft.Row([logo_ujat], alignment="center")
    
    txtBienvenido = ft.Text("¡Bienvenido!", size=28, text_align="center", color="green")
    filatxtBienvenido = ft.Row([txtBienvenido], alignment="center")

    txtDatos = ft.Text("Av. Universidad s/n, Zona de la Cultura, Col. Magisterial, Vhsa, Centro, Tabasco, Mex. C.P. 86040. Tel (993) 358 15 00", size=14, text_align="center", color="green",)
    filatxtDatos = ft.Row([txtDatos], alignment="center")
    
    contenido = ft.Column(
        [filatxtBienvenido,filaLogo,filatxtDatos], 
        alignment="center",
        spacing=50
    )    

    page.add(contenido)
    page.update()    

ft.app(main, view=ft.AppView.WEB_BROWSER)
