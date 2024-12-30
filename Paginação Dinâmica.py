import tkinter as tk
from tkinter import ttk

# Definição das páginas
pages = [
    "Página 1: Bem-vindo à primeira página!",
    "Página 2: Aqui estão mais algumas informações.",
    "Página 3: Você está na metade do caminho!",
    "Página 4: Quase no fim!",
    "Página 5: Obrigado por visitar a última página",
]

current_page = 0

def update_content():
    """Atualiza o conteúdo da página e os botões de navegação."""
    page_label.config(text=pages[current_page])

    # Atualiza a cor dos botões de páginas
    for i, btn in enumerate(page_buttons):
        if i == current_page:
            btn.config(style="Active.TButton")
        else:
            btn.config(style="TButton")

    # Habilita/desabilita os botões anterior e próximo
    prev_button.config(state="normal" if current_page > 0 else "disabled")
    next_button.config(state="normal" if current_page < len(pages) - 1 else "disabled")

def go_to_page(page_index):
    """Vai para uma página específica."""
    global current_page
    current_page = page_index
    update_content()

def go_prev():
    """Vai para a página anterior."""
    global current_page
    if current_page > 0:
        current_page -= 1
        update_content()

def go_next():
    """Vai para a próxima página."""
    global current_page
    if current_page < len(pages) - 1:
        current_page += 1
        update_content()

# Configuração da janela principal
root = tk.Tk()
root.title("Paginação Dinâmica")
root.geometry("900x300")
root.configure(bg="#f9f9f9")

# Estilos
style = ttk.Style()
style.configure("TButton", font=("Poppins", 12), padding=5, background="#f4f4f4")
style.configure("Active.TButton", font=("Poppins", 12, "bold"), background="#007bff", foreground="#ffffff")
style.map("TButton", background=[("active", "#e0e0e0")])

# Rótulo do conteúdo
page_label = tk.Label(
    root,
    text="",
    font=("Poppins", 14),
    wraplength=400,
    justify="center",
    bg="#f9f9f9",
    relief="solid",
    padx=10,
    pady=10
)
page_label.pack(pady=20)

# Container de paginação
pagination_frame = tk.Frame(root, bg="#f9f9f9")
pagination_frame.pack(pady=10)

# Botão "Anterior"
prev_button = ttk.Button(pagination_frame, text="« Anterior", command=go_prev)
prev_button.grid(row=0, column=0, padx=5)

# Botões de páginas
page_buttons = []
for i in range(len(pages)):
    btn = ttk.Button(
        pagination_frame,
        text=str(i + 1),
        command=lambda i=i: go_to_page(i)
    )
    btn.grid(row=0, column=i + 1, padx=5)
    page_buttons.append(btn)

# Botão "Próximo"
next_button = ttk.Button(pagination_frame, text="Próximo »", command=go_next)
next_button.grid(row=0, column=len(pages) + 1, padx=5)

# Inicializa o conteúdo
update_content()

# Executa a interface
root.mainloop()
