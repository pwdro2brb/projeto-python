import PySimpleGUI as sg

import base64
from io import BytesIO
from PIL import Image

def base64_image_import(path):
    image = Image.open(path)
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    b64 = base64.b64encode(buffer.getvalue())
    return b64

sg.theme('reddit')

play_layout = [
    [sg.VPush()],
    [sg.Push(),sg.Text('Nome do som', font = 'Arial 20'),sg.Push],
    [sg.VPush()],
    [
        sg.Push(),
        sg.Button(image_data = base64_image_import('projetos_9_ao_12\Tocador_de_música\Play.png'), button_color = 'white',border_width = 0),
        sg.Text(' '),
        sg.Button(image_data = base64_image_import('projetos_9_ao_12\Tocador_de_música\Pausar.png'), button_color = 'white',border_width = 0),
        sg.Push(),
    ],
    [sg.VPush()],
    [sg.Progress(100, size=(50,50))],
]

volume_layout = [
    [sg.VPush()],
    [sg.Push(),sg.Slider(range = (0,100), default_value = 100, orientation='h', key='Volume'),sg.Push()],
    [sg.VPush()],
    ]

layout = [
    [sg.TabGroup([[sg.Tab('Play',play_layout),sg.Tab('Volume',volume_layout)]])],
]

Janela = sg.Window('toca_música', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
Janela.close()