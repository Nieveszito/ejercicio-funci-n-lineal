import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def graficar():
    try:
        m = float(entry_m.get())
        b = float(entry_b.get())
        
        x = np.linspace(-1000, 1000, 1000)
        y = m * x + b

        ax.clear()
        ax.plot(x, y, label=f"f(x) = {m}x + {b}", color="blue")
        # Dibujar ejes X y Y en el centro
        ax.axhline(0, color='black', linewidth=1)  # Eje X
        ax.axvline(0, color='black', linewidth=1)  # Eje Y
        ax.set_xlim(-30, 30)
        ax.set_ylim(-30, 30)

        ax.set_title("Función Lineal")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.grid(True)
        ax.legend()

        canvas.draw()
    except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos para m y b.")


ventana = tk.Tk()
ventana.title("Funcion Lineal")

ttk.Label(ventana, text="Pendiente (m):").grid(row=0, column=0, padx=10, pady=5)
entry_m = ttk.Entry(ventana)
entry_m.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(ventana, text="Término independiente (b):").grid(row=1, column=0, padx=10, pady=5)
entry_b = ttk.Entry(ventana)
entry_b.grid(row=1, column=1, padx=10, pady=5)

boton = ttk.Button(ventana, text="Graficar", command=graficar)
boton.grid(row=2, column=0, columnspan=2, pady=10)


fig, ax = plt.subplots(figsize=(5,4))
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)


ventana.mainloop()