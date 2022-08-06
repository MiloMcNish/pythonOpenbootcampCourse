import sqlite3
import getpass

def main():
    crear_usuario(4,"camilo","Mcnish50")

def main2():
    username = input('Nombre de usuario:')
    password = getpass.getpass("Contraseña: ")
    
    if verifica_credenciales(username, password):
        print('Login correcto')
    else:
        print('Login incorrecto')

def verifica_credenciales(username,password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    
    query = f"SELECT id FROM users WHERE username ='{username}' AND password ='{password}'"
    print('Query a ejecutar:', query)
    
    rows = cursor.execute(query)
    data = rows.fetchone()
    
    cursor.close()
    conn.close()

    if data == None:
        return False
    return True

def crear_usuario(identificador, usuario, password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    
    query = f"INSERT INTO users(id, username, password) VALUES({identificador},'{usuario}', '{password}')"
    print('Query a ejecutar:', query)
    
    rows = cursor.execute(query)
    print(type(rows))
    
    
    conn.commit()
    cursor.close()
    conn.close()

   
    
if __name__ == '__main__':
    main()

