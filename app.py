from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

# importando pillow
from PIL import ImageTk, Image

# # tk calendar
# from tkcalendar import Calendar, DateEntry
# from datetime import date
    
# chamando a view
from view import *

def obter_cores():
    return {
        "preto": "#2e2d2b",
        "branco": "#feffff",
        "cinza": "#e5e5e5",
        "verde": "#00a095",
        "letra": "#403d3d",
        "azul": "#003452"
    }

# # cores
# co0 = "#2e2d2b"  # Preta
# co1 = "#feffff"  # Branca
# co2 = "#e5e5e5"  # grey
# co3 = "#00a095"  # Verde
# co4 = "#403d3d"   # letra
# co6 = "#003452"   # azul


# Criando janela
janela = Tk()
janela.title("")
janela.geometry('810x535')
janela.configure(background=obter_cores()["branco"])
janela.resizable(width=FALSE, height=FALSE)
nb = ttk.Notebook(janela)
nb.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
tb1 = Frame(janela)
nb.add(tb1, text='Alunos')
tb2 = Frame(janela)
nb.add(tb2, text='Funcionarios')

frame_logo = Frame(tb1, width=850, height=52, bg = obter_cores()["azul"])
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW, columnspan=5)

frame_botoes = Frame(janela, width=100, height=200, bg = obter_cores()["branco"], relief=RAISED)



frame_botoes.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_detalhes = Frame(janela, width=800, height=100, bg = obter_cores()["branco"], relief=SOLID)
frame_detalhes.grid(row=1, column=1, pady=1, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg = obter_cores()["branco"])
frame_tabela.grid(row=3, column=0, pady=0, padx=10, sticky=NSEW, columnspan=5)


# Trabalhando no frame Logo ----------------------------
global imagem, imagem_string, l_imagem

app_lg = Image.open('./img/logo.webp')
app_lg = app_lg.resize((40, 40))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(tb1, image=app_lg, text=" Sistema de Registro de Alunos",
                 width=850, compound=LEFT, anchor=NW, font=('Verdana 15'), bg = obter_cores()["azul"], fg = obter_cores()["branco"])
app_logo.place(x=5, y=0)


# abrindo a imagem
imagem = Image.open('./img/logo.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_detalhes, image=imagem, bg = obter_cores()["branco"], fg= obter_cores()["verde"])
l_imagem.place(x=390, y=10)

# ------------- Criando funcoes para CRUD ---------------

# funcao criar


def adicionar():
    """
    Função para adicionar um registro a partir dos dados de entrada no formulário.
    """
    global imagem, imagem_string, l_imagem

    # Obtendo os valores do formulário
    nome = e_nome.get().strip()  # Remove espaços em branco extras
    email = e_email.get().strip()
    tel = e_tel.get().strip()
    sexo = c_sexo.get().strip()
    # data = data_nascimento.get().strip()  # Certifique-se de descomentar se necessário
    endereco = e_endereco.get().strip()
    curso = c_curso.get().strip()
    imagem_string = ""  # assign an empty string to imagem_string
    img = imagem_string

    # Validação básica dos campos obrigatórios
    if not nome or not email or not tel or not sexo or not endereco or not curso:
        print("Todos os campos devem ser preenchidos!")  # Mensagem de erro (substitua por uma mensagem gráfica, se necessário)
        return

    # Validação adicional de e-mail (opcional)
    if "@" not in email or "." not in email.split("@")[-1]:
        print("O e-mail fornecido é inválido!")  # Mensagem de erro (substitua por uma mensagem gráfica, se necessário)
        return

    # Adicionando registro ou salvando informações (adicione a lógica apropriada aqui)
    try:
        novo_registro = {
            "nome": nome,
            "email": email,
            "telefone": tel,
            "sexo": sexo,
            # "data_nascimento": data,  # Inclua se necessário
            "endereco": endereco,
            "curso": curso,
            "imagem": img
        }
        print("Registro adicionado com sucesso:", novo_registro)  # Mensagem de sucesso (substitua por exibição gráfica, se necessário)

        # Resetando os campos após adicionar o registro
        e_nome.delete(0, 'end')
        e_email.delete(0, 'end')
        e_tel.delete(0, 'end')
        c_sexo.set('')  # Reseta o combobox
        e_endereco.delete(0, 'end')
        c_curso.set('')
        imagem = None
        imagem_string = None
        l_imagem = None  # Atualize o estado da imagem se necessário

    except Exception as e:
        print(f"Erro ao adicionar registro: {e}")  # Mensagem de erro (substitua por uma mensagem gráfica, se necessário)


# funcao procurar
def procurar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # search for a student by id
    dados = registration_system.search_student(id_aluno)

    # limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    # data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # inserindo os valores
    e_nome.insert(END, dados[1])
    e_email.insert(END, dados[2])
    e_tel.insert(END, dados[3])
    c_sexo.insert(END, dados[4])
    # data_nascimento.insert(END, dados[5])
    e_endereco.insert(END, dados[6])
    c_curso.insert(END, dados[7])
    # img = imagem_string

    imagem = dados[8]
    imagem_string = imagem

    # abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

l_imagem = Label(frame_detalhes, image=imagem, bg = obter_cores()["branco"], fg= obter_cores()["verde"])
l_imagem.place(x=390, y=10)


# funcao atualizar
def atualizar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # obtendo os valores
    nome = e_nome.get()
    email = e_email.get()
    tel = e_tel.get()
    sexo = c_sexo.get()
    # data = data_nascimento.get()
    endereco = e_endereco.get()
    curso = c_curso.get()
    img = imagem_string

    lista = [nome, email, tel, sexo, data, endereco, curso, img, id_aluno]

    # Verificando caso algum campo esteja vazio ou nao\\\\/
    for i in lista:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

    # update the student
    registration_system.update_student(lista)

    # limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    # data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    # abrindo a imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_detalhes, image=imagem, bg = obter_cores()["branco"], fg= obter_cores()["verde"])
    l_imagem.place(x=390, y=10)

    # mostrando os valores na Tabela
    mostrar_alunos()


# funcao deletar
def deletar():
    global imagem, imagem_string, l_imagem

    # obtendo o id
    id_aluno = int(e_procurar.get())

    # delete a student by id
    registration_system.delete_student(id_aluno)

    # limpando os campos de entradas
    e_nome.delete(0, END)
    e_email.delete(0, END)
    e_tel.delete(0, END)
    c_sexo.delete(0, END)
    # data_nascimento.delete(0, END)
    e_endereco.delete(0, END)
    c_curso.delete(0, END)

    e_procurar.delete(0, END)

    # abrindo a imagem
    imagem = Image.open('logo.png')
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frame_detalhes, image=imagem, bg = obter_cores()["branco"], fg= obter_cores()["verde"])
    l_imagem.place(x=390, y=10)

    # mostrando os valores na Tabela
    mostrar_alunos()


