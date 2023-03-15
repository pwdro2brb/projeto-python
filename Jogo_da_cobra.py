import PySimpleGUI as sg

layout = [
    []
]

Janela = sg.Window('Jogo da cobra', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED():
        break

Janela.read()