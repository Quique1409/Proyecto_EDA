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

def inventario():
    #Aquí se muestran los distintos productos con sus unidades en existencia que se venden en la tienda
    print("\n|-----------------------------------------------------------------------------|")
    print("|      Perifericos       |      Componentes       | Videojuegos               |")
    print("|------------------------|------------------------|---------------------------|")
    print("|1.Teclado Logitech (6u) |7.Placa base (6u)       |13.Minecraft (15u)         |")
    print("|2.Teclado Razer (5u)    |8.Ryzen 7 7700X (8u)    |14.GTA VI (45u)            |")
    print("|3.Mouse Logitech (4u)   |9.Intel i7-13700KF (9u) |15.Sons of the Forest (4u) |")
    print("|4.Mouse Tempest (7u)    |10.RTX 4060 Ti (2u)     |16.F1 2023 (78u)           |")
    print("|5.Headset Logitech (3u) |11.RAM 16 GB dual (10)  |17.Fortnite (120u)         |")
    print("|6.Headset Corsair (6u)  |12.SSD 512 GB (12u)     |18.Valorant (496u)         |")
    print("|-----------------------------------------------------------------------------|")



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
