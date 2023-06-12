from collections import deque

def switch_case_principal(case, inventario):
    if case == 1:
        print("Inventario")
        imprimir_inventario(inventario)
    elif case == 2:
        carrito = deque()
        while True:
            imprimir_inventario(inventario)
            mostrar_carrito(carrito)
            print("\n¿Qué deseas hacer?")
            print("1. Agregar producto al carrito")
            print("2. Eliminar producto del carrito")
            print("3. Realizar compra")
            print("4. Salir")
            opcion = input("Ingresa el número de opción: ")

            if opcion == '1':
                agregar_producto(carrito, inventario)
            elif opcion == '2':
                eliminar_producto(carrito, inventario)
            elif opcion == '3':
                realizar_compra(carrito)
            elif opcion == '4':
                break
            else:
                print("Opción inválida. Por favor, selecciona una opción válida.")

    elif case == 3:
        print("Salir del programa")
    else:
        print("Ingresa una opción válida :)")

def imprimir_inventario(inventario):
    print("\n|-----------------------------------------------------------------------------|")
    print("|      Periféricos       |      Componentes       |     Videojuegos            |")
    print("|------------------------|------------------------|---------------------------|")
    for producto in inventario:
        codigo = producto['codigo']
        nombre = producto['nombre']
        cantidad = producto['cantidad']
        print(f"|{codigo}. {nombre:22} |{cantidad:^23}|")
    print("|-----------------------------------------------------------------------------|")

def mostrar_carrito(carrito):
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

def agregar_producto(carrito, inventario):
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

def eliminar_producto(carrito, inventario):
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

def realizar_compra(carrito):
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
    return inventario

#Interfaz de inicio para el cliente
while True:
    print("\n¡Bienvenido a MARMOTAS online!\n")
    print("Aquí podrás encontrar variedad de productos para mejorar tu set-up.\n")
    print("|--------------------------|")
    print("|           MENU           |")
    print("|--------------------------|")
    print("|1. Inventario             |")
    print("|2. Realizar pedido        |")
    print("|3. Salir                  |")
    print("|--------------------------|\n")
    opcion = int(input("\nEscoge la opción: "))
    inventario = gestionar_inventario()
    switch_case_principal(opcion, inventario)
    if opcion >= 1 and opcion <= 3:
        break
