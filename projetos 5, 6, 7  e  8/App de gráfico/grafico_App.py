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
        if novo_valor.isnumeric() or \
           novo_valor.isdecimal:
            conteudo_tabela.append([len(conteudo_tabela) + 1,float(novo_valor)])
            Janela['-Tabela-'].update(conteudo_tabela)
            Janela['-input-'].update('')


Janela.close()