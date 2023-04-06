import random
import string
import PySimpleGUI as sg

Maiúsculo = random.sample(string.ascii_uppercase, 2)
Minúsculo = random.sample(string.ascii_lowercase, 2)
digitos = random.sample(string.digits, 2)
simbolos = random.sample(string.punctuation, 2)

total = Maiúsculo+Minúsculo+digitos+simbolos
total = random.sample(total, len(total))
total = ''.join(total)
print(total)

sg.theme('LightBlue2')
sg.set_options(font='Verdana 15')

layout = [
    [sg.Text('Crie senhas com o app, escolhas quantos carcteres de cada tipo abaixo terá na senha que será criada')],
    [sg.Text('Quantidade Maiúsculas'), sg.Input(size = 15)],
    [sg.Text('Quantidade Minúsculas'), sg.Input(size = 15)],
    [sg.Text('Quantidade Números   '), sg.Input(size = 15)],
    [sg.Text('Quantidade Simbolos   '), sg.Input(size = 15)],
    [sg.Button('Ok'), sg.Button('Cancelar')],
    [sg.Text('Senha'), sg.Multiline(size = 15, no_scrollbar=True, disabled=True)]
]

janela = sg.Window('Gerador de senha', layout)

while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
janela.close()