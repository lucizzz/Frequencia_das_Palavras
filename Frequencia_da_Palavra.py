from tkinter import *

def Escrever_Contador(contador):
    resposta.configure(state='normal')   
    resposta.delete('1.0', 'end')                     
    resposta.insert('1.0', contador)           
    resposta.configure(state='disabled')
    
def Funcao():
    contador = 0
    i = 0
    list = texto_entry.get("1.0", "end")
    list = list.lower().strip().split(" ")

    b = palavra_entry.get("1.0", "end") 
    b = b.lower().strip()
    
    if b == "":
        i =  i + 1

    for palavra in list:                             
        if palavra == b:
            contador = contador + 1
    
    if contador !=0:
        if list == ['']:
            lb_nexiste.configure(foreground='red')
            lb_nexiste.place(
                relx=0.40,
                rely=0.58
                )
            lb_nexiste.config(
                text = 'Digite algum texto',
                bg='#dae3f2'
                )
        else:
            lb_nexiste.configure(foreground='#dae3f2')
            Escrever_Contador(contador) 
    else:
        if i == 0:
            lb_nexiste.place(
                relx=0.35,
                rely=0.58
                )
            lb_nexiste.config(
                text = 'A palavra não existe no texto',
                bg='#dae3f2',
                fg='#7c8cb9'
                )
            lb_nexiste.configure(foreground='red')
            Escrever_Contador(contador)
        else:
            lb_nexiste.place(
                relx=0.3,
                rely=0.58
                )
            lb_nexiste.config(
                text = 'Escreva a palavra que deseja ver a frequencia',
                bg='#dae3f2',
                fg='#7c8cb9'
                )
            lb_nexiste.configure(foreground='red')
            Escrever_Contador(contador)
          
root = Tk()
# TELA
root.title("Frequencia das Palavras")
root.geometry('650x600')
root.minsize(width=600, height= 650)
root.resizable(True, True)

#FRAME1 onde esta a caixa do texto, da palavra e o botão:
frame_1 = Frame(root, bg='#dae3f2')
frame_1.place(
    relx=0.02,
    rely=0.02,
    relheight=0.68,
    relwidth=0.96
    )

# CAIXA DE TEXTO onde vai o texto
lb_texto = Label(
    frame_1,
    text='Digite o texto',
    font=('Calibri bold', 15),
    bg='#dae3f2',
    fg='#7c8cb9'
    )
lb_texto.place(
    relx=0.40,
    rely=0.03
    )

texto_entry = Text(frame_1)
texto_entry.place(
    relx=0.05,
    rely=0.11,
    relheight=0.5,
    relwidth=0.9
    )

# CAIXA DE TEXTO 2 onde vai escrever a palavra que quer ver a frequencia
lb_palavra = Label(
    frame_1,
    text='Palavra:',
    font=('Calibri bold', 15),
    bg='#dae3f2',
    fg='#7c8cb9'
    )
lb_palavra.place(
    relx=0.05,
    rely=0.77
    )

palavra_entry = Text(frame_1)
palavra_entry.place(
    relx=0.43,
    rely=0.75,
    relheight=0.1,
    relwidth=0.20
    )

botao_1 = Button(
    frame_1,
    font=('Calibri bold', 13),
    text='Ver!',
    bd='2',
    bg = '#dae3f2',
    fg = '#7c8cb9',
    command=Funcao
    )
botao_1.place(
    relx=0.48,
    rely=0.89,
    relheight=0.080,
    relwidth=0.1
    )

#FRAME2 onde ta a resposta:
frame_2 = Frame(root, bg='#dae3f2')
frame_2.place(
    relx=0.02,
    rely=0.72,
    relwidth=0.96,
    relheight=0.26
    )

lb_resposta = Label(
    frame_2,
    text='A frequencia da palavra é:',
    font=('Calibri bold', 15),
    bg='#dae3f2',
    fg='#7c8cb9'
    )
lb_resposta.place(
    relx=0.05,
    rely=0.37
    )

resposta = Text(
    frame_2,
    font = (None, 15),
    state='disabled'
    )
resposta.place(
    relx=0.43,
    rely=0.30,
    relheight=0.27,
    relwidth=0.20
    )

#CAIXA INVISIVEL para caso não existir a palavra
lb_nexiste = Label(
    frame_2,
    font=('Calibri bold', 15),
    foreground='#dae3f2'
    )

root.mainloop()
