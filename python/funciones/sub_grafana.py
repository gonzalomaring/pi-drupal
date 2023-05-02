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
    print()

#Función para mostrar información sobre el usuario conectado

def grafana_lsuser(grafana_api):
    users = grafana_api.users.find_user('admin')
    print("Nombre del usuario: ", users['login'])
    print("Fecha de creación: ", users['createdAt'])
    cadena = '¿Es admin?: ' + str(users['isGrafanaAdmin'])
    cadena = cadena.replace('True', 'Verdadero')
    print(cadena)
    print()


#Función para añadir un nuevo usuario
def grafana_adduser(grafana_api):
    nombre=input("Introduzca el nombre del usuario: ")
    email=input("Introduzca el email del usuario: ")
    login=input("Introduzca el nombre de login del usuario: ")
    password=input("Introduzca la contraseña del usuario: ")

    user = grafana_api.admin.create_user({"name": nombre, "email": email, "login": login, "password": password, "OrgId": 1})

#Función para mostrar información sobre un usuario
def grafana_userinfo(grafana_api):
    usuario=input("Introduzca el nombre del usuario: ")
    users = grafana_api.users.find_user(usuario)
    print("Nombre del usuario: ", users['login'])
    print("Fecha de creación: ", users['createdAt'])
    print()

#Función para mostrar dashboards
def grafana_dashboards(grafana_api):
    while True:
        print("Dashboards disponibles:")
        print("1. MySQL")
        print("2. Node Exporter")
        print("3. Salir")
        print()

        option = input("Seleccione una opción: ")
        print()

        if option == "1":
            uid="MQWgroiiz"
            dashboards = grafana_api.dashboard.get_dashboard(uid)
            print("Nombre del dashboard: ",dashboards['dashboard']['title'])
            print("Descripción del dashboard: ",dashboards['dashboard']['description'])
            print("UID del dashboard:", uid)
            print()
        elif option == "2":
            uid="rYdddlPWk"
            dashboards = grafana_api.dashboard.get_dashboard(uid)
            print("Nombre del dashboard: ",dashboards['dashboard']['title'])
            print("Descripción del dashboard: ",dashboards['dashboard']['description'])
            print("UID del dashboard:", uid)
        elif option == "3":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            print()
