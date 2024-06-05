import flet as ft

def main(page: ft.Page):
    
    page.scroll = True
    
    lista_tabla = []
    responsables = [
        {"ID": "MWO02270", "nombre": "Miguel Antonio Wister Ovando", "grado": "Doctor", "correo": "miguel.wister@ujat.mx", "division": "DACyTI"},
        {"ID": "EGA03425", "nombre": "Eddy Arquímedes García Alcocer", "grado": "Doctor", "correo": "arquimedes.garcia@ujat.mx", "division": "DACyTI"},
        {"ID": "EMM03483", "nombre": "Erika Yunuen Morales Mateos", "grado": "Doctora", "correo": "erika.morales@ujat.mx", "division": "DACyTI"},
        {"ID": "OCB03420", "nombre": "Oscar Alberto Chávez Bosquez", "grado": "Doctor", "correo": "oscar.chavez@ujat.mx", "division": "DACyTI"},
        {"ID": "PPC01592", "nombre": "Pablo Payró Campos", "grado": "Doctor", "correo": "pablo.payro@ujat.mx", "division": "DACyTI"}
    ]

    for responsable in responsables:
        celda1 = ft.DataCell(ft.Text(responsable["ID"]))
        celda2 = ft.DataCell(ft.Text(responsable["nombre"]))
        celda3 = ft.DataCell(ft.Text(responsable["grado"]))
        celda4 = ft.DataCell(ft.Text(responsable["correo"]))
        celda5 = ft.DataCell(ft.Text(responsable["division"]))
        fila = ft.DataRow(cells=[celda1, celda2, celda3, celda4, celda5])
        lista_tabla.append(fila)

    encabezado = [ft.DataColumn(ft.Text("ID")), ft.DataColumn(ft.Text("Nombre")), ft.DataColumn(ft.Text("Grado")), ft.DataColumn(ft.Text("Correo")), ft.DataColumn(ft.Text("División"))]

    tblResponsable = ft.DataTable(columns=encabezado, rows=lista_tabla, heading_row_color="grey200", border=ft.border.all(2,"grey200"))

    columna = ft.Column([tblResponsable])
    return columna    

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
