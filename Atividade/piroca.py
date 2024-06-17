import customtkinter as ctk

# Função para adicionar o número pressionado à entrada
def on_number_press(num):
    current_text = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(0, current_text + str(num))

# Função para limpar a entrada
def clear_entry():
    entry.delete(0, ctk.END)

# Inicializa a biblioteca CTk
ctk.set_appearance_mode("light")  # Modo de aparência: "light" ou "dark"
ctk.set_default_color_theme("blue")  # Tema de cor: "blue", "green", "dark-blue"

# Cria a janela principal
root = ctk.CTk()
root.title("Teclado Numérico")
root.geometry("300x400")

# Cria uma entrada para mostrar os números pressionados
entry = ctk.CTkEntry(root, width=200, justify='right')
entry.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

# Define os botões numerados de 0 a 9 e o botão de limpar
buttons = [
    {'text': '1', 'row': 1, 'column': 0},
    {'text': '2', 'row': 1, 'column': 1},
    {'text': '3', 'row': 1, 'column': 2},
    {'text': '4', 'row': 2, 'column': 0},
    {'text': '5', 'row': 2, 'column': 1},
    {'text': '6', 'row': 2, 'column': 2},
    {'text': '7', 'row': 3, 'column': 0},
    {'text': '8', 'row': 3, 'column': 1},
    {'text': '9', 'row': 3, 'column': 2},
    {'text': '0', 'row': 4, 'column': 1},
    {'text': 'C', 'row': 4, 'column': 0, 'command': clear_entry}
]

# Cria os botões e adiciona-os à grade
for btn_info in buttons:
    btn = ctk.CTkButton(root, text=btn_info['text'], command=lambda b=btn_info['text']: on_number_press(b) if b != 'C' else clear_entry())
    btn.grid(row=btn_info['row'], column=btn_info['column'], padx=10, pady=10, sticky='nsew')

# Ajusta a configuração da grade para expandir os botões uniformemente
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

# Rodando a aplicação
root.mainloop()
