import PySimpleGUI as sg

layout = [
    [sg.Button('Começando um novo app', key='b')]
]

Janela = sg.Window('App_para_clima', layout)

while True:
    event, values =  Janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'b':
        Janela.close()

Janela.close()