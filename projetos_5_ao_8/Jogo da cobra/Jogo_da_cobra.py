import PySimpleGUI as sg
from time import time
from random import randint

def convert_pos_to_pixel(celula):
    tl = celula[0] * tamanho_celula, celula[1] * tamanho_celula
    br = tl[0] + tamanho_celula, tl[1] + tamanho_celula 
    return tl, br

def colocar_maca():
    maça_pos = randint(0,tamanho_celula - 1), randint(0,tamanho_celula-1)
    while maça_pos in corpo_cobra:
        maça_pos = randint(0, tamanho_celula - 1), randint(0, tamanho_celula - 1)
    return maça_pos

#Tamanho do campo do jogo
Tamanho_campo = 400
numero_celula = 20
tamanho_celula = Tamanho_campo/numero_celula

#Cobra
corpo_cobra = [(4,4),(3,4),(2,4)]
DIRECTIONS = {'left': (-1,0), 'right': (1,0), 'up':(0,1), 'down':(0,-1)}
direcao = DIRECTIONS['up']

#Maçã
maça_pos = colocar_maca()
comer_maca = False

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
    if event =='Left:37': direcao = DIRECTIONS['left']
    if event =='Up:38': direcao = DIRECTIONS['up']
    if event =='Right:39': direcao = DIRECTIONS['right']
    if event =='Down:40': direcao = DIRECTIONS['down']

    #Tempo para aparecer outra maçã
    tempo_quando_começar = time() - start_time
    if tempo_quando_começar >= 0.3: #Velocidade do jogo
        start_time = time()

        #Colisão com a maçâ
        if corpo_cobra[0] == maça_pos:
            maça_pos = colocar_maca()
            comer_maca = True
        
        #Atualiza a posição da cobra
        nova_cabeça = (corpo_cobra[0][0] + direcao[0],corpo_cobra[0][1] + direcao[1])
        corpo_cobra.insert(0, nova_cabeça)
        if not comer_maca:
            corpo_cobra.pop()
        comer_maca = False

        #Verifica morte
        if not 0 <= corpo_cobra[0][0] <= numero_celula - 1 or \
           not 0 <= corpo_cobra[0][1] <= numero_celula - 1 or \
           corpo_cobra[0] in corpo_cobra[1:]:
               sg.popup('Você morreu')
               break
               

        Campo.draw_rectangle((0,0),(Tamanho_campo,Tamanho_campo), 'black')

        #Desenha a maçã
        tl, br = convert_pos_to_pixel(maça_pos) 
        Campo.DrawRectangle(tl, br,'red')

        #Desenha a cobra
        for index, part in enumerate(corpo_cobra):
            tl, br = convert_pos_to_pixel(part)
            Cor = 'yellow' if index == 0 else 'green'
            Campo.DrawRectangle(tl,br,Cor)

Janela.close()