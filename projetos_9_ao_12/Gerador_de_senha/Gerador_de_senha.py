import random
import string

Maiúsculo = random.sample(string.ascii_uppercase, 2)
Minúsculo = random.sample(string.ascii_lowercase, 2)
digitos = random.sample(string.digits, 2)
simbolos = random.sample(string.punctuation, 2)

total = Maiúsculo+Minúsculo+digitos+simbolos
total = random.sample(total, len(total))
total = ''.join(total)
print(total)

import PySimpleGUI as sg

layout = [
    [sg.Text('Começando a codificação                                                      ')]
]

janela = sg.Window('Gerador de senha', layout)

while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
janela.close()