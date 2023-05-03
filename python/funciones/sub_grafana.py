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
    print()
    try:
        user = grafana_api.admin.create_user({"name": nombre, "email": email, "login": login, "password": password, "OrgId": 1})
        print("Usuario creado correctamente.")
        print()
    except Exception as e:
        print("Error al crear el usuario: ", e)
        print()
 
#Función para mostrar información sobre un usuario
def grafana_userinfo(grafana_api):
    try:
        usuario=input("Introduzca el nombre del usuario: ")
        users = grafana_api.users.find_user(usuario)
        print("Nombre del usuario: ", users['login'])
        print("Fecha de creación: ", users['createdAt'])
        print("ID del usuario: ", users['id'])
        print()
    except Exception as e:
        print("El usuario no existe")
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
            try:
                uid="MQWgroiiz"
                dashboards = grafana_api.dashboard.get_dashboard(uid)
                print("Nombre del dashboard: ",dashboards['dashboard']['title'])
                print("Descripción del dashboard: ",dashboards['dashboard']['description'])
                print("UID del dashboard:", uid)
                print("Fecha de creación: ",dashboards['meta']['created'])
                print("¿Se puede editar el dashboard?,",dashboards['meta']['canEdit'])
                print("¿Cada cuanto se refresca el panel?",dashboards['dashboard']['refresh'])
                print("Fichero JSON del dashboard?",dashboards['meta']['provisionedExternalId'])
                print()
            except: 
                print("No se ha podido obtener información sobre el dashboard")
                print()
        elif option == "2":
            try: 
                uid="rYdddlPWk"
                dashboards = grafana_api.dashboard.get_dashboard(uid)
                print("Nombre del dashboard: ",dashboards['dashboard']['title'])
                print("UID del dashboard:", dashboards['dashboard']['uid'])
                print("Fecha de creación: ",dashboards['meta']['created'])
                print("¿Se puede editar el dashboard?,",dashboards['meta']['canEdit'])
                print("Fichero JSON del dashboard:", dashboards['meta']['provisionedExternalId'])
                print()
            except:
                print("No se ha podido obtener información sobre el dashboard")
                print()
        elif option == "3":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            print()

#Función para eliminar un usuario
def grafana_deluser(grafana_api):
    usuario=input("Introduzca el nombre del usuario: ")
    try:
        users = grafana_api.users.find_user(usuario)
        id=users['id']
        dec=input("¿Quieres borrar el usuario? (S/N): ")
        if dec=="S" or dec=="s":
            try:
                grafana_api.admin.delete_user(id)
                print("Usuario eliminado correctamente.")
                print()
            except Exception as e:
                print("Error al eliminar el usuario ")
                print()
    except Exception as e:
        print("El usuario no existe ")
        print()

#Función para modificar la contraseña de un usuario
def grafana_modpasswd(grafana_api):
    usuario=input("Introduzca el nombre del usuario: ")
    try:
        users = grafana_api.users.find_user(usuario)
        id=users['id']
        password=input("Introduzca la nueva contraseña: ")
        dec=input("¿Quieres modificar la contraseña? (S/N): ")
        if dec=="S" or dec=="s":
            try:
                grafana_api.admin.change_user_password(id, password)
                print("Contraseña modificada correctamente.")
                print()
            except Exception as e:
                print("Error al modificar la contraseña ")
                print()
    except Exception as e:
        print("El usuario no existe ")
        print()

#Función para ver las carpetas disponibles
def grafana_folders(grafana_api):
    try:
        folders = grafana_api.folder.get_all_folders()
        print("Carpetas disponibles:")
        for folder in folders:
            print("Nombre de la carpeta: ",folder['title'])
            print("UID de la carpeta: ",folder['uid'])
            print("----------------------------------")
        print()
    except Exception as e:
        print("Error al obtener las carpetas: ")
        print()

#Función para crear una nueva carpeta
def grafana_addfolder(grafana_api):
    nombre=input("Introduzca el nombre de la carpeta: ")
    try:
        folder = grafana_api.folder.create_folder(nombre)
        print("Carpeta creada correctamente.")
        print()
    except Exception as e:
        print("Error al crear la carpeta: ")
        print()

#Función para eliminar una carpeta. Aunque sea elimine da error, por lo que el except es el mensaje que se vera por pantalla
def grafana_delfolder(grafana_api):
    nombre=input("Introduzca el nombre de la carpeta: ")
    folders = grafana_api.folder.get_all_folders()
    for folder in folders:
        try:
            if folder['title']==nombre:
                uid=folder['uid']
                dec=input("¿Quieres borrar la carpeta? (S/N): ")
                if dec=="S" or dec=="s":
                    grafana_api.folder.delete_folder(uid)
                    print("Carpeta eliminada correctamente.")
                    print()
        except Exception as e:
            print("Carpeta eliminada correctamente.")
            print()

#Función para ver las organizaciones disponibles
def grafana_orgs(grafana_api):
    try:
        orgs = grafana_api.organization.get_current_organization()
        print("Nombre de la organización: ",orgs['name'])
        print("ID de la organización: ",orgs['id'])
        print()
    except Exception as e:
        print("Error al obtener las organizaciones")
        print()