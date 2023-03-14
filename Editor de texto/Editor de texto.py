import PySimpleGUI as sg

smileys = [
   'feliz',[':)','xD',':D','<3'],
   'triste',[':(','T_T'],
   'outros',[':3']
    ]
smiley_events = smileys[1] + smileys[3] + smileys[5]
menu_layout = [
    ['Arquivo',['Abrir', 'Salvar','---','Sair']],
    ['Mecânicas',['Contador de palavras']],
    ['Adicionar',smileys]
    ]


sg.theme('GrayGrayGray')
layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Sem título', key='-documentoNome-')],
    [sg.Multiline(no_scrollbar = True, size = (30,40), key = '-caixaDeTexto-')]
]

Janela = sg.Window('Editor de texto', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Contador de palavras':
        print('funcional um botão aí')
Janela.close()