import tkinter as tk
from tkinter import simpledialog
from controller import ControladorProductos



def agregar_producto():
    codigo = codigo_entry.get()
    nombre = nombre_entry.get()
    precio = precio_entry.get()
    stock = stock_entry.get()

    if codigo and nombre and precio and stock:  # Verifica si los campos no están vacíos
        try:
            # Intenta convertir a float e int solo si los campos no están vacíos
            precio = float(precio)
            stock = int(stock)
            controlador.agregar_producto(codigo, nombre, precio, stock)
            listar_productos()
            print("Producto agregado con éxito.")
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos para Precio y Stock.")
    else:
        print("Por favor, complete todos los campos.")

def listar_productos():
    lista_productos.delete(0, tk.END)
    productos = controlador.listar_productos()
    for producto in productos:
        lista_productos.insert(tk.END, f"ID: {producto[0]}, Código: {producto[1]}, Nombre: {producto[2]}, Precio: ${producto[3]}, Stock: {producto[4]}")

def eliminar_producto():
    selected = lista_productos.curselection()
    if selected:
        codigo = controlador.listar_productos()[selected[0]][1]  # Selecciona el código del producto
        controlador.eliminar_producto(codigo)
        listar_productos()


def obtener_nuevo_nombre():
    nuevo_nombre = simpledialog.askstring("Actualizar Producto", "Ingrese el nuevo nombre del producto")
    return nuevo_nombre

def obtener_nuevo_precio():
    nuevo_precio = simpledialog.askfloat("Actualizar Producto", "Ingrese el nuevo precio del producto")
    return nuevo_precio

def obtener_nuevo_stock():
    nuevo_stock = simpledialog.askinteger("Actualizar Producto", "Ingrese el nuevo stock del producto")
    return nuevo_stock

def actualizar_producto():
    selected = lista_productos.curselection()
    if selected:
        producto = controlador.listar_productos()[selected[0]]
        codigo = producto[1]  # Suponiendo que el código está en la posición 1 de la lista del producto

        nuevo_nombre = obtener_nuevo_nombre()  # Obtener el nuevo nombre
        if nuevo_nombre:
            nuevo_precio = obtener_nuevo_precio()  # Obtener el nuevo precio
            nuevo_stock = obtener_nuevo_stock()  # Obtener el nuevo stock

            # Lógica para actualizar el producto con el nuevo nombre, precio y stock obtenidos
            controlador.actualizar_producto(codigo, nuevo_nombre, nuevo_precio, nuevo_stock)
            listar_productos()  # Actualizar la lista de productos

root = tk.Tk()
root.title("Gestión de Productos")

# Resto del código de tu interfaz gráfica


# Cambiando colores para el fondo y texto de la interfaz
root.configure(bg="lightgray")  # Color de fondo

controlador = ControladorProductos()

# Etiquetas y campos para agregar un producto
tk.Label(root, text="Código:", bg="lightgray").grid(row=0, column=0)
codigo_entry = tk.Entry(root)
codigo_entry.grid(row=0, column=1)

tk.Label(root, text="Nombre:", bg="lightgray").grid(row=1, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=1, column=1)

tk.Label(root, text="Precio:", bg="lightgray").grid(row=2, column=0)
precio_entry = tk.Entry(root)
precio_entry.grid(row=2, column=1)

tk.Label(root, text="Stock:", bg="lightgray").grid(row=3, column=0)
stock_entry = tk.Entry(root)
stock_entry.grid(row=3, column=1)

# Botón para agregar producto
tk.Button(root, text="Agregar Producto", command=agregar_producto, bg="blue", fg="white").grid(row=4, column=0, columnspan=2)

# Lista de productos
lista_productos = tk.Listbox(root, width=50)
lista_productos.grid(row=5, column=0, columnspan=2)

listar_productos()  # Muestra los productos existentes

# Botón para eliminar producto
tk.Button(root, text="Eliminar Producto", command=eliminar_producto, bg="red", fg="white").grid(row=6, column=0, columnspan=2)

# Botón para actualizar producto
tk.Button(root, text="Actualizar Producto", command=actualizar_producto, bg="green", fg="white").grid(row=7, column=0, columnspan=2)

root.mainloop()