import flet as ft
from datetime import date

hoy = date.today()

def main(page: ft.Page):

    def cerrar_ventana(e:ft.ControlEvent):
        page.window_close()

    def validar_campos(e:ft.ControlEvent):
        error = None
        if txtPosgrado.value.strip() == "":        
            error = "Error: Introduce el nombre del posgrado"
        elif drpTipo.value is None:
            error = "Error: Seleccione el tipo del posgrado"
        elif drpOrientacion.value is None:
            error = "Error: Seleccione la orientacion del posgrado"
        elif drpModalidad.value is None:
            error = "Error: Seleccione la modalidad del posgrado"
        elif drpDivision.value is None:
            error = "Error: Selecciona la división del posgrado"
        elif drpResponsable.value is None:
            error = "Error: Selecciona el responsable del posgrado"
        else:
            guardar_datos()    
        
        if error is not None:
            snackbar = ft.SnackBar(ft.Text(error, color="black"), show_close_icon=True, bgcolor="amber")
            page.snack_bar = snackbar
            snackbar.open = True
            page.update()
                   
    def guardar_datos():


        # Mostrar snackbar de OK
        snackbar = ft.SnackBar(ft.Text("Datos guardados correctamente"), show_close_icon=True, bgcolor="green")
        page.snack_bar = snackbar
        snackbar.open = True
        page.update()
 

        # Guardar datos del posgrado en la base de datos
        try:
            p = Posgrado.create(nombre=txtPosgrado.value.strip(),
                                tipo=drpTipo.value,
                                orientacion=drpOrientacion.value,
                                #orientacion=radOrientacion.value,
                                modalidad=drpModalidad.value,

                                id_division=drpDivision.value,
                                id_responsable=drpResponsable.value,
                                snp=chkSNP.value)
                                
            print("Datos Guardados Exitosamente")
        
        except pw.IntegrityError as error:
            print("Error SQLite", error) 



    page.window_width = 420
    page.window_height = 640
    page.title = "Sistema Posgrado"
    page.theme_mode = "light"
    appBar = ft.AppBar(title=ft.Text("Nuevo Posgrado"), 
                       center_title=True, 
                       bgcolor="green", 
                       color="white")
    page.appbar = appBar
    
    txtPosgrado = ft.TextField(label="Nombre del posgrado")
    
    tipo = [ft.dropdown.Option("Especialidad"),
                ft.dropdown.Option("Maestría"),
                ft.dropdown.Option("Doctorado")]
    drpTipo = ft.Dropdown(label="Seleccione su tipo", options=tipo)    
    
    orientacion = [ft.dropdown.Option("Profesional"),
                ft.dropdown.Option("Investigación")]
    drpOrientacion = ft.Dropdown(label="Seleccione su orientación", options=orientacion)    


    modalidad = [ft.dropdown.Option("Escolarizado"),
                ft.dropdown.Option("No Escolarizado")]
    drpModalidad = ft.Dropdown(label="Seleccione su modalidad", options=modalidad)
    
    division = [ft.dropdown.Option("DACyTI"),
                ft.dropdown.Option("DAEA")]
    drpDivision = ft.Dropdown(label="Seleccione su división", options=division)
    
    drpResponsable = ft.Dropdown(label="Seleccione su responsable", options=None)
        
    chkSNP = ft.Checkbox()
    textSNP = ft.Text("Pertenece al SNP", size=16,)
    filaSNP = ft.Row([textSNP, chkSNP], alignment="center")

    btnGuardar = ft.ElevatedButton("Guardar", icon="check_circle", bgcolor="white", color="black", icon_color="green400", on_click=validar_campos)
    btnCancelar = ft.ElevatedButton("Cancelar", 
                                bgcolor="white",  
                                color="black",
                                icon="cancel", 
                                icon_color="red400",
                                on_click=cerrar_ventana)
    
    rowBotones = ft.Row([btnGuardar, btnCancelar], alignment="center")
    
    columna = ft.Column([txtPosgrado,drpTipo,drpOrientacion,drpModalidad,drpDivision,drpResponsable,filaSNP,rowBotones])
    return columna

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
