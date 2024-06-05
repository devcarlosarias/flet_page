import flet as ft
from simpledt import SQLDataTable
from simpledt import DataFrame

def main(page: ft.Page):

    page.window_width = 980
    page.window_height = 640
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Posgrados Activos"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
    page.scroll=True

    #sql = SQLDataTable('sqlite', 'posgrado.sqlite3', 'responsable') # Serialize everything from `users` table
    
    sql = SQLDataTable('sqlite', 'posgrado.sqlite3',  statement="SELECT id_responsable as Clave, nombre as Nombre, grado as Grado, correo as Correo, id_division as División FROM responsable") # Write a custom query statement
    tblReponsable = sql.datatable

    tblReponsable.bgcolor = ft.colors.GREEN_200
    tblReponsable.border = ft.border.all(2, ft.colors.GREEN_400)     
    
    """     page.add(tblReponsable)
    page.update() """

    columna = ft.Column([tblReponsable])
    return columna    

if __name__ == "__main__":
    ft.app(target=main)