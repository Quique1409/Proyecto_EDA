# proyecto_v1 final
# Tienda en linea de componentes para computadoras |puede cambiar la tematica | (Escoger nombre de empresa)
#Importaciones necesarias
from collections import deque

#Definicion de funciones
def switch_case_principal(case):
    #Funcion switch_case para opciones en el  menu
    if case == 1:
        #Aqui se encuentran los objetos que se venden junto a sus unidades
        print("Inventario")
        inventario_usuario()
    elif case == 2:
        gestionar_inventario()
    elif case == 3:
        #Opcion para que el usuario se salga del programa 
        print("Salir del programa")
    else:
        print("Ingresa una opción valida :)")


def inventario_usuario():
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
    print("|-----------------------------------------------------------------------------|\n")

def gestionar_inventario():
    inventario = [
        {'codigo': '1', 'nombre': 'Teclado Logitech', 'cantidad': 6},
        {'codigo': '2', 'nombre': 'Teclado Razer', 'cantidad': 5},
        {'codigo': '3', 'nombre': 'Mouse Logitech', 'cantidad': 4},
        {'codigo': '4', 'nombre': 'Mouse Tempest', 'cantidad': 7},
        {'codigo': '5', 'nombre': 'Headset Logitech', 'cantidad': 3},
        {'codigo': '6', 'nombre': 'Headset Corsair', 'cantidad': 6},
        {'codigo': '7', 'nombre': 'Placa base', 'cantidad': 6},
        {'codigo': '8', 'nombre': 'Ryzen 7 7700X', 'cantidad': 8},
        {'codigo': '9', 'nombre': 'Intel i7-13700KF', 'cantidad': 9},
        {'codigo': '10', 'nombre': 'RTX 4060 Ti', 'cantidad': 2},
        {'codigo': '11', 'nombre': 'RAM 16 GB dual', 'cantidad': 10},
        {'codigo': '12', 'nombre': 'SSD 512 GB', 'cantidad': 12},
        {'codigo': '13', 'nombre': 'Minecraft', 'cantidad': 15},
        {'codigo': '14', 'nombre': 'GTA VI', 'cantidad': 45},
        {'codigo': '15', 'nombre': 'Sons of the Forest', 'cantidad': 4},
        {'codigo': '16', 'nombre': 'F1 2023', 'cantidad': 78},
        {'codigo': '17', 'nombre': 'Fortnite', 'cantidad': 120},
        {'codigo': '18', 'nombre': 'Valorant', 'cantidad': 496},
    ]

    carrito = deque()

    while True:
        inventario_usuario()

        print("\n=== Carrito ===")
        if carrito:
            print("Código\tNombre\t\tCantidad")
            for producto in carrito:
                codigo = producto['codigo']
                nombre = producto['nombre']
                cantidad = producto['cantidad']
                print(f"{codigo}\t{nombre}\t\t{cantidad}")
        else:
            print("El carrito está vacío.")

        print("\n¿Qué deseas hacer?")
        print("1. Agregar producto al carrito")
        print("2. Eliminar producto del carrito")
        print("3. Realizar compra")
        print("4. Salir")

        opcion_menu = input("Ingresa el número de opción: ")

        if opcion_menu == '1':
            codigo = input("Ingresa el código del producto que deseas agregar: ")
            producto = next((p for p in inventario if p['codigo'] == codigo), None)
            if producto:
                cantidad = int(input("Ingresa la cantidad del producto que deseas agregar: "))
                if producto['cantidad'] >= cantidad:
                    producto_carrito = producto.copy()
                    producto_carrito['cantidad'] = cantidad
                    carrito.append(producto_carrito)
                    producto['cantidad'] -= cantidad
                    print("Producto agregado al carrito.")
                else:
                    print("No hay suficientes unidades disponibles de este producto.")
            else:
                print("El código de producto ingresado no existe en el inventario.")
        elif opcion_menu == '2':
            codigo = input("Ingresa el código del producto que deseas eliminar: ")
            producto = next((p for p in carrito if p['codigo'] == codigo), None)
            if producto:
                carrito.remove(producto)
                producto_inventario = next((p for p in inventario if p['codigo'] == codigo), None)
                if producto_inventario:
                    producto_inventario['cantidad'] += producto['cantidad']
                print("Producto eliminado del carrito.")
            else:
                print("El código de producto ingresado no existe en el carrito.")
        elif opcion_menu == '3':
            total = 0
            print("\n=== Detalles de compra ===")
            if carrito:
                print("Código\tNombre\t\tCantidad")
                for producto in carrito:
                    codigo = producto['codigo']
                    nombre = producto['nombre']
                    cantidad = producto['cantidad']
                    print(f"{codigo}\t{nombre}\t\t{cantidad}")
                    subtotal = cantidad
                    total += subtotal

                print(f"\nTotal de la compra: {total}")
                carrito.clear()
                print("¡Gracias por tu compra!")
            else:
                print("El carrito está vacío. No se puede realizar la compra.")
        elif opcion_menu == '4':
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


#Interfaz de inicio para el cliente
while True:
    print("\n¡ Bienvenido a MARMOTAS online ! \n")
    print("Aquí podras encontrar variedad de productos para mejor tu set-up \n")
    print("\n|--------------------------|")
    print("|           MENU           |")
    print("|--------------------------|")
    print("|1. Inventario             |")
    print("|2. Realizar pedido        |")
    print("|3. Salir                  |")
    print("|--------------------------|\n")

    opcion = int(input("\n\nEscoge la opción: "))
    switch_case_principal(opcion)
    #SI se cumple esta condicion se para el bucle
    if opcion >= 1 and opcion <=3:
        break
