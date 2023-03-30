import PySimpleGUI as sg

import base64
from io import BytesIO
from PIL import Image

from pygame import mixer, time
mixer.init()
clock = time.Clock()

def base64_image_import(path):
    image = Image.open(path)
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    b64 = base64.b64encode(buffer.getvalue())
    return b64

#Importa o som
path = sg.popup_get_file('Open', no_window=True)
nome_som = path.split('/')[-1].split('.')[0]
song = mixer.Sound(path)

#temporizador
Tamanho_som = int(song.get_length())
time_since_start = 0
pause_amount = 0
playing = False

sg.theme('reddit')

play_layout = [
    [sg.VPush()],
    [sg.Text(nome_som, font = 'Arial 20')],
    [sg.VPush()],
    [
        sg.Push(),
        sg.Button(image_data = base64_image_import('projetos_9_ao_12\Tocador_de_música\Play.png'), button_color = 'white',border_width = 0, key='-play-'),
        sg.Text(' '),
        sg.Button(image_data = base64_image_import('projetos_9_ao_12\Tocador_de_música\Pausar.png'), button_color = 'white',border_width = 0, key='-pausa-'),
        sg.Push(),
    ],
    [sg.VPush()],
    [sg.Progress(Tamanho_som, size=(50,50), key='-progresso-')],
]

volume_layout = [
    [sg.VPush()],
    [sg.Push(),sg.Slider(range = (0, 100), default_value = 100, orientation='h', key='-Volume-'),sg.Push()],
    [sg.VPush()],
    ]

layout = [
    [sg.TabGroup([[sg.Tab('Play',play_layout),sg.Tab('Volume',volume_layout)]])],
]

Janela = sg.Window('toca_música', layout)

while True:
    event, values = Janela.read(timeout=1)
    if event == sg.WIN_CLOSED:
        break
    
    if playing:
        time_since_start = time.get_ticks()
        Janela['-progresso-'].update((time_since_start - pause_amount) // 1000)
    
    if event == '-play-':
        playing = True
        pause_amount += time.get_ticks() - time_since_start
        if mixer.get_busy() == False:   
            song.play()
        else:
            mixer.unpause()
            
    if event == '-pausa-':
        mixer.pause()
        playing = False
    song.set_volume(values['-Volume-'] / 100)            
    
Janela.close()