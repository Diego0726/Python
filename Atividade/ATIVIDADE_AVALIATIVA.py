import customtkinter as ctk
import tkinter
from tkinter import *
from tkinter import messagebox


############## CONFIGURAÇÃO DA JANELAS ###############
janela_inicio = ctk.CTk()
janela_inicio.title('Automação Residencial')
janela_inicio.geometry('450x500')
janela_inicio.resizable(height=False, width=False)
ctk.set_appearance_mode('System')


def add_numero_precionado(num):
    current_text = Entry.get()
    Entry.delete(0,ctk.END)
    Entry.insert(0, current_text + str(num))

def limpar_entrada():
    Entry.delete(0,ctk.END)

def comando_limpar(text):
    return lambda: add_numero_precionado(text) if text !='C' else limpar_entrada()


Entry = ctk.CTkEntry(janela_inicio, width=300, height=50)
Entry.grid(row=0, column=0, columnspan=3,pady=55,padx=79)


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
    {'text': 'C', 'row': 4, 'column': 0, 'command': limpar_entrada}

]

for btn in teclado:
    btn = ctk.CTkButton(janela_inicio,text=btn['text'], command=comando_limpar(btn['text'])) 
    btn.grid(row=btn['text'], column=btn['column'],padx=56,pady=80,stick='nsew')

for i in range(5):
    janela_inicio.grid_rowconfigure(i, weight=1)
for i in range(3):
    janela_inicio.grid_columnconfigure(i, weight=1)




Acessar = ctk.CTkButton(janela_inicio,text='Acessar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e',command=lambda: open_janela_function())


Acessar.place(x=155,y=400)








def open_janela_function():
    janela_function = ctk.CTkToplevel()
    janela_function.title('Automação Residencial')
    janela_function.geometry('450x500')
    janela_function.maxsize(width=724, height=540)
    janela_function.minsize(width=150, height=150)
    ctk.set_appearance_mode('System')

############## COMPONENTES (LAYOUT) #################
#Lampada
    botao1 = ctk.CTkButton(master=janela_function,text='Ligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
    botao2 = ctk.CTkButton(master=janela_function,text='Desligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
#Ventilador
    botao3 = ctk.CTkButton(master=janela_function,text='Ligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
    botao4 = ctk.CTkButton(master=janela_function,text='Desligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
#Fechadura
    botao5 = ctk.CTkButton(master=janela_function,text='Abrir',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
    botao6 = ctk.CTkButton(master=janela_function,text='Fechar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
    botao1.pack(pady=5)
    botao2.pack(pady=5)
    botao3.pack(pady=5)
    botao4.pack(pady=5)
    botao5.pack(pady=5)
    botao6.pack(pady=5)

############### POSIÇÃO DOS COMPONETES (LAYOUT) #################









janela_inicio.mainloop()
