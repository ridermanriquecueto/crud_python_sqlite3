from model import BaseDatosProductos

class ControladorProductos:
    def __init__(self):
        self.base_datos = BaseDatosProductos()

    def listar_productos(self):
        return self.base_datos.listar_productos()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.base_datos.agregar_producto(codigo, nombre, precio, stock)

    def eliminar_producto(self, codigo):
        self.base_datos.eliminar_producto(codigo)


        # Dentro de controller.py

    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio, nuevo_stock):
        producto_existente = self.obtener_producto_por_codigo(codigo)

        if producto_existente:
            self.base_datos.actualizar_producto(codigo, nuevo_nombre, nuevo_precio, nuevo_stock)
            return True
        else:
            print("El producto con el código dado no existe en la base de datos.")
            return False
        
    def obtener_producto_por_codigo(self, codigo):
        return self.base_datos.obtener_producto_por_codigo(codigo)    
     
     
    def cerrar_base_datos(self):
        self.base_datos.cerrar()



