import tkinter as tk
from tkinter import ttk

# ventanas importadas de la carpeta app/
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas

def main():
    # 1.ventana principal
    root = tk.Tk()
    root.title("KreaTea")
    root.geometry("750x450")
    root.configure(bg="#EEF4FA")  # Color de fondo general de la app

    # 2. Creamos los dos contenedores principales
    # sidebar = barra lateral de navegación
    sidebar = tk.Frame(root, bg="#163560", width=180)
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)  # Evita que la barra lateral se encoja

    # content = área principal de la derecha
    content = tk.Frame(root, bg="#EEF4FA", padx=20, pady=20)
    content.pack(side="right", fill="both", expand=True)  

    # ================= 3. DISEÑO DE LA BARRA LATERAL =================
   
    # Título y subtítulo en la barra lateral
    tk.Label(sidebar, text="KreaTea", font=("Segoe UI", 14, "bold"), fg="white", bg="#163560").pack(pady=(20, 2))
    tk.Label(sidebar, text="APRENDIZAJE", font=("Segoe UI", 7, "bold"), fg="#A0B8D0", bg="#163560").pack(pady=(0, 15))

    # Botones del menú principal
    tk.Button(sidebar, text="🏠  Inicio", font=("Segoe UI", 9), fg="white", bg="#163560", bd=0, anchor="w", padx=15, pady=6, command=lambda: open_win_home(root)).pack(fill="x", pady=2)
    tk.Button(sidebar, text="⚙️  Formulario", font=("Segoe UI", 9), fg="white", bg="#163560", bd=0, anchor="w", padx=15, pady=6, command=lambda: open_win_form(root)).pack(fill="x", pady=2)
    tk.Button(sidebar, text="📋  Lista", font=("Segoe UI", 9), fg="white", bg="#163560", bd=0, anchor="w", padx=15, pady=6, command=lambda: open_win_list(root)).pack(fill="x", pady=2)
    tk.Button(sidebar, text="📊  Progreso", font=("Segoe UI", 9), fg="white", bg="#163560", bd=0, anchor="w", padx=15, pady=6, command=lambda: open_win_table(root)).pack(fill="x", pady=2)
    tk.Button(sidebar, text="🧠  Ejercicios", font=("Segoe UI", 9), fg="white", bg="#163560", bd=0, anchor="w", padx=15, pady=6, command=lambda: open_win_canvas(root)).pack(fill="x", pady=2)

    # Botón Salir en la parte inferior de la barra lateral
    tk.Button(sidebar, text="↪  Salir", font=("Segoe UI", 9), fg="#FFCCCC", bg="#163560", bd=0, anchor="w", padx=15, pady=6, command=root.destroy).pack(side="bottom", fill="x", pady=15)

    # ================= 4. ÁREA DE CONTENIDO PRINCIPAL =================
   
    # Encabezado de bienvenida
    tk.Label(content, text="Hola, María", font=("Segoe UI", 18, "bold"), fg="#12263A", bg="#EEF4FA").pack(anchor="w", pady=(0, 4))
    tk.Label(content, text="Aquí puedes ver el progreso de tu hijo", font=("Segoe UI", 10), fg="#5A6B7C", bg="#EEF4FA").pack(anchor="w", pady=(0, 15))

    # Tarjeta sencilla de resumen del niño
    tarjeta = tk.Frame(content, bg="white", padx=15, pady=15, highlightbackground="#DCE5F0", highlightthickness=1)
    tarjeta.pack(fill="x", pady=5)
   
    tk.Label(tarjeta, text=" Perfil del Niño: Daniel (7 años)", font=("Segoe UI", 11, "bold"), fg="#12263A", bg="white").pack(anchor="w")
    tk.Label(tarjeta, text="Tutor: María  |  Fecha de ingreso: 15/09/2026", font=("Segoe UI", 9), fg="#5A6B7C", bg="white").pack(anchor="w", pady=(4, 0))

    # 5. Mantiene la ventana abierta ejecutando el programa
    root.mainloop()

if __name__ == "__main__":
    main()
