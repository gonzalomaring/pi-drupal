from funciones.menu import *
from funciones.sub_bbdd import *
from urllib.parse import urlparse
import mysql.connector,time,requests,json



#Función para mostrar información sobre el usuario conectado

def grafana_data(url,key):
    #Especificamos la URL correcta para el endpoint de la API
    datasources_url = url + "datasources"
    #Especificamos los headers para la autenticación
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json"
    }
    #Obtenemos la lista de datasources
    response = requests.get(datasources_url, headers=headers)
    datasources = json.loads(response.content)
    print("Nombres y URLs de los datasources:")
    for ds in datasources:
        parsed_url = urlparse(ds['url'])
        #Si el hostname no es localhost, reemplazamos el hostname por localhost
        if parsed_url.hostname != 'localhost':
            url = ds['url'].replace(parsed_url.hostname, 'localhost')
        else:
            url = ds['url']
        print(f"{ds['name']}: {url}")

#Función para mostrar información sobre el usuario conectado


def grafana_lsuser(url, key):
    # Realiza la solicitud GET para obtener información del usuario
    users_url = url + "user"
    # Especificamos los headers para la autenticación
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json"
    }
    response = requests.get(users_url, headers=headers)
    if response.status_code == 200:
        user_info = response.json()
        print(f"Nombre de usuario: {user_info['login']}")
        print(f"Email: {user_info['email']}")
    else:
        print("Error al obtener información del usuario:", response.json())

def grafana_adduser(url, key):
    # Realiza la solicitud POST para crear un nuevo usuario
    users_url = url + "admin/users"
    # Especificamos los headers para la autenticación
    headers = {
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json"
    }
    # Solicitamos los datos del nuevo usuario
    username = input("Ingrese el nombre de usuario: ")
    email = input("Ingrese el email: ")
    password = input("Ingrese la contraseña: ")
    # Creamos el payload
    payload = {
        "name": username,
        "email": email,
        "login": username,
        "password": password
    }
    response = requests.post(users_url, headers=headers, json=payload)
    if response.status_code == 200:
        print("Usuario creado con éxito")
    else:
        print("Error al crear el usuario:", response.json())