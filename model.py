import sqlite3


class BaseDatosProductos:
    def __init__(self):
        self.conn = sqlite3.connect('productos.db')
        self._crear_tabla()

    def _crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY,
            codigo TEXT NOT NULL,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        );
        ''')
        self.conn.commit()

    def agregar_producto(self, codigo, nombre, precio, stock):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            INSERT INTO productos (codigo, nombre, precio, stock)
            VALUES (?, ?, ?, ?);
            ''', (codigo, nombre, precio, stock))
            self.conn.commit()
        except Exception as e:
            print(f"Error al agregar producto: {e}")
            self.conn.rollback()

    def listar_productos(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, codigo, nombre, precio, stock FROM productos')
        return cursor.fetchall()

    def actualizar_producto(self, codigo, nuevo_nombre, nuevo_precio, nuevo_stock):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            UPDATE productos 
            SET nombre = ?, precio = ?, stock = ?
            WHERE codigo = ?;
            ''', (nuevo_nombre, nuevo_precio, nuevo_stock, codigo))
            self.conn.commit()
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            self.conn.rollback()

    def eliminar_producto(self, codigo):
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
            DELETE FROM productos 
            WHERE codigo = ?;
            ''', (codigo,))
            self.conn.commit()
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            self.conn.rollback()

    def cerrar(self):
        if self.conn:
            self.conn.close()
