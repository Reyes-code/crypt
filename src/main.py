# interfaz.py
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.widgets import Button
from werkzug import KeyHasher  # Asegúrate que este archivo esté en la misma carpeta

def hash_password():
    hasher = KeyHasher()
    result = hasher.hash_combined(entry.get())
    password = entry.get()
    output.config(state='normal')
    output.delete(1.0, tk.END)
    output.insert(tk.END, result)
    output.config(state='disabled')
    print(hasher.normal_hash(password))

# Configuración de la ventana
root = tk.Tk()
root.title("Sistema de Hashing Seguro")
Style(theme='minty')

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Elementos UI
tk.Label(frame, text="Sistema de Hashing Seguro", font=('Helvetica', 16)).pack(pady=10)
tk.Label(frame, text="Ingrese su contraseña:").pack()

entry = tk.Entry(frame, width=40, show="•")
entry.pack(pady=5)

Button(frame, text="Generar Hash", command=hash_password, bootstyle="success").pack(pady=10)

output = tk.Text(frame, height=5, width=50, state='disabled')
output.pack()

root.mainloop()
