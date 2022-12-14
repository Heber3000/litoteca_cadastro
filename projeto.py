import tkinter as tk
import sqlite3
import pandas as pd

#Banco de Dados

# conexao = sqlite3.connect('banco_dados_rochas.db')

# c = conexao.cursor()

# c.execute("""CREATE TABLE banco_dados_rochas (
#    nome text,
#    minerais text,
#    local text,
#    coordenadas text,
#   codigo)""")

# conexao.commit()

# conexao.close()

def cadastrar_rochas():
    conexao = sqlite3.connect('banco_dados_rochas.db')
    c = conexao.cursor()

    c.execute("INSERT INTO banco_dados_rochas VALUES (:nome, :minerais, :local, :coordenadas, :codigo)",
              {
                  'nome': nome_entry.get(),
                  'minerais': modaMineral_entry.get(),
                  'local': local_entry.get(),
                  'coordenadas': coordenadas_entry.get(),
                  'codigo': codigo_entry.get()
              })

    conexao.commit()
    conexao.close()

    # apaga os valores da caixa de entrada
    nome_entry.delete(0,"end")
    modaMineral_entry.delete(0,"end")
    local_entry.delete(0,"end")
    coordenadas_entry.delete(0,"end")
    codigo_entry.delete(0,"end")


def exportar_dados():
    conexao = sqlite3.connect('banco_dados_rochas.db')
    c = conexao.cursor()

    c.execute("SELECT *, oid FROM banco_dados_rochas")
    rochas_cadastradas = c.fetchall()

    rochas_cadastradas = pd.DataFrame(rochas_cadastradas,columns=['nome','minerais','local','coordenadas','codigo','Id'])
    rochas_cadastradas.to_excel('banco_dados_rochas.xlsx')

    conexao.commit()
    conexao.close()



# JANELA
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


# Botão Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Amostra de Rochas',command=cadastrar_rochas)
botao_cadastrar.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx= 80)

# Botão Exportar

botao_exportar = tk.Button(text='exportar dados', command=exportar_dados)
botao_exportar.grid(row=8, column=0, columnspan=2, padx=10, pady=10, ipadx= 80)


janela.mainloop()
