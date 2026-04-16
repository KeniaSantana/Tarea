import btrypt
from .databaseModel import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self,usuario_data):
        #Encriptar contraseña
        salt = btrypt.gensalt()
        hashed_password = btrypt.hashpw(usuario_data.password.encode('utf-8'), salt)
        conn=self.db.get_connection()
        cursor=conn.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (username, email, password) VALUES (%s, %s, %s)",
                        (usuario_data.nombre, usuario_data.email, hashed_password.decode('utf-8')))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def validar_login(self, email, password):
        conn=self.db.get_connection()
        cursor=conn.cursor(directory=True)
        cursor.execute("SELECT password FROM usuarios WHERE email = %s", (email,))
        user=cursor.fetchone()
        conn.close()
        if user and btrypt.checkpw(password.encode('utf-8'), user[password].encode('utf-8')):
            return user
        return home