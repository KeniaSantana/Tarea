import flet as ft 
from src.controllers.UserController import AuthController
from src.controllers.TareaController import TareaController
from src.views.loginView import loginview
from src.views.dashboard import DashboardView

def main(page:ft.page):
    #Instanciamos los controles una sola vez
    auth_ctrl=AuthController
    task_ctrl=TareaController
    
    def route_chance(route):
        page.view.clear()
        if page.route=="/":
            page.views.append(loginview(page,auth_ctrl))
        elif page.route=="/deshboard":
            page.view.append(DashboardView(page,task_ctrl))
            #Agregas aqui el registro_view de la misma forma
            page.update()
            
        page.on_route_chance=route_chance
        page.go("/")
        
if __name__=="__main__":
    ft.run(main)
