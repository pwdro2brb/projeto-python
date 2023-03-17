import PySimpleGUI as sg

def convert_pos_to_pixel(celula):
    tl = celula[0] * tamanho_celula, celula[1] * tamanho_celula
    br = tl[0] + tamanho_celula, tl[1] + tamanho_celula 
    return tl, br

#Tamanho do campo do jogo
Tamanho_campo = 400
numero_celula = 10
tamanho_celula = Tamanho_campo/numero_celula

#Cobra
corpo_cobra = [(4,4),(3,4),(2,4)]
DIRECTIONS = {'left': (-1,0), 'right': (1,0), 'up':(0,1), 'down':(0,-1)}

#Maçã
maça_pos = (0,1)

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

    tl, br = convert_pos_to_pixel(maça_pos) 
    Campo.DrawRectangle(tl, br,'red')

    #Desenha a cobra
    for index, part in enumerate(corpo_cobra):
        tl, br = convert_pos_to_pixel(part)
        Cor = 'yellow' if index == 0 else 'green'
        Campo.DrawRectangle(tl,br,Cor)

Janela.close()