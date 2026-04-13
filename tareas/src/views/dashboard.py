import flet as ft 

def DashboardView(page,tarea_controller):
    user=page.session.get("user")
    lista_tarea=
    ft.Column(scroll=ft.ScrollMode.ALWAYS,expand=True)
    
    def refresh():
        lista_tareas.controls.clear()
        for t in
        tarea_controller.obtener_lista(user['id_usuario']):
            
        lista_tareas.controls.append(ft.Card(
            content=ft.Container(
                content=ft.LostTile(
                    
                )
            )
        ))