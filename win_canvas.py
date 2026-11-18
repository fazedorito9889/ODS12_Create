import tkinter as tk
from tkinter import ttk

def open_win_canvas(parent):
    # Crear ventana secundaria vinculada al menú principal
    win = tk.Toplevel(parent)
    win.title("KreaTea - Progresos y Estadísticas Semanales")
    win.geometry("920x540")
    win.configure(bg="#F4F7FC")
    win.grab_set()

    # --- ENCABEZADO DE LA SECCIÓN ---
    header_frame = tk.Frame(win, bg="#F4F7FC")
    header_frame.pack(fill=tk.X, padx=30, pady=(20, 15))

    title_label = tk.Label(
        header_frame, 
        text="KreaTea • Progresos y Estadísticas Semanales", 
        font=("Segoe UI", 17, "bold"), 
        fg="#1E293B", 
        bg="#F4F7FC"
    )
    title_label.pack(anchor="w")

    subtitle_label = tk.Label(
        header_frame, 
        text="Visualiza el cumplimiento de rutinas y actividades de apoyo de tu hijo en la escuela.", 
        font=("Segoe UI", 10), 
        fg="#64748B", 
        bg="#F4F7FC"
    )
    subtitle_label.pack(anchor="w", pady=(2, 0))

    # --- CONTENEDOR PRINCIPAL ---
    content_frame = tk.Frame(win, bg="#F4F7FC")
    content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0, 10))

    # --- TARJETA IZQUIERDA: LIENZO (CANVAS) CON GRÁFICA ---
    canvas_card = tk.Frame(content_frame, bg="white", bd=0, highlightbackground="#E2E8F0", highlightthickness=1)
    canvas_card.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 15))

    card_title = tk.Label(
        canvas_card, 
        text="Gráfica de Actividades Completadas (%)", 
        font=("Segoe UI", 12, "bold"), 
        fg="#1E293B", 
        bg="white"
    )
    card_title.pack(anchor="w", padx=20, pady=(15, 5))

    canvas = tk.Canvas(canvas_card, bg="#FFFFFF", highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

    def draw_chart(event=None):
        canvas.delete("all")
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        
        if width < 50 or height < 50:
            return

        days = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        values = [70, 85, 60, 90, 95, 80, 75]
        
        max_val = 100
        chart_top = 35
        chart_bottom = height - 45
        chart_height = chart_bottom - chart_top
        
        num_bars = len(days)
        total_width = width - 60
        bar_width = max(22, int(total_width / (num_bars * 1.8)))
        spacing = int((total_width - (bar_width * num_bars)) / (num_bars + 1))

        for i in range(4):
            y = chart_top + int((chart_height / 3) * i)
            val_label = str(100 - int(33.3 * i)) + "%"
            canvas.create_text(35, y, text=val_label, fill="#94A3B8", font=("Segoe UI", 9), anchor="e")
            canvas.create_line(45, y, width - 20, y, fill="#F1F5F9", dash=(4, 4))

        for i in range(num_bars):
            x1 = 50 + spacing + i * (bar_width + spacing)
            val_pct = values[i]
            bar_h = int((val_pct / max_val) * chart_height)
            y1 = chart_bottom - bar_h
            x2 = x1 + bar_width
            y2 = chart_bottom

            bar_color = "#3B82F6" if val_pct < 90 else "#1D4ED8"

            canvas.create_rectangle(x1, y1, x2, y2, fill=bar_color, outline="")
            canvas.create_text(x1 + bar_width/2, y1 - 12, text=f"{val_pct}%", fill="#334155", font=("Segoe UI", 9, "bold"))
            canvas.create_text(x1 + bar_width/2, chart_bottom + 18, text=days[i], fill="#64748B", font=("Segoe UI", 10, "bold"))

    canvas.bind("<Configure>", draw_chart)

    # --- TARJETA DERECHA: RESUMEN Y CONSEJOS ---
    info_card = tk.Frame(content_frame, bg="white", bd=0, highlightbackground="#E2E8F0", highlightthickness=1, width=290)
    info_card.pack(side=tk.RIGHT, fill=tk.Y, padx=(15, 0))
    info_card.pack_propagate(False)

    info_title = tk.Label(
        info_card, 
        text="Resumen del Periodo", 
        font=("Segoe UI", 12, "bold"), 
        fg="#1E293B", 
        bg="white"
    )
    info_title.pack(anchor="w", padx=20, pady=(15, 12))

    def add_metric(label_text, value_text, color):
        row = tk.Frame(info_card, bg="white")
        row.pack(fill=tk.X, padx=20, pady=6)
        tk.Label(row, text=label_text, font=("Segoe UI", 10), fg="#64748B", bg="white").pack(side=tk.LEFT)
        tk.Label(row, text=value_text, font=("Segoe UI", 10, "bold"), fg=color, bg="white").pack(side=tk.RIGHT)

    add_metric("Promedio Semanal", "85%", "#3B82F6")
    add_metric("Rutinas Constantes", "5 / 7 días", "#10B981")
    add_metric("Ejercicios Cognitivos", "12 completados", "#8B5CF6")

    tip_frame = tk.Frame(info_card, bg="#EFF6FF", bd=0)
    tip_frame.pack(fill=tk.X, padx=20, pady=20)

    tk.Label(tip_frame, text="💡 Consejo KreaTea", font=("Segoe UI", 10, "bold"), fg="#1E40AF", bg="#EFF6FF").pack(anchor="w", padx=12, pady=(10, 4))
    tk.Label(
        tip_frame, 
        text="Mantener una rutina visual constante ayuda a tu hijo a sentirse más seguro y anticipar las actividades del día.", 
        font=("Segoe UI", 9), 
        fg="#1E3A8A", 
        bg="#EFF6FF", 
        justify=tk.LEFT, 
        wraplength=230
    ).pack(anchor="w", padx=12, pady=(0, 10))

    # --- PIE DE VENTANA CON BOTÓN CERRAR ---
    footer_frame = tk.Frame(win, bg="#F4F7FC")
    footer_frame.pack(fill=tk.X, padx=30, pady=(5, 20))

    btn_cerrar = ttk.Button(footer_frame, text="Cerrar", command=win.destroy)
    btn_cerrar.pack(side=tk.RIGHT)