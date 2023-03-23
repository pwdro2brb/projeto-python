import PySimpleGUI as sg

coluna_controle = sg.Column([
    [sg.Slider(range = (0,10), orientation= 'h')],
    [sg.Checkbox('Emboss', key='-Emboss-'), sg.Checkbox('Countour', key='-Countor-')],
    [sg.Checkbox('Virar x', key='-VirarX-'), sg.Checkbox('Virar y', key='-VirarY-')],
    [sg.Button('Salvar imagem', key='-Salvar-')],
])
coluna_imagem = sg.Column([[sg.Image('projetos 5, 6, 7  e  8\Editor de imagem\cross.jpg')]])

layout = [
    [coluna_controle, coluna_imagem]
]

Janela =  sg.Window('Editor de imagem', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
Janela.close()