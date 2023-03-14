import PySimpleGUI as sg

smileys = [
   'feliz',[':)','xD',':D','<3'],
   'triste',[':(','T_T'],
   'outros',[':3']
    ]

menu_layout = [
    ['Arquivo',['Abrir', 'Salvar','---','Sair']],
    ['Mecânicas',['Contador de palavras']],
    ['Adicionar',smileys]
    ]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Sem título', key='-documentoNome-')],
    [sg.Multiline()]
]

Janela = sg.Window('Editor de texto', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

Janela.close()