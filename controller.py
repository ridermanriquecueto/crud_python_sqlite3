from model import BaseDatosProductos


class ControladorProductos:
    def __init__(self):
        self.base_datos = BaseDatosProductos()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.base_datos.agregar_producto(codigo, nombre, precio, stock)
        
    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio, nuevo_stock):
        producto_existente = self.base_datos.obtener_producto_por_codigo(codigo)
        
        if producto_existente:
            while True:
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
                    nuevo_stock = int(input("Ingrese el nuevo stock del producto: "))
                    break  # Esto finaliza el bucle, ya que se obtuvieron los valores correctamente
                except ValueError:
                    print("Por favor, ingrese valores numéricos válidos.")
            
            self.base_datos.actualizar_producto(codigo, nuevo_nombre, nuevo_precio, nuevo_stock)
        else:
            print("El producto con el código dado no existe en la base de datos.")

    def eliminar_producto(self, codigo):
        self.base_datos.eliminar_producto(codigo)

    def listar_productos(self):
        return self.base_datos.listar_productos()

    def cerrar_base_datos(self):
        self.base_datos.cerrar()

    def obtener_producto_por_codigo(self, codigo):
        return self.base_datos.obtener_producto_por_codigo(codigo)
