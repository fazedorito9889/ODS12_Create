import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

def open_win_list(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Krea-Tea - Gestión de Usuarios")
    win.geometry("980x580")
    win.configure(bg="#f1f5f9")

   
    win.image_references = []

    style = ttk.Style()
    style.theme_use("clam")

    COLOR_PRIMARY = "#1e3a8a"
    COLOR_ACCENT = "#2563eb"
    COLOR_BG = "#f1f5f9"
    COLOR_CARD = "#ffffff"
    COLOR_BADGE = "#dbeafe"

    style.configure("TFrame", background=COLOR_BG)
    style.configure("Card.TFrame", background=COLOR_CARD, relief="flat")
    style.configure("Title.TLabel", background=COLOR_BG, foreground=COLOR_PRIMARY, font=("Segoe UI", 18, "bold"))
    style.configure("Subtitle.TLabel", background=COLOR_BG, foreground="#64748b", font=("Segoe UI", 10))
    style.configure("Action.TButton", background=COLOR_ACCENT, foreground="white", font=("Segoe UI", 9, "bold"))

    main_frm = ttk.Frame(win, padding=20)
    main_frm.pack(fill="both", expand=True)

    header_frm = ttk.Frame(main_frm)
    header_frm.pack(fill="x", pady=(0, 15))

    ttk.Label(header_frm, text="Usuarios", style="Title.TLabel").pack(anchor="w")
    ttk.Label(header_frm, text="Gestiona los perfiles de tus hijos y revisa su información", style="Subtitle.TLabel").pack(anchor="w")

    content_frm = ttk.Frame(main_frm)
    content_frm.pack(fill="both", expand=True)

    left_container = ttk.Frame(content_frm)
    left_container.pack(side="left", fill="both", expand=True, padx=(0, 15))

    canvas = tk.Canvas(left_container, bg=COLOR_BG, highlightthickness=0)
    scrollbar = ttk.Scrollbar(left_container, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas, style="TFrame")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    right_container = ttk.Frame(content_frm, width=280)
    right_container.pack(side="right", fill="y", padx=(0, 0))

    summary_card = ttk.Frame(right_container, style="Card.TFrame", padding=15)
    summary_card.pack(fill="x", pady=(0, 15))
    
    ttk.Label(summary_card, text="📊 Resumen General", font=("Segoe UI", 11, "bold"), background=COLOR_CARD, foreground=COLOR_PRIMARY).pack(anchor="w", pady=(0, 10))
    
    stats_frm = ttk.Frame(summary_card, style="Card.TFrame")
    stats_frm.pack(fill="x")
    
    lbl_total = ttk.Label(stats_frm, text="3\nNiños", font=("Segoe UI", 12, "bold"), background=COLOR_CARD, foreground=COLOR_PRIMARY, justify="center")
    lbl_total.pack(side="left", expand=True)
    
    lbl_act = ttk.Label(stats_frm, text="12 h\nActividades", font=("Segoe UI", 12, "bold"), background=COLOR_CARD, foreground=COLOR_PRIMARY, justify="center")
    lbl_act.pack(side="right", expand=True)

    form_card = ttk.Frame(right_container, style="Card.TFrame", padding=15)
    form_card.pack(fill="x", pady=(0, 15))

    ttk.Label(form_card, text="Acciones rápidas", font=("Segoe UI", 11, "bold"), background=COLOR_CARD, foreground=COLOR_PRIMARY).pack(anchor="w", pady=(0, 8))

    usuarios = [
        {"nombre": "Lucas Pérez", "edad": "7 años", "apoyo": "Apoyo moderado", "avatar": ""},
        {"nombre": "María González", "edad": "6 años", "apoyo": "Apoyo leve", "avatar": ""},
        {"nombre": "Mateo López", "edad": "8 años", "apoyo": "Apoyo intenso", "avatar": ""}
    ]

    def actualizar_lista():
        win.image_references.clear()

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        for idx, user in enumerate(usuarios):
            card = ttk.Frame(scrollable_frame, style="Card.TFrame", padding=12)
            card.pack(fill="x", pady=6, padx=2)

            avatar_frm = ttk.Frame(card, style="Card.TFrame")
            avatar_frm.pack(side="left", padx=(0, 12))

            img_label = ttk.Label(avatar_frm, background="#e2e8f0")
            img_label.pack()

            img_loaded = False
            if user['avatar'] and os.path.exists(user['avatar']):
                try:
                    img = tk.PhotoImage(file=user['avatar'])
                    if img.width() > 60 or img.height() > 60:
                        factor = max(img.width() // 60, img.height() // 60, 1)
                        img = img.subsample(factor, factor)
                    img_label.config(image=img)
                    win.image_references.append(img)
                    img_loaded = True
                except Exception as e:
                    print(f"Aviso al cargar imagen: {e}")

            if not img_loaded:
                img_label.config(text="👤", font=("Segoe UI", 22), foreground=COLOR_PRIMARY)

            info_frm = ttk.Frame(card, style="Card.TFrame")
            info_frm.pack(side="left", fill="y", anchor="w")

            ttk.Label(info_frm, text=user['nombre'], font=("Segoe UI", 11, "bold"), background=COLOR_CARD, foreground="#0f172a").pack(anchor="w")
            ttk.Label(info_frm, text=user['edad'], font=("Segoe UI", 9), background=COLOR_CARD, foreground="#64748b").pack(anchor="w")
            
            ttk.Label(info_frm, text=user['apoyo'], font=("Segoe UI", 8, "bold"), background=COLOR_BADGE, foreground=COLOR_PRIMARY, padding=3).pack(anchor="w", pady=(4, 0))

            btn_frm = ttk.Frame(card, style="Card.TFrame")
            btn_frm.pack(side="right", fill="y")

            ttk.Button(btn_frm, text="Ver progreso", command=lambda n=user['nombre']: messagebox.showinfo("Progreso", f"Viendo progreso de {n}")).pack(side="left", padx=2)
            ttk.Button(btn_frm, text="Editar", command=lambda i=idx: abrir_modal_usuario(i)).pack(side="left", padx=2)
            ttk.Button(btn_frm, text="Eliminar", command=lambda i=idx: eliminar_usuario(i)).pack(side="left", padx=2)

        lbl_total.config(text=f"{len(usuarios)}\nNiños")

    def abrir_modal_usuario(idx=None):
        is_edit = idx is not None
        modal = tk.Toplevel(win)
        modal.title("Editar Perfil" if is_edit else "Agregar Nuevo Niño")
        modal.geometry("400x450")
        modal.minsize(400, 450)
        modal.configure(bg=COLOR_BG)
        modal.grab_set()

        frm_modal = ttk.Frame(modal, padding=20)
        frm_modal.pack(fill="both", expand=True)

        ttk.Label(frm_modal, text="Nombre del niño:", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        ent_nombre = ttk.Entry(frm_modal, font=("Segoe UI", 10))
        ent_nombre.pack(fill="x", pady=(0, 10))

        ttk.Label(frm_modal, text="Edad (ej. 7 años):", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        ent_edad = ttk.Entry(frm_modal, font=("Segoe UI", 10))
        ent_edad.pack(fill="x", pady=(0, 10))

        ttk.Label(frm_modal, text="Nivel de Apoyo:", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        combo_apoyo = ttk.Combobox(frm_modal, values=["Apoyo leve", "Apoyo moderado", "Apoyo intenso"], font=("Segoe UI", 10), state="readonly")
        combo_apoyo.pack(fill="x", pady=(0, 10))

        ttk.Label(frm_modal, text="Imagen de perfil (PNG/GIF):", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=(0, 2))
        
        path_var = tk.StringVar(value="")
        path_frame = ttk.Frame(frm_modal)
        path_frame.pack(fill="x", pady=(0, 20))

        lbl_path = ttk.Label(path_frame, text="Ninguna seleccionada", font=("Segoe UI", 8), foreground="#64748b")
        lbl_path.pack(side="left", fill="x", expand=True)

        def seleccionar_imagen():
            archivo = filedialog.askopenfilename(
                title="Seleccionar imagen",
                filetypes=[("Archivos de imagen", "*.png *.gif *.jpg *.jpeg"), ("Todos los archivos", "*.*")]
            )
            if archivo:
                path_var.set(archivo)
                lbl_path.config(text=os.path.basename(archivo), foreground="#0f172a")

        ttk.Button(path_frame, text="Examinar...", command=seleccionar_imagen).pack(side="right", padx=(5, 0))

        if is_edit:
            user_data = usuarios[idx]
            ent_nombre.insert(0, user_data["nombre"])
            ent_edad.insert(0, user_data["edad"])
            combo_apoyo.set(user_data["apoyo"])
            if user_data["avatar"]:
                path_var.set(user_data["avatar"])
                lbl_path.config(text=os.path.basename(user_data["avatar"]), foreground="#0f172a")
        else:
            combo_apoyo.set("Apoyo moderado")

        def guardar():
            nom = ent_nombre.get().strip()
            edad = ent_edad.get().strip()
            apoyo = combo_apoyo.get().strip()
            avatar_path = path_var.get().strip()

            if not nom or not edad:
                messagebox.showwarning("Campos vacíos", "Por favor completa el nombre y la edad.", parent=modal)
                return

            try:
                if is_edit:
                    usuarios[idx] = {"nombre": nom, "edad": edad, "apoyo": apoyo, "avatar": avatar_path}
                else:
                    usuarios.append({"nombre": nom, "edad": edad, "apoyo": apoyo, "avatar": avatar_path})

                actualizar_lista()
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el registro: {e}", parent=modal)
                return

            modal.destroy()

        btn_action_frm = ttk.Frame(frm_modal)
        btn_action_frm.pack(fill="x", pady=(10, 0))

        ttk.Button(btn_action_frm, text="Guardar", command=guardar, style="Action.TButton").pack(side="left", fill="x", expand=True, padx=(0, 5))
        ttk.Button(btn_action_frm, text="Cancelar", command=modal.destroy).pack(side="right", fill="x", expand=True, padx=(5, 0))

    def eliminar_usuario(idx):
        if 0 <= idx < len(usuarios):
            usuarios.pop(idx)
            actualizar_lista()

    ttk.Button(form_card, text="+ Agregar niño", command=lambda: abrir_modal_usuario(None), style="Action.TButton").pack(fill="x", pady=5)

    footer_frm = ttk.Frame(main_frm, style="Card.TFrame", padding=10)
    footer_frm.pack(fill="x", pady=(10, 0))
    ttk.Label(footer_frm, text="ℹ️ Puedes agregar hasta 3 perfiles por cuenta de forma gratuita.", 
              background=COLOR_CARD, foreground="#334155", font=("Segoe UI", 9)).pack(anchor="w")

    actualizar_lista()