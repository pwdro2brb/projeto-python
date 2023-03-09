import PySimpleGUI as sg

layout = [
    []
]

Janela = sg.Window('Editor de texto', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

Janela.close()