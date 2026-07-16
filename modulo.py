productos = {
'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True,
False],
'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False,
False],
'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False,
True],
'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True,
False],
'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False,
False]
}

stock = {
'M001': [32990, 12],
'M002': [9990, 0],
'M003': [5490, 25],
'M004': [7990, 5],
'M005': [11990, 7],
'M006': [24990, 3]
}

def mostrar_opciones():
    print("----- MENÚ PRINCIPAL -----")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precios")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
def solicitar_opcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        return -1
def validar_categoria(categoria):
    return len(categoria.strip()) > 0
def validar_nuevoproducto(producto):
    return len(producto.strip()) > 0
def validar_unidades(unidades_str):
    try:
        valor = int(unidades_str)
        return valor > 0
    except ValueError:
        return False
def validar_precio(valor_str):
        precio=float(valor_str)
def registrar_categoria(lista_productos):
    print("\n--- Registrar categoria ---")
    cat = input("Ingrese nombre de categoria: ")
    uni = input("Ingrese unidades: ")
    pre = input("Ingrese precio de producto: ")
    if not validar_categoria(cat):
        print("[ERROR]: El nombre no puede estar vacío")
        return
    if not validar_unidades(uni):
        print("[ERROR]: El uptime debe ser un número entero mayor a cero")
        return
    if not validar_precio(pre):
        print("[ERROR]: La carga debe ser un número decimal entre 1.0 y 100.0")
        return
    lista_productos ={
        "categoria":cat.strip(),
        "unidades":int(uni),
        "precio":float(pre)
    }
    lista_productos.append()
    print("producto registrado exitosamente")
def localizar_producto(lista_productos,nombre_buscar):
    for i in range(len(lista_productos)):
        if lista_productos[i]["nombre"].lower() == nombre_buscar.strip().lower():
            return i
    return -1