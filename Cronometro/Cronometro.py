import PySimpleGUI as sg
from time import time

sg.theme('black')

layout = [
    [sg.Push(),sg.Image('Cronometro/cross.png',size =(10,10), pad = 0, enable_events=True, key = '-Fechar-')],
    [sg.VPush()],
    [sg.Text('Tempo', font = 'Young 50', key = '-TEMPO-')],
    [   sg.Button('Começar', button_color = ('#FFFFFF','#FF0000'), border_width= 0, key =  '-ComeçoPara-'), 
        sg.Button('Lap',button_color = ('#FFFFFF','#FF0000'), border_width= 0, key = 'LAP')],
    [sg.VPush()]
]

Janela = sg.Window('Cronometro', 
                   layout,
                   size =(300,300),
                   no_titlebar= True,
                   element_justification = 'center')
start_time = 0
active = False

while True:
    event, values = Janela.read(timeout = 10)
    if event in (sg.WIN_CLOSED,  '-Fechar-'):
        break

    if event == '-ComeçoPara-':
        start_time = time()
        active = True

    if active:
        elapsed_time = round(time() - start_time,1)
        Janela['-TEMPO-'].update(elapsed_time)


Janela.close()