import flet as ft


def main(page: ft.Page):
    
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Sistema De Adminstración"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
    
    logo_ujat = ft.Image(src="https://github.com/vjcarlosedit/flet_page/raw/main/assets/logo-ujat.png", width=200)
    filaLogo = ft.Row([logo_ujat], alignment="center")
    
    txtBienvenido = ft.Text("¡Bienvenido!", size=24, text_align="center", width=page.window_width, color="green")
    txtDatos = ft.Text("Av. Universidad s/n, Zona de la Cultura, Col. Magisterial, Vhsa, Centro, Tabasco, Mex. C.P. 86040. Tel (993) 358 15 00", size=10, text_align="center", width=page.window_width, color="green", height=200)

    btnNuevoPosgrado = ft.NavigationRailDestination(label="Nuevo Posgrado", icon="add_circle_outline", selected_icon="add_circle")
    btnNuevoResponsable = ft.NavigationRailDestination(label="Nuevo Responsable", icon="person_add_outlined", selected_icon="person_add_rounded")
    btnBajaPosgrado = ft.NavigationRailDestination(label="Bajas De Posgrados", icon="ARCHIVE_OUTLINED", selected_icon="ARCHIVE")
    btnReportesPosgrado = ft.NavigationRailDestination(label="Reportes Posgrados", icon="TABLE_CHART_OUTLINED", selected_icon="TABLE_CHART_ROUNDED"
    btnReportesResponsable = ft.NavigationRailDestination(label="Reportes Responsables", icon="TABLE_CHART_OUTLINED", selected_icon="TABLE_CHART_ROUNDED")
    btnReportesDivision = ft.NavigationRailDestination(label="Reportes División", icon="TABLE_CHART_OUTLINED", selected_icon="TABLE_CHART_ROUNDED")
    
    listaBotones = [btnNuevoPosgrado, btnNuevoResponsable, btnBajaPosgrado, btnReportesPosgrado, btnReportesResponsable, btnReportesDivision]
    
    contenido = ft.Column(
        [txtBienvenido,filaLogo,txtDatos], 
        alignment="center",
        spacing=50
    )    

    navRail = ft.NavigationRail(bgcolor="green50", destinations=listaBotones)
    contenedorPrincipal = ft.Container(content=contenido, expand=True)
    fila = ft.Row([navRail, contenedorPrincipal], expand=True)    
    
    page.add(fila)
    page.update()    

ft.app(main, view=ft.AppView.WEB_BROWSER)
