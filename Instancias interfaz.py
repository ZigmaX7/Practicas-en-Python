import tkinter as tk # importa librería tkinter

# crea ventanas tkinter

root = tk.Tk()
root1 = tk.Tk()
root2 = tk.Tk()

#define tamaño de ventanas
root.geometry("200x200")
root1.geometry("400x300")
root2.geometry("300x300") 

# coloca title a ventanas
label = tk.Label(root, text = " Hola buen día !!")
label = tk.Label(root1, text = " Hola Buenas tardes!!!")
label = tk.Label(root2, text = " Hola buenas noches!!")
# aplica etiquetas de title a ventanas
label.pack()
label.pack()
label.pack()

# invoca ventanas.
root.mainloop()
root1.mainloop()
root2.mainloop()