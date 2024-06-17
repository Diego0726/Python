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


Acessar = ctk.CTkButton(master=janela_inicio,text='Acessar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e').place(x=155,y=335)








def janela_function():
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
