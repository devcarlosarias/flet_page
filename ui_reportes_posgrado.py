

import flet as ft
from modelo import Posgrado
from modelo import Division
from modelo import Responsable

def main(page: ft.Page):

    page.window_width = 840
    page.window_height = 640
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Posgrados Activos"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
    page.scroll=True

    # Traer los posgrados de la base de datos
    lista_tabla = []
    posgrado = Posgrado.select()
    for p in posgrado:
        celda1 = ft.DataCell(ft.Text(p.nombre))
        celda2 = ft.DataCell(ft.Text(p.id_posgrado))
        celda3 = ft.DataCell(ft.Text(p.tipo))
        celda4 = ft.DataCell(ft.Text(p.activo))
        celda5 = ft.DataCell(ft.Text(p.snp))
        celda6 = ft.DataCell(ft.Text(p.orientacion))
        celda7 = ft.DataCell(ft.Text(p.modalidad))
        celda8 = ft.DataCell(ft.Text(p.id_division))
        #celda9 = ft.DataCell(ft.Text(p.id_responsable))



        fila = ft.DataRow(cells=[celda1,celda2,celda3,celda4,celda5,celda6,celda7,celda8])
        lista_tabla.append(fila)
    
    encabezado = [ft.DataColumn(ft.Text("Nombre")), ft.DataColumn(ft.Text("ID"), numeric=True), ft.DataColumn(ft.Text("Tipo")), ft.DataColumn(ft.Text("Activo")), ft.DataColumn(ft.Text("SNP")), ft.DataColumn(ft.Text("Orientacion")), ft.DataColumn(ft.Text("Modalidad")), ft.DataColumn(ft.Text("División"))]

    tblPosgrado =ft.DataTable(columns=encabezado,rows=lista_tabla, heading_row_color="grey200", border=ft.border.all(2,"grey200"))


    """     page.add(tblPosgrado)
    page.update()
     """
    columna = ft.Column([tblPosgrado])
    return columna    


if __name__ == "__main__":
    ft.app(target=main)