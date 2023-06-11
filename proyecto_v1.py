# proyecto_v1 final
# Tienda en linea de componentes para computadoras |puede cambiar la tematica | (Escoger nombre de empresa)

#Importaciones necesarias

#Definicion de funciones
def switch_case(case):
    #Funcion switch_case para opciones en el  menu
    if case == 1:
        #Aqui se encuentran los objetos que se venden junto a sus unidades
        print("Inventario")
    elif case == 2:
        #Aqui se va a mostra el inventario y la opcion de compra para el cliente
        print("Comprar")
    elif case == 3:
        #Esta opcion le muestra al cliente que a agregado a su lista de compra al final
        print("Ver lista de compra")
    elif case == 4:
        print("Ustede salio de la tienda, vuelva pronto!")
    else:
        print("Ingresa una opción valida :)")


#Interfaz de inicio para el cliente
while True:
    print("\n¡ Bienvenido a MARMOTAS online ! \n")
    print("Aquí podras encontrar variedad de productos para mejor tu set-up \n")
    print("\n|--------------------------|")
    print("|           MENU           |")
    print("|--------------------------|")
    print("|1. Inventario             |")
    print("|2. Comprar                |")
    print("|3. Ver lista de compra    |")
    print("|4. Salir del programa     |")
    print("|--------------------------|\n")

    opcion = int(input("\n\nEscoge la opción: "))
    switch_case(opcion)
    #SI se cumple esta condicion se para el bucle
    if opcion >= 1 and opcion <=4:
        break

print("#")
