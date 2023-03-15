import PySimpleGUI as sg

#Tamanho do campo do jogo
Tamanho_campo = 400

sg.theme('LightGreen3')
Campo = sg.Graph(
    canvas_size= (Tamanho_campo,Tamanho_campo),
    graph_bottom_left= (0,0),
    graph_top_right= (Tamanho_campo,Tamanho_campo),
    background_color = 'black'
)
layout = [
    [Campo]
]

Janela = sg.Window('Jogo da cobra', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED():
        break

Janela.read()