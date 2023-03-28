import PySimpleGUI as sg

sg.theme('reddit')

play_layout = [
    [sg.Text('Nome do som')]
]

layout_volume = [
    [sg.Slider(range = (0,100))]
    ]

layout = [
    [sg.TabGroup([[sg.Tab('Play',play_layout),sg.Tab('Volume',layout_volume)]])],
]

Janela = sg.Window('Tocador de música', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
Janela.close()