import tkinter as tk
from tkinter import messagebox


#Tkinter
ventana = tk.Tk()
ventana.title("Inventario Tienda Animal")
ventana.geometry("400x400")

tk.Label(ventana, text="Codigo").pack()
entrada_codigo = tk.Entry(ventana)
entrada_codigo.pack()

tk.Label(ventana, text="Producto").pack()
entrada_producto = tk.Entry(ventana)
entrada_producto.pack()

tk.Label(ventana, text="Animal").pack()
entrada_animal = tk.Entry(ventana)
entrada_animal.pack()

tk.Label(ventana, text="Categoria").pack()
entrada_categoria = tk.Entry(ventana)
entrada_categoria.pack()

tk.Label(ventana, text="Stock").pack()
entrada_stock = tk.Entry(ventana)
entrada_stock.pack()

tk.Label(ventana, text="Precio").pack()
entrada_precio = tk.Entry(ventana)
entrada_precio.pack()


ventana.mainloop()
