import tkinter as tk # importa libreria tkinter para interfaz gráfica

def alta_producto():
    print("Alta de productos")

def eliminar_producto():
    print("eliminar producto")


gestion_productos = tk.Tk() # crea la ventana
gestion_productos.geometry("400x400") # se define tamaño de ventana
label = tk.Label(gestion_productos, text = " Gestor de productos")
label.pack()

btn_alta_prod = tk.Button(gestion_productos, text = "Crear un producto", command = alta_producto) 
btn_alta_prod.pack()
btn_elim_prod = tk.Button(gestion_productos, text = "Eliminar un producto", command = eliminar_producto) 
btn_elim_prod.pack()

##### (alta_pruducto, elminar producto son las funciones creadas por nosotros para asignar al boton creado)

gestion_productos.mainloop()
