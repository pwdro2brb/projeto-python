import PySimpleGUI as sg
from time import time

sg.theme('black')

layout = [
    [sg.Push(),sg.Image('Cronometro/cross.png',size =(10,10), pad = 0, enable_events=True, key = '-Fechar-')],
    [sg.VPush()],
    [sg.Text('Tempo', font = 'Young 50', key = '-TIME-')],
    [   sg.Button('Começar', button_color = ('#FFFFFF','#FF0000'), border_width= 0, key =  '-ComeçoPara-'), 
        sg.Button('Lap',button_color = ('#FFFFFF','#FF0000'), border_width= 0, key = 'LAP')],
    [sg.VPush()]
]

Janela = sg.Window('Cronometro', 
                   layout,
                   size =(300,300),
                   no_titlebar= True,
                   element_justification = 'center')

while True:
    event, values = Janela.read()
    if event in (sg.WIN_CLOSED,  '-Fechar-'):
        break


Janela.close()