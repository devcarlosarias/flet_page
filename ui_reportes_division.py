import flet as ft

def main(page: ft.Page):
    
    page.scroll = True
    
    lista_tabla = []
    divisiones = [
        {"nombre": "División Académica de Ciencias Agropecuarias", "id_division": "DACA", "ubicacion": "Km. 25. Carretera Villahermosa-Teapa, Teapa, Tabasco, México"},
        {"nombre": "División Académica de Ciencias Básicas", "id_division": "DACB", "ubicacion": "Carretera Cunduacán-Jalpa KM. 1 Col. La Esmeralda, Cunduacán, Tabasco, México"},
        {"nombre": "División Académica de Ciencias Biológicas", "id_division": "DACBiol", "ubicacion": "Carretera Villahermosa-Cárdenas Km. 0.5 S/N, Entronque a Bosques de Saloya, Villahermosa, Tabasco, México"},
        {"nombre": "División Académica de Ciencias Económico Administrativas", "id_division": "DACEA", "ubicacion": "Av. Universidad S/N Zona de la Cultura, Villahermosa, Tabasco, México"},
        {"nombre": "División Académica de Ciencias de la Salud", "id_division": "DACS", "ubicacion": "Av. Gregorio Méndez 2838-A Col. Tamulté, Villahermosa, Tabasco, México"},
        {"nombre": "División Académica de Ciencias Sociales y Humanidades", "id_division": "DACSyH", "ubicacion": "Prolongación de Avenida Paseo Usumacinta S/N Ranchería González Primera Sección, Villahermosa, Tabasco, México"},
        {"nombre": "División Académica de Ciencias y Tecnologías de la Información", "id_division": "DACyTI", "ubicacion": "Carretera Cunduacán-Jalpa KM. 1 Col. La Esmeralda, Cunduacán, Tabasco, México"},
        {"nombre": "División Académica de Educación y Artes", "id_division": "DAEA", "ubicacion": "Av. Universidad S/N Zona de la Cultura, Villahermosa, Tabasco"},
        {"nombre": "División Académica de Ingeniería y Arquitectura", "id_division": "DAIA", "ubicacion": "Carretera Cunduacán-Jalpa KM. 1 Col. La Esmeralda, Cunduacán, Tabasco, México"},
        {"nombre": "División Académica Multidisciplinaria de Comalcalco", "id_division": "DAMC", "ubicacion": "Ranchería Sur 4ta. sección, Comalcalco, Tabasco, México"},
        {"nombre": "División Académica Multidisciplinaria de Jalpa de Mendez", "id_division": "DAMJM", "ubicacion": "Carretera Estatal Libre Villahermosa-Comalcalco Km. 27+000 s/n Ranchería Ribera Alta, Jalpa de Méndez, Tabasco, México"},
        {"nombre": "División Académica Multidisciplinaria de los Rios", "id_division": "DAMR", "ubicacion": "Km. 1. Carretera Tenosique-Estapilla, Tenosique, Tabasco, México"}
    ]

    for division in divisiones:
        celda1 = ft.DataCell(ft.Text(division["id_division"]))
        celda2 = ft.DataCell(ft.Text(division["nombre"]))
        celda3 = ft.DataCell(ft.Text(division["ubicacion"]))
        fila = ft.DataRow(cells=[celda1, celda2, celda3])
        lista_tabla.append(fila)

    encabezado = [ft.DataColumn(ft.Text("ID")), ft.DataColumn(ft.Text("Nombre")), ft.DataColumn(ft.Text("Ubicación"))]

    tblDivisiones = ft.DataTable(columns=encabezado, rows=lista_tabla, heading_row_color="grey200", border=ft.border.all(2,"grey200"))

    columna = ft.Column([tblDivisiones], scroll=True)
    return columna    

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
