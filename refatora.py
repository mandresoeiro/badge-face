import os
from tkinter import Tk, Label, Entry, Button, Frame, PhotoImage, filedialog as fd, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from view import *  # Certifique-se de que a importação seja usada adequadamente

# Definição de cores
def obter_cores():
    return {
        "preto": "#2e2d2b",
        "branco": "#feffff",
        "cinza": "#e5e5e5",
        "verde": "#00a095",
        "letra": "#403d3d",
        "azul": "#003452"
    }

# Configurações da janela principal
def criar_janela():
    janela = Tk()
    janela.title("Sistema de Registro de Alunos")
    janela.geometry("810x535")
    janela.configure(background=cores["branco"])
    janela.resizable(width=False, height=False)
    return janela

# Configuração de Frames
def configurar_frames(janela):
    nb = ttk.Notebook(janela)
    nb.grid(row=0, column=0, pady=0, padx=0, sticky="nsew", columnspan=5)

    tb1 = Frame(nb)
    nb.add(tb1, text='Alunos')

    tb2 = Frame(nb)
    nb.add(tb2, text='Funcionários')

    frame_logo = Frame(tb1, width=850, height=52, bg=cores["azul"])
    frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky="nsew", columnspan=5)

    frame_botoes = Frame(janela, width=100, height=200, bg=cores["branco"], relief="raised")
    frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky="nsew")

    frame_detalhes = Frame(janela, width=800, height=100, bg=cores["branco"], relief="solid")
    frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky="nsew")

    frame_tabela = Frame(janela, width=850, height=200, bg=cores["branco"])
    frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky="nsew", columnspan=5)

    return tb1, frame_logo, frame_botoes, frame_detalhes, frame_tabela

# Funções auxiliares de imagens
def carregar_imagem(caminho, tamanho):
    try:
        img = Image.open(caminho)
        img = img.resize(tamanho)
        return ImageTk.PhotoImage(img)
    except FileNotFoundError:
        messagebox.showerror("Erro", f"Arquivo não encontrado: {caminho}")
        return None

# Configuração de logo e botões principais
def configurar_logo(tb1, frame_logo):
    logo_img = carregar_imagem('./img/image40.png', (40, 40))
    if logo_img:
        Label(tb1, image=logo_img, text="Sistema de Registro de Alunos", compound="left",
              anchor="nw", font=('Verdana 15'), bg=cores["azul"], fg=cores["branco"]).place(x=5, y=0)

    # Exemplo de imagem principal
    principal_img = carregar_imagem('./img/QI.png', (130, 130))
    if principal_img:
        Label(frame_logo, image=principal_img, bg=cores["branco"]).place(x=390, y=10)

# CRUD e outras funcionalidades
def adicionar():
    campos = [e_nome.get(), e_email.get(), e_tel.get(), c_sexo.get(), e_endereco.get(), c_curso.get()]
    if not all(campos):
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    # Adicione lógica de persistência aqui
    limpar_campos()

# Limpar campos após operação
def limpar_campos():
    for campo in [e_nome, e_email, e_tel, c_sexo, e_endereco, c_curso]:
        campo.delete(0, 'end')

# Inicializar aplicação
if __name__ == "__main__":
    cores = obter_cores()
    janela = criar_janela()
    tb1, frame_logo, frame_botoes, frame_detalhes, frame_tabela = configurar_frames(janela)
    configurar_logo(tb1, frame_logo)
    janela.mainloop()
