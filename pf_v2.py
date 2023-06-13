from queue import Queue

# Inventario de frutas
inventario = {
    'manzana': 5,
    'plátano': 10,
    'naranja': 3,
    'uva': 8
}

# Cola de pedidos
cola_pedidos = Queue()

# Lista de pedidos validados
lista_pedidos = []

# Variable para almacenar la complejidad temporal
complejidad_temporal = 0

def imprimir_menu():
    print("\n----- Menú de Frutas -----")
    for i, (fruta, cantidad) in enumerate(inventario.items(), start=1):
        print(f"{i}. {fruta}: {cantidad} unidades")
    print("--------------------------")

def agregar_pedido():
    imprimir_menu()
    opcion = int(input("Seleccione el número de la fruta que desea pedir: "))
    
    frutas = list(inventario.keys())
    if 1 <= opcion <= len(frutas):
        fruta = frutas[opcion - 1]
        cantidad = int(input("Ingrese la cantidad que desea: "))
        pedido = (fruta, cantidad)
        cola_pedidos.put(pedido)
        print("Pedido agregado a la cola.")
    else:
        print("Opción inválida. Intente de nuevo.")

def validar_pedido_recursivo():
    global complejidad_temporal

    if cola_pedidos.empty():
        print("No hay pedidos en espera.")
        return
    
    pedido = cola_pedidos.get()
    fruta, cantidad = pedido

    if fruta in inventario and cantidad <= inventario[fruta]:
        print("Pedido válido.")
        lista_pedidos.append(pedido)
        inventario[fruta] -= cantidad
        complejidad_temporal += cantidad  # Se incrementa la complejidad temporal en función de la cantidad de productos
    else:
        print("No existe o no hay suficientes unidades disponibles.")
    
    validar_pedido_recursivo()

def validar_pedido_fuerza_bruta():
    global complejidad_temporal

    if cola_pedidos.empty():
        print("No hay pedidos en espera.")
        return
    
    while not cola_pedidos.empty():
        pedido = cola_pedidos.get()
        fruta, cantidad = pedido
        productos_validos = True

        if fruta not in inventario or cantidad > inventario[fruta]:
            productos_validos = False

        if productos_validos:
            for _ in range(cantidad):
                inventario[fruta] -= 1
                complejidad_temporal += 1
            lista_pedidos.append(pedido)
            print("Pedido válido.")
        else:
            print("No existe o no hay suficientes unidades disponibles.")

def imprimir_lista():
    print("----- Lista de Pedidos -----")
    for fruta, cantidad in lista_pedidos:
        print(f"{fruta}: {cantidad}")
    print("-----------------------------")

# Ejecución principal
while True:
    print("\n----- Tienda Online -----")
    print("1. Ver menú de frutas y cantidad de unidades")
    print("2. Agregar pedido")
    print("3. Procesar pedidos en espera")
    print("4. Imprimir lista de pedidos")
    print("5. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        imprimir_menu()
    elif opcion == 2:
        agregar_pedido()
    elif opcion == 3:
        print("\n----- Opciones de Procesamiento -----")
        print("1. Validar pedidos por recursividad")
        print("2. Validar pedidos por fuerza bruta")
        opcion_procesamiento = int(input("Seleccione una opción de procesamiento: "))
        if opcion_procesamiento == 1:
            validar_pedido_recursivo()
            print("Complejidad temporal del procesamiento de pedidos:", complejidad_temporal)
        elif opcion_procesamiento == 2:
            validar_pedido_fuerza_bruta()
            print("Complejidad temporal del procesamiento de pedidos:", complejidad_temporal)
        else:
            print("Opción inválida. Intente de nuevo.")
    elif opcion == 4:
        imprimir_lista()
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Intente de nuevo.")

print("Gracias por utilizar la tienda online :)\nSé feliz como una lombriz ♫ ♫")
