#bibliotecas
from tkinter import *
import tkinter
from datetime import datetime 
from PIL import Image,ImageTk

#Cores

cor1 = "#000000" #preta
cor2 = "#fafcff" #branca

fundo = cor1
cor = cor2

#Icon

""" app_img = Image.open('clockicon.png')
app_img = app_img.resize((20,20))
app_img = ImageTk.PhotoImage(app_img)
 """
#janela

janela = Tk()
janela.title("Relógio Digital")
janela.geometry("440x200")
janela.configure(bg = cor1)
janela.resizable(width = FALSE, height = FALSE)

#horas
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%b")
    ano = tempo.strftime("%Y")
     
    l1.config(text = hora)
    l1.after(200, relogio)
    l2.config(text = dia_semana + "   " + str(dia)
              + "/" + str(mes) + "/" + str(ano))
#LABEL
l1 = Label(janela, text="",font=("Arial 80"),bg=fundo,fg=cor)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="",font=("Arial 20"),bg=fundo,fg=cor)
l2.grid(row=1, column=0, sticky=NW, padx=5)

relogio()
janela.mainloop()




