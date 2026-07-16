import modulo as mm
def main():
    lista_productos = []
    while True:
        mm.mostrar_opciones()
        opcion = mm.solicitar_opcion()
        if opcion == 1:
            mm.agregar_producto(lista_productos)
        elif opcion == 2:
            print("-----Buscar producto por rango de precio -----")
            busqueda = input("Ingrese el rango de precio: ")
            posicion = mm.localizar_producto(lista_productos,busqueda)
 
 
            if posicion != -1:
                producto = lista_productos[posicion]
                print(f"producto encontrado en índice: {posicion}")
                print(f"categoria: {producto['categoria']}")
                print(f"unidades: {producto['unidades']}")
                print(f"precio: {producto['precio']}")
            else:
                print(f"El producto '{busqueda}' no se encuentra registrado.")
        elif opcion == 3:
            mm.actualizar_precios(lista_productos)
            print("Estados analizados y actualizados globalmente")
        elif opcion == 4:
            mm.agregar_producto(lista_productos)
        elif opcion == 5:
            print("-----Eliminar producto -----")
            eliminar = input("Ingrese el nombre del servidor a eliminar: ")
            posicion = mm.localizar_producto(lista_productos,eliminar)
            if posicion != 1:
                lista_productos.pop(posicion)
                print(f"El producto ha sido eliminado del sistema")
            else:
                print(f"El producto '{eliminar}' no se encuentra registrado")
        elif opcion == 6:
            print("Saliendo del sistema....")
            break
if __name__ == "__main__":
    main()