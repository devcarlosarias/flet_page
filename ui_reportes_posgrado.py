import flet as ft

def main(page: ft.Page):

    page.scroll = True
    
    lista_tabla = []
    posgrados = [
        {"nombre": "Maestría en Seguridad Alimentaria", "id_posgrado": 1, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Profesional", "modalidad": "No escolarizado", "id_division": "DACA"},
        {"nombre": "Maestría en Agronegocios", "id_posgrado": 2, "tipo": "Maestría", "activo": "Sí", "snp": "No", "orientacion": "Profesional", "modalidad": "Escolarizado", "id_division": "DACA"},
        {"nombre": "Maestría en Producción Animal Tropical", "id_posgrado": 3, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Profesional", "modalidad": "Escolarizado", "id_division": "DACA"},
        {"nombre": "Maestría en Ciencias Agroalimentarias", "id_posgrado": 4, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACA"},
        {"nombre": "Doctorado en Ciencias Agropecuarias", "id_posgrado": 5, "tipo": "Doctorado", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACA"},
        {"nombre": "Maestría en Ciencias con orientación en Materiales y Nanociencias y Química Orgánica", "id_posgrado": 6, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Maestría en Ciencias Matemáticas", "id_posgrado": 7, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Doctorado en Ciencias con Orientación en: Materiales y Nanociencias y Química Orgánica", "id_posgrado": 8, "tipo": "Doctorado", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Doctorado en Ciencias Matemáticas", "id_posgrado": 9, "tipo": "Doctorado", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Maestría en Ciencias en Química Aplicada", "id_posgrado": 10, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Especialidad en Ingeniería de Sistemas de Aguas Profundas (OffShore)", "id_posgrado": 11, "tipo": "Especialidad", "activo": "Sí", "snp": "Sí", "orientacion": "Profesional", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Doctorado en Ciencias en Química Aplicada", "id_posgrado": 12, "tipo": "Doctorado", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Maestría en Ciencias en Matemáticas Aplicadas", "id_posgrado": 13, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACB"},
        {"nombre": "Maestría en Ingeniería y Tecnología y Gestión Ambiental", "id_posgrado": 14, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Profesional", "modalidad": "Escolarizado", "id_division": "DACBiol"},
        {"nombre": "Maestría en Ciencias Ambientales", "id_posgrado": 15, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACBiol"},
        {"nombre": "Especialidad en Controversias Socioambientales en Hidrocarburos", "id_posgrado": 16, "tipo": "Especialidad", "activo": "Sí", "snp": "No", "orientacion": "Profesional", "modalidad": "Escolarizado", "id_division": "DACBiol"},
        {"nombre": "Doctorado en Ciencias en Ecología y Manejo de Sistemas Tropicales", "id_posgrado": 17, "tipo": "Doctorado", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACBiol"},
        {"nombre": "Maestría en Ciencias en Gestión del Desarrollo Regional", "id_posgrado": 18, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACEA"},
        {"nombre": "Doctorado en Administración Educativa", "id_posgrado": 19, "tipo": "Doctorado", "activo": "Sí", "snp": "Sí", "orientacion": "Investigación", "modalidad": "Escolarizado", "id_division": "DACEA"},
        {"nombre": "Maestría en Gerencia Pública y Gobierno", "id_posgrado": 20, "tipo": "Maestría", "activo": "Sí", "snp": "Sí", "orientacion": "Profesional", "modalidad": "Escolarizado", "id_division": "DACEA"},
    ]

    for p in posgrados:
        celda1 = ft.DataCell(ft.Text(p["nombre"]))
        celda2 = ft.DataCell(ft.Text(str(p["id_posgrado"])))
        celda3 = ft.DataCell(ft.Text(p["tipo"]))
        celda4 = ft.DataCell(ft.Text(p["activo"]))
        celda5 = ft.DataCell(ft.Text(p["snp"]))
        celda6 = ft.DataCell(ft.Text(p["orientacion"]))
        celda7 = ft.DataCell(ft.Text(p["modalidad"]))
        celda8 = ft.DataCell(ft.Text(p["id_division"]))

        fila = ft.DataRow(cells=[celda1, celda2, celda3, celda4, celda5, celda6, celda7, celda8])
        lista_tabla.append(fila)
    
    encabezado = [
        ft.DataColumn(ft.Text("Nombre")), 
        ft.DataColumn(ft.Text("ID"), numeric=True), 
        ft.DataColumn(ft.Text("Tipo")), 
        ft.DataColumn(ft.Text("Activo")), 
        ft.DataColumn(ft.Text("SNP")), 
        ft.DataColumn(ft.Text("Orientación")), 
        ft.DataColumn(ft.Text("Modalidad")), 
        ft.DataColumn(ft.Text("División"))
    ]

    tblPosgrado = ft.DataTable(columns=encabezado, rows=lista_tabla, heading_row_color="grey200", border=ft.border.all(2, "grey200"))

    columna = ft.Column([tblPosgrado], scroll=True)
    return columna    

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