# Criando os campos de entrada --------------------------

# criando campos de entrada
l_nome = Label(frame_detalhes, text="Nome *", height=1, anchor=NW, font=('Ivy 10'), bg=obter_cores()["branco"], fg=obter_cores()["preto"])
l_nome.place(x=4, y=10)
e_nome = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_nome.place(x=7, y=40)

l_email = Label(frame_detalhes, text="Email *", height=1, anchor=NW, font=('Ivy 10'), bg=obter_cores()["branco"], fg=obter_cores()["preto"])
l_email.place(x=4, y=70)
e_email = Entry(frame_detalhes, width=30, justify='left', relief='solid')
e_email.place(x=7, y=100)

l_tel = Label(frame_detalhes, text="Telefone *", height=1,
              anchor=NW, font=('Ivy 10'), bg = obter_cores()["branco"], fg = obter_cores()["preto"])

l_tel.place(x=4, y=130)
e_tel = Entry(frame_detalhes, width=15, justify='left', relief='solid')
e_tel.place(x=7, y=160)

# selecao de sexo
l_sexo = Label(frame_detalhes, text="Sexo *", height=1,
               anchor=NW, font=('Ivy 10'), bg = obter_cores()["branco"], fg = obter_cores()["preto"])

l_sexo.place(x=127, y=130)
c_sexo = ttk.Combobox(frame_detalhes, width=7,
                      font=('Ivy 8 bold'), justify='center')
c_sexo['values'] = ('M', 'F')
c_sexo.place(x=130, y=160)

# l_data_nascimento = Label(frame_detalhes, text="Data de nascimento *",
#                           height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
# l_data_nascimento.place(x=220, y=10)
# data_nascimento = DateEntry(frame_detalhes, width=18, justify='center',
#                             background='darkblue', foreground='white', borderwidth=2, year=2023)
# data_nascimento.place(x=224, y=40)

l_endereco = Label(frame_detalhes, text="Matricula *", height=1, anchor=NW, font=('Ivy 10'), bg = obter_cores()["branco"], fg = obter_cores()["verde"])


l_endereco.place(x=220, y=70)
e_endereco = Entry(frame_detalhes, width=20, justify='left', relief='solid')
e_endereco.place(x=224, y=100)

# Pegando as Turmas
cursos = ['MED1', 'MED2', 'MED3', 'MED4', 'MED5',
          'EXATAS', 'HUMANAS', 'NATUREZA', 'REDAÇÃO']
