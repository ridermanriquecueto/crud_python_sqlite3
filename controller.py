from model import BaseDatosProductos

class ControladorProductos:
    def __init__(self):
        self.base_datos = BaseDatosProductos()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.base_datos.agregar_producto(codigo, nombre, precio, stock)

    def listar_productos(self):
        return self.base_datos.listar_productos()
    
    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio, nuevo_stock):
        self.base_datos.actualizar_producto(codigo, nuevo_nombre, nuevo_precio, nuevo_stock)

    def eliminar_producto(self, codigo):
        self.base_datos.eliminar_producto(codigo)

    def cerrar_base_datos(self):
        self.base_datos.cerrar()
