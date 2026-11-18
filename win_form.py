import tkinter as tk
from tkinter import ttk, filedialog, messagebox


def open_win_form(parent):
    win = tk.Toplevel(parent)
    win.title("KreaTea - Registro")
    win.geometry("1000x600")
    win.configure(bg="#E9F0FD")

    # ---------- Barra lateral ----------
    lateral = tk.Frame(win, bg="#1E3A6E", width=200)
    lateral.pack(side="left", fill="y")
    lateral.pack_propagate(False)

    tk.Label(lateral, text="🧩", bg="#1E3A6E", font=("Arial", 40)).pack(pady=(20, 0))
    tk.Label(lateral, text="KreaTea", bg="#1E3A6E", fg="white",
             font=("Arial", 16, "bold")).pack()
    tk.Label(lateral, text="Apoyo en cada paso", bg="#1E3A6E", fg="white",
             font=("Arial", 9)).pack(pady=(0, 20))

   

    tk.Button(lateral, text="Cerrar sesión", command=win.destroy).pack(side="bottom", pady=20)

    # ---------- Formulario ----------
    form = tk.Frame(win, bg="white")
    form.pack(side="left", fill="both", expand=True, padx=(0, 15), pady=15)

    tk.Label(form, text="Registro de Usuario", bg="white", fg="#1B2F5E",
             font=("Arial", 18, "bold")).grid(row=0, column=0, columnspan=2, pady=(20, 0))
    tk.Label(form, text="Completa la información para crear una cuenta", bg="white",
             font=("Arial", 11)).grid(row=1, column=0, columnspan=2, pady=(0, 20))

    # Nombre
    tk.Label(form, text="Nombre del niño/a", bg="white").grid(row=2, column=0, sticky="w", padx=30)
    ent_nombre = ttk.Entry(form, width=30)
    ent_nombre.grid(row=3, column=0, padx=30, pady=(0, 10), sticky="w")

    # Edad
    tk.Label(form, text="Edad", bg="white").grid(row=2, column=1, sticky="w")
    ent_edad = ttk.Entry(form, width=30)
    ent_edad.grid(row=3, column=1, pady=(0, 10), sticky="w")

    # Sexo
    tk.Label(form, text="Sexo", bg="white").grid(row=4, column=0, sticky="w", padx=30)
    cmb_sexo = ttk.Combobox(form, values=["Masculino", "Femenino", "No mencionar", "Otro"],
                            state="readonly", width=27)
    cmb_sexo.set("Selecciona una opción")
    cmb_sexo.grid(row=5, column=0, padx=30, pady=(0, 10), sticky="w")

    # Nivel de apoyo
    tk.Label(form, text="Nivel de apoyo", bg="white").grid(row=4, column=1, sticky="w")
    cmb_nivel = ttk.Combobox(form, values=["Nivel 1", "Nivel 2", "Nivel 3"],
                             state="readonly", width=27)
    cmb_nivel.set("Selecciona un nivel")
    cmb_nivel.grid(row=5, column=1, pady=(0, 10), sticky="w")

    # Correo
    tk.Label(form, text="Correo del tutor", bg="white").grid(row=6, column=0, sticky="w", padx=30)
    ent_correo = ttk.Entry(form, width=65)
    ent_correo.grid(row=7, column=0, columnspan=2, padx=30, pady=(0, 10), sticky="w")

    # Contraseña
    tk.Label(form, text="Contraseña (mínimo 8 caracteres)", bg="white").grid(
        row=8, column=0, sticky="w", padx=30)
    ent_pw = ttk.Entry(form, width=65, show="*")
    ent_pw.grid(row=9, column=0, columnspan=2, padx=30, pady=(0, 10), sticky="w")

    # ---------- Validar y guardar ----------
    def validar_y_guardar():
        nombre = ent_nombre.get().strip()
        edad = cmb_edad.get()
        sexo = cmb_sexo.get()
        nivel = cmb_nivel.get()
        correo = ent_correo.get().strip()
        pw = ent_pw.get()

        if nombre == "":
            messagebox.showerror("Error", "El nombre es requerido.")
            return
        if edad not in edad:
            messagebox.showerror("Error", "Selecciona la edad.")
            return
        if sexo not in ["Masculino", "Femenino", "Otro"]:
            messagebox.showerror("Error", "Selecciona el sexo.")
            return
        if nivel not in ["Nivel 1", "Nivel 2", "Nivel 3"]:
            messagebox.showerror("Error", "Selecciona el nivel de apoyo.")
            return
        if "@" not in correo or "." not in correo:
            messagebox.showerror("Error", "Escribe un correo válido.")
            return
        if len(pw) < 8:
            messagebox.showerror("Error", "La contraseña debe tener mínimo 8 caracteres.")
            return

        ruta = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Texto", "*.txt")])
        if ruta:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write("Nombre: " + nombre + "\n")
                f.write("Edad: " + edad + "\n")
                f.write("Sexo: " + sexo + "\n")
                f.write("Nivel de apoyo: " + nivel + "\n")
                f.write("Correo del tutor: " + correo + "\n")
            messagebox.showinfo("OK", "Datos guardados.")

    tk.Button(form, text="Crear cuenta", bg="#2F6FDB", fg="white",
              font=("Arial", 13, "bold"), width=25, command=validar_y_guardar
              ).grid(row=10, column=0, columnspan=2, pady=15)

    return win


# Para probar el código
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    ventana = open_win_form(root)
    ventana.protocol("WM_DELETE_WINDOW", root.destroy)
    root.mainloop()
