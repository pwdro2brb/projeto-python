import PySimpleGUI as sg

layout = [
    [sg.Button('Começo')],
    [sg.Text('Começando algo')]
]

Janela = sg.Window('Tocador de música', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
Janela.close()