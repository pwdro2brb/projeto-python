import PySimpleGUI as sg
from PIL import Image

def atualiza_imagem(original, borrao, contraste, Emboss, Countor, flipx, flipy):
    print(original)

caminho_imagem = 'projetos 5, 6, 7  e  8\Editor de imagem\cross.jpg'

coluna_controle = sg.Column([
    [sg.Frame('Borrado', layout = [[sg.Slider(range = (0,10), orientation= 'h', key='-borrao-')]])],
    [sg.Frame('Contraste', layout = [[sg.Slider(range = (0,10), orientation= 'h', key='-Contraste-')]])],
    [sg.Checkbox('Emboss', key='-Emboss-'), sg.Checkbox('Countour', key='-Countor-')],
    [sg.Checkbox('Virar x', key='-VirarX-'), sg.Checkbox('Virar y', key='-VirarY-')],
    [sg.Button('Salvar imagem', key='-Salvar-')],
])
coluna_imagem = sg.Column([[sg.Image(caminho_imagem)]])

layout = [
    [coluna_controle, coluna_imagem]
]

original = Image.open(caminho_imagem)
Janela =  sg.Window('Editor de imagem', layout)

while True:
    event, values = Janela.read(timeout = 50)
    if event == sg.WIN_CLOSED:
        break
    
    atualiza_imagem(
        original, 
        values['-borrao-'],
        values['-Contraste-'],
        values['-Emboss-'],
        values['-Countor-'],
        values['-VirarX-'],
        values['-VirarY-'],)    
    
Janela.close()