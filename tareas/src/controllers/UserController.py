from src.models.UserModel import UsuarioModel
from src.models.shemasModel
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.db = UsuarioModel()
        
    def registrar_usuario(self,nombre,email,password):
        try:
            #Validar datos con el Schema
            nuevo_usuario=UsuarioShema(nombre=nombre,email=email,password=password)
            success=self.model.resgistrar(nuevo_usuario)
            return success,"Usuario creado correctamente"
        except ValidationError as e:
            #Retorna el primer error de validacion encontrado
            return false,e.errors()[]['msg']
            
            
    