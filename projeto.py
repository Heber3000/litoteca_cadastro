import tkinter as tk
import sqlite3
import pandas as pd

janela = tk.Tk()
janela.title("Cadastro de Rochas")
janela.geometry('330x350')


















#Label

nome_label = tk.Label(janela,text='Nome da Rochas')
nome_label.grid(row=0,column=0,padx=10,pady=10)

modaMineral_label = tk.Label(janela,text='Moda Mineral')
modaMineral_label.grid(row=1,column=0,padx=10,pady=10)

local_label = tk.Label(janela,text='Local')
local_label.grid(row=2,column=0,padx=10,pady=10)

coordenadas = tk.Label(janela,text='Coordenadas')
coordenadas.grid(row=3,column=0,padx=10,pady=10)

#ENTRADS

nome_entry = tk.Entry(janela, width=35)
nome_entry.grid(row=0,column=2,padx=10,pady=10)

modaMineral_entry = tk.Entry(janela, width=35)
nome_entry.grid(row=0,column=2,padx=10,pady=10)