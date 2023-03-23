import PySimpleGUI as sg

coluna_controle = True
coluna_imagem = sg.Column([[sg.Image('projetos 5, 6, 7  e  8\Editor de imagem\cross.jpg')]])

layout = [
    [coluna_imagem]
]

Janela =  sg.Window('Editor de imagem', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
Janela.close()