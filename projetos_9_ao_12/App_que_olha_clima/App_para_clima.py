import PySimpleGUI as sg
sg.theme('reddit')

Coluna_imagem = sg.Column([[sg.Image(key = '-Imagem-', background_color='#FFFFFF')]])
coluna_info = sg.Column([
    [sg.Text('', key = '-Localizacao-', font = 'Calibri 30', background_color = '#FF0000', text_color='#FFFFFf', pad = 0, visible = False)],
    [sg.Text('', key = '-Tempo-', font = 'Calibri 16', background_color = '#000000', pad = 0, visible = False, text_color='#FFFFFF')],
    [sg.Text('', key = '-Temp-', font = 'Calibri 16', pad = (0,10), background_color = '#FFFFFF', visible = False, text_color='#000000', justification = 'center')],
])

layout = [
    [sg.Input(expand_x = True, key = '-Input-'),sg.Button('Entrar', button_color='#000000', border_width=0)],
    [Coluna_imagem, coluna_info]
]

Janela = sg.Window('App_para_clima', layout)

while True:
    event, values =  Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Entrar':
        Janela['-Localizacao-'].update('test', visible = True)
        Janela['-Tempo-'].update('test', visible = True)
        Janela['-Temp-'].update('test', visible = True)
        Janela['-Imagem-'].update('projetos_9_ao_12\App_que_olha_clima\Imagens\Gelado.png')

Janela.close()