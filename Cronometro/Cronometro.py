import PySimpleGUI as sg

sg.theme('random')

layout = [
    [sg.VPush()],
    [sg.Text('Tempo')],
    [sg.Button('Começar', key = '-Começo-'), sg.Button('Lap')],
    [sg.VPush()]
]

Janela = sg.Window('Cronometro', 
                   layout,
                   size =(300,300),
                   no_titlebar= True,
                   element_justification = 'center')

while True:
    event, values = Janela.read()
    if event in (sg.WIN_CLOSED, 'Começar'):
        break
    if event == '-Começo-':
       Janela.close()

Janela.close()