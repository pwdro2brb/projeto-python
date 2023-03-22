import PySimpleGUI as sg 

sg.theme('LightGreen7')

conteudo_tabela = []

layout = [
    [sg.Table(
    headings=['Observações', 'resultados'], 
    values = conteudo_tabela, 
    expand_x = True,
    hide_vertical_scroll = True,
    key='-Tabela-')],
   [sg.Input(key='-input-', expand_x=True), sg.Button('Enviar')]    
]

Janela = sg.Window('App de gráfico', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Enviar':
        novo_valor = values['-input-']
        if novo_valor.isnumeric():
            Janela['-Tabela-'].update([[1,10], [2,12], [3,0]])

Janela.close()