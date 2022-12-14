import tkinter as tk
import sqlite3
import pandas as pd

janela = tk.Tk()
janela.title("Cadastro de Rochas")
janela.geometry('330x350')


















#ROTULOS
label_nome = tk.Label(janela,text='Nome da Rocha')
label_nome.grid(row=0,column=0,padx=10,pady=10)

label_modaMineral = tk.Label(janela,text='Minerais(Moda)')
label_modaMineral.grid(row=1,column=0,padx=10,pady=10)

label_Local = tk.Label(janela,text='Local')
label_Local.grid(row=2,column=0,padx=10,pady=10)

label_coordenadas = tk.Label(janela,text='Coordenadas')
label_coordenadas.grid(row=3,column=0,padx=10,pady=10)

label_codigo = tk.Label(janela,text='Código da Amostra')
label_codigo.grid(row=4,column=0,padx=10,pady=10)


#ENTRADS
nome_entry = tk.Entry(janela, width=35)
nome_entry.grid(row=0,column=2,padx=10,pady=10)

modaMineral_entry = tk.Entry(janela, width=35)
modaMineral_entry.grid(row=1,column=2,padx=10,pady=10)

local_entry = tk.Entry(janela,width=35)
local_entry.grid(row=2,column=2,padx=10,pady=10)

coordenadas_entry = tk.Entry(janela,width=35)
coordenadas_entry.grid(row=3,column=2,padx=10,pady=10)

codigo_entry = tk.Entry(janela,width=35)
codigo_entry.grid(row=4,column=2,padx=10,pady=10)



janela.mainloop()