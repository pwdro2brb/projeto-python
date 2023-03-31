import PySimpleGUI as sg

Coluna_imagem = sg.Column([sg.Image(key = '-Imagem-', background_color='FFFFFF')])
coluna_info = sg.Column([[
    [sg.Text('', key = '-Localizacao-',font = 'Calibri 30', background_color = '#FF0000', pad = 0, visible = False)],
    [sg.Text('', key = '-Tempo-',font = 'Calibri 16', background_color = '#000000', pad = 0, visible = False, text_color='#FFFFFF')],
    [sg.Text('', key = '-Temp-',font = 'Calibri 16', pad = (0,10), background_color = '#FFFFFF', visible = False, text_color='#000000', justification = 'center')],
]])

layout = [
    [sg.Input(expand_x = True, key = '-Input-'),sg.Button('Entrar')],
    [Coluna_imagem, coluna_info]
]

Janela = sg.Window('App_para_clima', layout)

while True:
    event, values =  Janela.read()
    if event == sg.WIN_CLOSED:
        break


Janela.close()