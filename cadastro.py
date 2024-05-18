import tkinter as tk
import sqlite3

def cadastrar_cliente():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()

    # Insere os dados na tabela
    c.execute("INSERT INTO clientes VALUES (?, ?, ?, ?)",
              (entry_nome.get(), entry_sobrenome.get(), entry_email.get(), entry_telefone.get()))

    # Salva as mudanças
    conexao.commit()

    # Fecha a conexão
    conexao.close()

# Cria a janela
janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry("330x350")

# Campos de entrada
entry_nome = tk.Entry(janela)
entry_sobrenome = tk.Entry(janela)
entry_email = tk.Entry(janela)
entry_telefone = tk.Entry(janela)

# Botão de cadastro
btn_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_cliente)

# Posicionamento dos widgets
entry_nome.pack()
entry_sobrenome.pack()
entry_email.pack()
entry_telefone.pack()
btn_cadastrar.pack()

# Inicia a aplicação
janela.mainloop()
