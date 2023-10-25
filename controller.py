from model import BaseDatosProductos

class ControladorProductos:
    def __init__(self):
        self.base_datos = BaseDatosProductos()

    def agregar_producto(self, codigo, nombre, precio, stock):
        self.base_datos.agregar_producto(codigo, nombre, precio, stock)
        
    def Actualizar_producto(self, codigo, nombre, precio, stock):
        producto_codigo = self.view.get_user_id_input()
        new_name = self.view.get_user_input("Ingrese el nuevo producto: ")
        self.model.update_user(user_id, new_name)
        self.view.show_message("producto actualizado exitosamente.")

        self.base_datos.actualizar_producto(codigo, nombre, precio, stock)

    def Eliminar_producto(self, codigo, nombre, precio, stock):
        producto_codigo = self.view.get_user_id_input()
        self.model.delete_user(user_id)
        self.view.show_message("producto eliminado exitosamente.")

        self.base_datos.eliminar_producto(codigo, nombre, precio, stock)

    def listar_productos(self):
        return self.base_datos.listar_productos()

    def cerrar_base_datos(self):
        self.base_datos.cerrar()



    