import tkinter as tk
from tkinter import ttk, messagebox
import csv
from pathlib import Path

def open_win_table(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Tabla (Treeview)")
    win.geometry("720x300")

    barra = tk.Frame(win, bg="#1E3A6E", width=160)
    barra.pack(side="left", fill="y")
    barra.pack_propagate(False)
    tk.Label(barra, text="👤", font=("Segoe UI Emoji", 30), bg="#1E3A6E", fg="white").pack(pady=(24, 4))
    tk.Label(barra, text="Tu nombre", font=("Segoe UI", 13, "bold"), bg="#1E3A6E", fg="white").pack()
    tk.Button(barra, text="Cerrar sesión", command=win.destroy, bg="#1E3A6E", fg="white",
              relief="flat", cursor="hand2").pack(side="bottom", fill="x", padx=12, pady=14)

    frm = ttk.Frame(win, padding=12)
    frm.pack(side="left", fill="both", expand=True)

    cols = ("nombre", "valor1", "valor2")
    tv = ttk.Treeview(frm, columns=cols, show="headings", height=10)
    for c in cols:
        tv.heading(c, text=c.capitalize())
        tv.column(c, width=120, anchor="center")
    tv.pack(fill="both", expand=True)

    ruta = Path(_file_).resolve().parents[2] / "data" / "sample.csv"  # <repo>/data/sample.csv
    if not ruta.exists():
        messagebox.showwarning("Aviso", f"No se encontró {ruta}. Crea el archivo de ejemplo.")
        return

    with open(ruta, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tv.insert("", "end", values=(row["nombre"], row["valor1"], row["valor2"]))

    ttk.Button(frm, text="Cerrar", command=win.destroy).pack(pady=8, anchor="e")