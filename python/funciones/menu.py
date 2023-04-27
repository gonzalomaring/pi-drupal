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
    #curl -H "Authorization: Bearer eyJrIjoiTHhWbVlUR0NGUVJpTlNiSnB5SWZGdjNVNkUzOHNTMFUiLCJuIjoiYWRtaW4iLCJpZCI6MX0=" http://localhost:3000/api/dashboards/home
    url = "http://localhost:3000/api/"
    key = "eyJrIjoiTHhWbVlUR0NGUVJpTlNiSnB5SWZGdjNVNkUzOHNTMFUiLCJuIjoiYWRtaW4iLCJpZCI6MX0="
    auth = ("admin", "admin")

    while True:
        print("Menú de opciones:")
        print("1. Ver Data Sources vinculados")
        print("2. Información sobre el usuario conectado")
        print("3. Añadir usuario")
        print("4. Eliminar usuario")
        print("5. Ver dashboards")
        print("6. Ver da")
        print("7. Salir")
        print()

        option = input("Seleccione una opción: ")
        print()

        if option == "1":
            grafana_data(url,key)
        elif option == "2":
            grafana_lsuser(url,key)
        elif option == "3":
            grafana_adduser(url,key)
        elif option == "4":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")
            print()

