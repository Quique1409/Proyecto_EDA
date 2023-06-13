
def procesar_pedido(pedido):
    if not pedido_valido(pedido):
        print("Pedido no válido")
        return

    if len(pedido) == 0:
        print("Pedido procesado")
        return

    producto_actual = pedido[0]
    procesar_producto(producto_actual)
    complejidad_producto_actual = calcular_complejidad(producto_actual)

    procesar_pedido(pedido[1:])
    complejidad_total = complejidad_producto_actual + calcular_complejidad(pedido[1:])
    print("La complejidad temporal del pedido es:", complejidad_total)




def recursive_function(n):
    if n <= 0:
        return
    else:
        # Realiza alguna operación
        print("Realizando una operación")

        # Llamada recursiva con un subproblema más pequeño
        recursive_function(n - 1)

# Calcular la complejidad del algoritmo recursivo
def calculate_complexity(n):
    # Reiniciar el contador de operaciones
    global operation_count
    operation_count = 0

    # Ejecutar la función recursiva
    recursive_function(n)

    # Imprimir el número total de operaciones
    print("Número total de operaciones:", operation_count)

# Variable global para contar las operaciones
operation_count = 0

# Sobrescribir la función original para contar las operaciones
def recursive_function(n):
    global operation_count
    operation_count += 1

    if n <= 0:
        return
    else:
        # Llamada recursiva con un subproblema más pequeño
        recursive_function(n - 1)

# Prueba del código
calculate_complexity(5)
