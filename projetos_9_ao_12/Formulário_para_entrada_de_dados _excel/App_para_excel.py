import PySimpleGUI as sg

sg.theme('DarkTeal4')

layout = [
    [sg.Text('Começando alguma coisa')],
    [sg.Button('Sair', key='sair')]
]

Janela = sg.Window('App para receber dados daqui e enviar para o excel', layout)


while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED():
        break
    if event == 'sair':
        Janela.close9

Janela.closed()