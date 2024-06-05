import os
import msvcrt
import csv
user=["id", "nombre"]
clases=[]
reservas=[]
id=100
while True:
    print("<<Press any key>>")
    msvcrt.getch()
    os.system("cls")
    print("""Sistema de reservas 'Gimnasio FitLife'
        ───────────────────────────────────────────
    1.- Registrar un nuevo usuario.
    2.- Reservar una clase.
    3.- Consultar clases disponibles.
    4.- Consultar reservas de un usuario.
    0.- Salir del programa""")
    opcion=input("Seleccione : ")
    if opcion=="1":
        print("Registrar nuevo usuario")
        nombre=input("Ingrese su nombre: ").capitalize()
        if len(nombre)>=3:
                id=max(id)+1
                user.append(id,user[nombre])
                print(user)
        else:
            print("\033[31mERROR, nombre no válido\033[0m")
    elif opcion=="2":
        print("Reservar una clase")
    elif opcion=="3":
        print("Consultar clases disponibles")
    elif opcion=="4":
        print("Consultar reservas de un usuario")
    elif opcion=="0":
        print("Gracias por usar el programa 🦎")
        break
    else:
        print("\033[31mERROR, opción no válida\033[0m")