curso = []

for i in cursos:
    curso.append(i)

l_curso = Label(frame_detalhes, text="Curso *", height=1,
                anchor=NW, font=('Ivy 10'), bg = obter_cores()["branco"], fg = obter_cores()["verde"])



l_curso.place(x=220, y=130)
c_curso = ttk.Combobox(frame_detalhes, width=20, font=('Ivy 8 bold'))
c_curso['values'] = (curso)
c_curso.place(x=224, y=160)


# funcaao para escolher imagem

def escolher_imagem():
    global imagem, imagem_string, l_imagem

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # abrindo a imagem
    imagem = Image.open(imagem)
    imagem = imagem.resize((130, 130))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frame_detalhes, image=imagem, bg = obter_cores()["branco"], fg= obter_cores()["verde"])


    l_imagem.place(x=390, y=10)

    botao_carregar['text'] = 'Trocar de foto'


botao_carregar = Button(frame_detalhes, command=escolher_imagem, text="Carregar Foto".upper(
), width=20, compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 7 bold'), bg = obter_cores()["branco"], fg = obter_cores()["preto"])

botao_carregar.place(x=390, y=160)


# Tabela Alunos
def mostrar_alunos():

    # creating a treeview with dual scrollbars
    list_header = ['id', 'Nome', 'email',  'Telefone',
                   'sexo', 'registro', 'Curso']

    # view all students
    df_list = registration_system.view_all_students()

    global tree_curso

    tree_aluno = ttk.Treeview(
        frame_tabela, selectmode="extended", columns=list_header, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical",
                        command=tree_aluno.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal",
                        command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "center", "center",
          "center", "center", "center", "center"]
    h = [40, 200, 180, 70, 70, 120, 100, 100]
    n = 0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        # adjust the column's width to the header string
        tree_aluno.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in df_list:
        tree_aluno.insert('', 'end', values=item)


# Procurar aluno -----------
frame_procurar = Frame(frame_botoes, width=40, height=50, bg=obter_cores()["branco"], relief=RAISED)
frame_procurar.grid(row=0, column=0, pady=10, padx=10, sticky=NSEW)

l_nome = Label(frame_procurar, text="Procurar aluno [ Entra ID ]", height=1, anchor=NW, font=('Ivy 10'), bg = obter_cores()["branco"], fg = obter_cores()["verde"])


l_nome.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)
e_procurar = Entry(frame_procurar, width=5, justify='center',
                   relief="solid", font=('Ivy 10'))
e_procurar.grid(row=1, column=0, pady=10, padx=0, sticky=NSEW)

botao_procurar = Button(frame_procurar, command=procurar, anchor=CENTER,
                        text="Procurar", width=9, overrelief=RIDGE,  font=('ivy 7 bold'), bg = obter_cores()["branco"], fg = obter_cores()["verde"])

# Botoes --------------------

app_img_adicionar = Image.open('add.png')
app_img_adicionar = app_img_adicionar.resize((25, 25))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_botoes, command=adicionar, image=app_img_adicionar, text=" Adicionar",
                       width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg = obter_cores()["branco"], fg=obter_cores()["verde"])
app_adicionar.grid(row=1, column=0, pady=5, padx=10, sticky=W)

app_img_atualizar = Image.open('update.png')
app_img_atualizar = app_img_atualizar.resize((25, 25))
app_img_atualizar = ImageTk.PhotoImage(app_img_atualizar)
app_atualizar = Button(frame_botoes, command=atualizar, image=app_img_atualizar, text=" Atualizar",
                       width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg = obter_cores()["branco"], fg = obter_cores()["verde"])

app_atualizar.grid(row=2, column=0, pady=5, padx=10, sticky=W)

app_img_deletar = Image.open('./img/excluir.png')
app_img_deletar = app_img_deletar.resize((25, 25))
app_img_deletar = ImageTk.PhotoImage(app_img_deletar)
app_deletar = Button(frame_botoes, command=deletar, image=app_img_deletar, text=" Deletar",
                     width=100, compound=LEFT, relief=GROOVE, overrelief=RIDGE, font=('Ivy 11'), bg = obter_cores()["branco"], fg = obter_cores()["preto"])

app_deletar.grid(row=3, column=0, pady=5, padx=10, sticky=W)


# linha separatoria ---------------------------------------------------

l_linha = Label(frame_botoes, relief=GROOVE, text='h', width=1, height=123, anchor=NW, font=('Ivy 1'), bg = obter_cores()["branco"], fg = obter_cores()["preto"])
l_linha.place(x=240, y=15)


# ver a tabela de estudantes
mostrar_alunos()

janela.mainloop()


