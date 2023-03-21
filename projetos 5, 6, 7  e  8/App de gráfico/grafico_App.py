import PySimpleGUI as sg 

layout = [
    []    
]

Janela = sg.Window('App de gráfico', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

Janela.close()