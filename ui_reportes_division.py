import flet as ft
from simpledt import SQLDataTable

def main(page: ft.Page):

    sql = SQLDataTable('sqlite', 'posgrado.sqlite3', 'division')
    tblDivision = sql.datatable

    tblDivision.bgcolor = ft.colors.GREEN_200
    tblDivision.border = ft.border.all(2, ft.colors.GREEN_400)    

    """     page.add(tblDivision)
    page.update() """


    columna = ft.Column([tblDivision])
    return columna        

if __name__ == "__main__":
    def main2(page: ft.Page):
        # Ancho de la ventana    
        page.window_width = 420
        # Largo de la ventana    
        page.window_height = 640
        # Título de la ventana
        page.title = "Sistema Posgrado"
        # Tema de la ventana
        page.theme_mode = "light"
        # Barra de título
        appBar = ft.AppBar(title=ft.Text("Nuevo Registro"), 
                        # Título centrado
                        center_title=True, 
                        # Color de fondo
                        bgcolor="green", 
                        # Color de texto
                        color="white")
        page.appbar = appBar
        page.add(main(page))
    ft.app(target=main)