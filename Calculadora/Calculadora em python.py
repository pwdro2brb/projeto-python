import PySimpleGUI as sg

layout = [[sg.Button('=')]]

Janela = sg.Window('Calculadora', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

Janela.close() 