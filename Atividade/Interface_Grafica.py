# ALUNO: DIEGO OLIVEIRA BARRETO
# Escute essa musica enquanto avalia o projeto por favor https://youtu.be/L_jWHffIx5E?si=HuTemvz0n_k9pvnV



import customtkinter as ctk
from tkinter import *
import serial


try:
    arduino = serial.Serial('COM3', 9600)
except serial.SerialException as e:
    print(f"Erro ao Conectar com o Arduino: {e}")

############## CONFIGURAÇÃO DA JANELA_INICIO ###############
janela_inicio = ctk.CTk()
janela_inicio.title('Automação Residencial')
janela_inicio.geometry('450x500')
janela_inicio.resizable(height=False, width=False)
ctk.set_appearance_mode('System')

# Função para adicionar o número pressionado à entrada
def add_numero_precionado(num):
    current_text = entry.get()
    entry.delete(0, ctk.END)
    entry.insert(0, current_text + str(num))

# Função para limpar a entrada
def limpar_entrada():
    entry.delete(0, ctk.END)

# Função auxiliar para criar o comando correto
def comando_limpar(text):
    return lambda: add_numero_precionado(text) if text != 'Apagar' else limpar_entrada()


############# Função para abrir a nova janela ###############
def open_janela_function():
    janela_function = ctk.CTkToplevel()
    janela_function.title('Automação Residencial')
    janela_function.geometry('450x500')
    janela_function.resizable(width=False, height=False)
    ctk.set_appearance_mode('System')

    

    #Area dos Textos de Estatus (LAYOUT)
    
    lampada_label = ctk.CTkLabel(master=janela_function, text='Estado da Lâmpada: Desligada', text_color='#cac0d1', width=250, height=50)
    lampada_label.place(x=100, y=50)
    
    ventilador_label = ctk.CTkLabel(master=janela_function, text='Estado do Ventilador: Desligado', text_color='#cac0d1', width=250, height=50)
    ventilador_label.place(x=100, y=200)
    
    fechadura_label = ctk.CTkLabel(master=janela_function, text='Estado da Fechadura: Fechada', text_color='#cac0d1', width=250, height=50)
    fechadura_label.place(x=100, y=350)


    #Funções dos Botões

    def Texto_lampada_ligar():
        botao1.configure(text="Ligar")
        lampada_label.configure(text='Estado da Lâmpada: Ligada')

    def Texto_lampada_desligar():
        botao2.configure(text="Desligar")
        lampada_label.configure(text='Estado da Lâmpada: Desligada')

    def Texto_ventilador_ligar():
        botao3.configure(text="Ligar")
        ventilador_label.configure(text='Estado do Ventilador: Ligado')

    def Texto_ventilador_desligar():
        botao4.configure(text="Desligar")
        ventilador_label.configure(text='Estado do Ventilador: Desligado')

    def Texto_fechadura_abrir():
        botao5.configure(text=" Abrir")
        fechadura_label.configure(text='Estado da Fechadura: Aberta')

    def Texto_fechadura_fechar():
        botao6.configure(text="Fechar")
        fechadura_label.configure(text='Estado da Fechadura: Fechada')

    

    # Botão Lampada (LAYOUT)
    botao1 = ctk.CTkButton(master=janela_function, text='Ligar', text_color='#cac0d1', width=150, height=50, fg_color='#17268f',
                           hover_color='#806f7e', command=Texto_lampada_ligar)
    botao2 = ctk.CTkButton(master=janela_function, text='Desligar', text_color='#cac0d1', width=150, height=50, fg_color='#17268f',
                           hover_color='#806f7e', command=Texto_lampada_desligar)
    
    
    
    # Botão Ventilador (LAYOUT)
    botao3 = ctk.CTkButton(master=janela_function, text='Ligar', text_color='#cac0d1', width=150, height=50, fg_color='#17268f',
                           hover_color='#806f7e', command=Texto_ventilador_ligar)
    botao4 = ctk.CTkButton(master=janela_function, text='Desligar', text_color='#cac0d1', width=150, height=50, fg_color='#17268f',
                           hover_color='#806f7e', command=Texto_ventilador_desligar)
    
   
    # Botão Fechadura (LAYOUT)
    botao5 = ctk.CTkButton(master=janela_function, text='Abrir', text_color='#cac0d1', width=150, height=50, fg_color='#17268f',
                           hover_color='#806f7e', command=Texto_fechadura_abrir)
    botao6 = ctk.CTkButton(master=janela_function, text='Fechar', text_color='#cac0d1', width=150, height=50, fg_color='#17268f',
                           hover_color='#806f7e', command=Texto_fechadura_fechar)

    #Posicionamento dos Botões

    botao1.place(x=50,y=100)
    botao2.place(x=250,y=100)
    botao3.place(x=50,y=250)
    botao4.place(x=250,y=250)
    botao5.place(x=50,y=400)
    botao6.place(x=250,y=400)

    
    


# Criação de um Painel para mostrar os números pressionados (LAYOUT)
entry = ctk.CTkEntry(janela_inicio, width=450, height=50,show='*', justify='center',font=('Arial', 25))
entry.grid(row=0, column=0, columnspan=3, pady=10, padx=79)

# Definindo Teclado Numerico (LAYOUT)
teclado = [
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
    {'text': 'Apagar', 'row': 4, 'column': 0}
]

# Cria os botões e adiciona-os à grade (LAYOUT)
for btn_info in teclado:
    btn = ctk.CTkButton(janela_inicio, text=btn_info['text'],width=50,height=50,fg_color='#17268f',
                        hover_color='#806f7e',text_color='#cac0d1', command=comando_limpar(btn_info['text']))
    
    btn.grid(row=btn_info['row'], column=btn_info['column'],padx=5, pady=5, sticky='nsew')

 

# Ajusta a configuração da grade para expandir os botões uniformemente
for i in range(9):
    janela_inicio.grid_rowconfigure(i, weight=1)
for i in range(6):
    janela_inicio.grid_columnconfigure(i, weight=1)

# Botão de Acessar (LAYOUT)
Acessar = ctk.CTkButton(janela_inicio, text='Acessar', text_color='#cac0d1', width=180, height=60, fg_color='#17268f',
                        hover_color='#DB0006', command=open_janela_function)


Acessar.place(x=135, y=420)



janela_inicio.mainloop()
