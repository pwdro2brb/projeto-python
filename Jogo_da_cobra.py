import PySimpleGUI as sg

#Tamanho do campo do jogo
Tamanho_campo = 400
numero_celula = 10
tamanho_celula = Tamanho_campo/numero_celula

#Maçã
maça_pos = (2,4)

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

Janela = sg.Window('Jogo da cobra', layout, return_keyboard_events = True)

while True:
    event, values = Janela.read(timeout=10)
    if event == sg.WIN_CLOSED: break
    if event =='Left:37': print('Esquerda')
    if event =='Up:38': print('Acima')
    if event =='Right:39': print('Direita')
    if event =='Down:40': print('Abaixo')
    Campo.DrawRectangle( (100,100), (400,0),'red')

Janela.close()