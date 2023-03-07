import PySimpleGUI as sg

layout = [[sg.Text('Começo'),
           sg.Button('cronometragem vai vir', key = '-Começo-')
           ]]

Janela = sg.Window('Cronometro', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-Começo-':
       Janela.close()

Janela.close()