import customtkinter as ctk
import tkinter
from tkinter import *
from tkinter import messagebox


############## CONFIGURAÇÃO DA JANELA ###############
janela = ctk.CTk('#080808')
janela.title('Automação Residencial')
janela.geometry('450x500')
ctk.set_appearance_mode('System')


############## COMPONENTES (LAYOUT) #################
imagem = PhotoImage (file="images\Fechadura.png")
imagem = imagem.subsample(3,3)
figural = Label(image=imagem, bg='#080808')



#Lampada
botao1 = ctk.CTkButton(janela,text='Ligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
botao2 = ctk.CTkButton(janela,text='Desligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
#Ventilador
botao3 = ctk.CTkButton(janela,text='Ligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
botao4 = ctk.CTkButton(janela,text='Desligar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
#Fechadura
botao5 = ctk.CTkButton(janela,text='Abrir',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
botao6 = ctk.CTkButton(janela,text='Fechar',text_color='#cac0d1',width=150,height=50,fg_color='#17268f',
                      hover_color='#806f7e')
botao1.pack(pady=5)
botao2.pack(pady=5)
botao3.pack(pady=5)
botao4.pack(pady=5)
botao5.pack(pady=5)
botao6.pack(pady=5)

############### POSIÇÃO DOS COMPONETES (LAYOUT) #################









janela.mainloop()
