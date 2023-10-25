from controller import ControladorProductos

def main():
    controlador = ControladorProductos()

    while True:
        print("\nMenú:")
        print("1. Agregar producto")
        print("2. Actualizar productos")
        print("3. Eliminar productos")
        print("4. Listar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            
            try:
                precio = float(input("Ingrese el precio del producto: "))
                stock = int(input("Ingrese el stock del producto: "))
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos.")
                continue

            controlador.agregar_producto(codigo, nombre, precio, stock)
            print("Producto agregado con éxito.")
            
        elif opcion == "4": 
            print("\nLista de productos:")
            productos = controlador.listar_productos()
            for producto in productos:
                print(f"ID: {producto[0]}, Código: {producto[1]}, Nombre: {producto[2]}, Precio: ${producto[3]}, Stock: {producto[4]}")
                
        elif opcion == "5":
            print("Cerrando la base de datos y saliendo del programa.")
            controlador.cerrar_base_datos()
            break
            
        else:
            print("Opción no válida.")
 

if __name__ == "__main__":
    main()
