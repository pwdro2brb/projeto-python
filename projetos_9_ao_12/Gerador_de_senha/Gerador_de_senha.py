import random
import string
import PySimpleGUI as sg


sg.theme('LightBlue2')
sg.set_options(font='Verdana 15')

layout = [
    [sg.Text('Crie senhas com o app, escolhas quantos carcteres de cada tipo abaixo terá na senha que será criada')],
    [sg.Text('Quantidade Maiúsculas'), sg.Input(size = 15, key='-Maiúsculo-')],
    [sg.Text('Quantidade Minúsculas'), sg.Input(size = 15, key='-Minúsculo-')],
    [sg.Text('Quantidade Números   '), sg.Input(size = 15, key='-Digito-')],
    [sg.Text('Quantidade Simbolos   '), sg.Input(size = 15, key='-Simbolo-' )],
    [sg.Button('Ok'), sg.Button('Cancelar')],
    [sg.Text('Senha'), sg.Multiline(size = 15, no_scrollbar=True, disabled=True, key='-Passar-')]
]

janela = sg.Window('Gerador de senha', layout)

while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break
    if event == 'Ok': 
        try:      
            voce_maior = int(values['-Maiúsculo-'])
            Maiúsculo = random.sample(string.ascii_uppercase, voce_maior)
            voce_menor = int(values['-Minúsculo-'])
            Minúsculo = random.sample(string.ascii_lowercase, voce_menor)
            voce_núm = int(values['-Digito-'])
            digitos = random.sample(string.digits, voce_núm)
            voce_simb = int(values['-Simbolo-'])
            simbolos = random.sample(string.punctuation, voce_simb)

            total = Maiúsculo+Minúsculo+digitos+simbolos
            total = random.sample(total, len(total))
            total = ''.join(total)
            janela['-Passar-'].update(total)
        except ValueError:
           janela['-Passar-'].update('Sem um número válido') 
janela.close()