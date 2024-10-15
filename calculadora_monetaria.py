from requests import *
from tkinter import *
from tkinter import messagebox

### Pegando as informações da API
url = get('https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL')
url_format = url.json()

dolar_hj = url_format['USDBRL']['bid']
dolar_hj = float(dolar_hj)
dolar_hj = round(dolar_hj,2)

euro_hj = url_format['EURBRL']['bid']
euro_hj = float(euro_hj)
euro_hj = round(euro_hj,2)

#real = float(input('Real: '))
#print('Dólar: {:.2f}'.format(real/dolar_hj))

### Criando a janela
janela_principal = Tk()
janela_principal.title('Calculadora Monetária')
janela_principal.geometry('310x430+400+200')
janela_principal.resizable(False, False)
janela_principal.config(background='#333333')

def converter():
    try:
        if text_real.get() == '' and text_euro.get() == '':
            dolar = float(text_dolar.get())
            
            real = dolar * dolar_hj
            text_real.insert(0,round(real,3))

            euro = real / euro_hj
            text_euro.insert(0,round(euro,3))

        elif text_dolar.get() == '' and text_euro.get() == '':
            real = float(text_real.get())
           
            dolar = real / dolar_hj
            text_dolar.insert(0,round(dolar,3))

            euro = real / euro_hj
            text_euro.insert(0,round(euro,3))

        elif text_real.get() == '' and text_dolar.get() == '':
            euro = float(text_euro.get())

            real = euro * euro_hj
            text_real.insert(0,round(real,3))

            dolar = real / dolar_hj
            text_dolar.insert(0,round(dolar,3))

    except ValueError:
        messagebox.showerror('Atenção', 'Por favor, coloque um valor numérico!')


def apagar():
    text_dolar.delete(0,END)
    text_real.delete(0,END)
    text_euro.delete(0,END)

### Definindo as cores
cinza = '#333333'
amarelo = '#E5AA17'
amarelo_escuro = '#916206'
branco = '#feffff'


### Colocando o logo
logo = PhotoImage(file='coin.png')
figura1 = Label(image=logo, bg=cinza)

### Colocando o limpar
limpar = PhotoImage(file='lixeira.png')
figura2 = Label(image=limpar, bg=cinza)

### Colocando o espaço das moedas
frame_dolar = Frame(janela_principal, borderwidth=1.5, relief='solid', bg=cinza)
label_dolar = Label(janela_principal, text='Dolar', bg=amarelo, fg=branco)
text_dolar = Entry(frame_dolar, width=25, justify='left', font=('',15),relief='solid', bg=cinza, fg=branco)

frame_real = Frame(janela_principal, borderwidth=1.5, relief='solid', bg=cinza)
label_real = Label(janela_principal, text='Real', bg=amarelo, fg=branco)
text_real = Entry(frame_real, width=25, justify='left', font=('',15),relief='solid', bg=cinza, fg=branco)

frame_euro = Frame(janela_principal, borderwidth=1.5, relief='solid', bg=cinza)
label_euro = Label(janela_principal, text='Euro', bg=amarelo, fg=branco)
text_euro = Entry(frame_euro, width=25, justify='left', font=('',15),relief='solid', bg=cinza, fg=branco)

### Colocar o hover no botão de entrar
def on_enter(event):
    entrar['background'] = amarelo_escuro
    entrar['foreground'] = branco

def on_leave(event):
    entrar['background'] = amarelo
    entrar['foreground'] = branco

### Colocando o botão entrar
entrar = Button(janela_principal, text='Converter', command=converter, width=20, justify='center', font=('Ivy 15'), relief='solid', bg=amarelo, fg=branco)
entrar.bind('<Enter>', on_enter)
entrar.bind('<Leave>', on_leave)

### Colocando o botão de limpar
bt_limpar = Button(janela_principal, command=apagar, image=limpar, bd=0, bg=cinza, highlightthickness=0)


figura1.place(x=118, y=40)
frame_dolar.place(x=5, y=145, width=295, height=55)
label_dolar.place(x=8, y=135)
text_dolar.place(x=5, y=15)

frame_real.place(x=5, y=215, width=295, height=55)
label_real.place(x=8, y=205)
text_real.place(x=5, y=15)

frame_euro.place(x=5, y=286, width=295, height=55)
label_euro.place(x=8, y=276)
text_euro.place(x=5, y=15)

entrar.place(x=5, y=370)
bt_limpar.place(x=250, y=365)

janela_principal.mainloop()

