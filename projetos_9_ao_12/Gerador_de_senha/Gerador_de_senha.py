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