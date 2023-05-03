from funciones.sub_grafana import *
from funciones.sub_bbdd import *
# Función para mostrar el menú de opciones del programa
def show_menu():
    while True:
        print("Menú de opciones:")
        print("1. Test a la BBDD")
        print("2. Grafana API")
        print("3. Salir")
        print()


        option = input("Seleccione una opción: ")
        print()

        if option == "1":
            print()
            execute_queries()
        elif option == "2":
            grafana_menu()
        elif option == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            print()

#Función para mostrar menú de opciones de Grafana
def grafana_menu():
    #Importamos las librería de Grafana que usaremos
    from grafana_api.grafana_face import GrafanaFace
    grafana_api = GrafanaFace(auth=('admin', 'admin'), host='localhost', protocol='http', port='3000')
    #curl -H "Authorization: Bearer eyJrIjoiTHhWbVlUR0NGUVJpTlNiSnB5SWZGdjNVNkUzOHNTMFUiLCJuIjoiYWRtaW4iLCJpZCI6MX0=" http://localhost:3000/api/dashboards/home
    url = "http://localhost:3000/api/"
    #adminKEY
    key = "eyJrIjoiTHhWbVlUR0NGUVJpTlNiSnB5SWZGdjNVNkUzOHNTMFUiLCJuIjoiYWRtaW4iLCJpZCI6MX0="
    auth = ("admin", "admin")

    while True:
        print("Menú de opciones:")
        print("1. Ver Data Sources vinculados")
        print("2. Información sobre el usuario conectado")
        print("3. Añadir usuario")
        print("4. Información sobre usuario")
        print("5. Ver dashboards")
        print("6. Eliminar usuario ")
        print("7. Modificar contraseña usuario")
        print("8. Ver carpetas")
        print("9. Crear carpeta")
        print("10. Eliminar carpeta")
        print("11. Ver organizaciones")
        print("12. Salir")
        print()

        option = input("Seleccione una opción: ")
        print()

        if option == "1":
            grafana_data(url,key)
        elif option == "2":
            grafana_lsuser(grafana_api)
        elif option == "3":
            grafana_adduser(grafana_api)
        elif option == "4":
            grafana_userinfo(grafana_api)
        elif option == "5":
            grafana_dashboards(grafana_api)
        elif option == "6":
            grafana_deluser(grafana_api)
        elif option == "7":
            grafana_modpasswd(grafana_api)
        elif option == "8":
            grafana_folders(grafana_api)
        elif option == "9":
            grafana_addfolder(grafana_api)
        elif option == "10":
            grafana_delfolder(grafana_api)
        elif option == "11":
            grafana_orgs(grafana_api)
        elif option == "12":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            print()

