


#No mover ni cambiar nada de este archivo es nuestra copia de seguridad



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

def imprimir_menu():
    print("\n----- Menú de Frutas -----")
    for fruta, cantidad in inventario.items():
        print(f"{fruta}: {cantidad} unidades")
    print("--------------------------")

def agregar_pedido():
    fruta = input("Ingrese la fruta que desea pedir: ")
    cantidad = int(input("Ingrese la cantidad que desea: "))
    pedido = (fruta, cantidad)
    cola_pedidos.put(pedido)
    print("Pedido agregado a la cola.")


### validar pedido por recursividad 

def validar_pedido():
    if cola_pedidos.empty():
        print("No hay pedidos en espera.")
        return
    
    pedido = cola_pedidos.get()
    fruta, cantidad = pedido

    if fruta in inventario and cantidad <= inventario[fruta]:
        print("Pedido válido.")
        lista_pedidos.append(pedido)
    else:
        print("No existe o no hay suficientes unidades disponibles.")
    
    validar_pedido()  # Llamada recursiva para procesar el siguiente pedido en la cola

def imprimir_lista():
    print("----- Lista de Pedidos -----")
    for pedido in lista_pedidos:
        fruta, cantidad = pedido
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
        validar_pedido()
    elif opcion == 4:
        imprimir_lista()
    elif opcion == 5:
        break
    else:
        print("Opción inválida. Intente de nuevo.")

print("Gracias por utilizar la tienda online:)\nSé feliz como una lombriz ♫ ♫")
