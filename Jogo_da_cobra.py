import PySimpleGUI as sg
from time import time

def convert_pos_to_pixel(celula):
    tl = celula[0] * tamanho_celula, celula[1] * tamanho_celula
    br = tl[0] + tamanho_celula, tl[1] + tamanho_celula 
    return tl, br

#Tamanho do campo do jogo
Tamanho_campo = 400
numero_celula = 20
tamanho_celula = Tamanho_campo/numero_celula

#Cobra
corpo_cobra = [(4,4),(3,4),(2,4)]
DIRECTIONS = {'left': (-1,0), 'right': (1,0), 'up':(0,1), 'down':(0,-1)}
direcao = DIRECTIONS['up']

#Maçã
maça_pos = (0,0)

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

start_time = time()

while True:
    event, values = Janela.read(timeout=10)
    if event == sg.WIN_CLOSED: break
    if event =='Left:37': print('Esquerda')
    if event =='Up:38': print('Acima')
    if event =='Right:39': print('Direita')
    if event =='Down:40': print('Abaixo')

    #Tempo para aparecer outra maçã
    tempo_quando_começar = time() - start_time
    if tempo_quando_começar >= 0.5:
        start_time = time()
        
        #Atualiza a posição da cobra
        nova_cabeça = (corpo_cobra[0][0] + direcao[0],corpo_cobra[0][1] + direcao[1])
        corpo_cobra.insert(0, nova_cabeça)
        corpo_cobra.pop()

        #Desenha a maçã
        tl, br = convert_pos_to_pixel(maça_pos) 
        Campo.DrawRectangle(tl, br,'red')

        Campo.draw_rectangle((0,0),(Tamanho_campo,Tamanho_campo), 'black')

        #Desenha a cobra
        for index, part in enumerate(corpo_cobra):
            tl, br = convert_pos_to_pixel(part)
            Cor = 'yellow' if index == 0 else 'green'
            Campo.DrawRectangle(tl,br,Cor)

Janela.close()