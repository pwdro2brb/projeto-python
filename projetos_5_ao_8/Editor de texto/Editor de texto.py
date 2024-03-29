import PySimpleGUI as sg
from pathlib import Path

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

    if event == 'Abrir':
        caminho_arquivo = sg.popup_get_file('Abrir', no_window= True)
        if caminho_arquivo:
            arquivo = Path(caminho_arquivo)
            Janela['-caixaDeTexto-'].update(arquivo.read_text())
            Janela['-documentoNome-'].update(caminho_arquivo.split('/')[-1])

    if event == 'Salvar':
        caminho_arquivo = sg.popup_get_file('Salvar como', no_window = True, save_as=True) + '.txt'
        arquivo = (caminho_arquivo)
        Path(caminho_arquivo).write_text(values['-caixaDeTexto-'])
        Janela['-documentoNome-'].update(caminho_arquivo.split('/')[-1])

    if event == 'Contador de palavras':
       texto_cheio = values['-caixaDeTexto-']
       texto_limpo = texto_cheio.replace('\n', ' ').split(' ')
       conta_palavra = len(texto_limpo)
       conta_caracter = len(''.join(texto_limpo))
       sg.popup(f'Palavras {conta_palavra}\nCarácteres: {conta_caracter}')

    if event in smiley_events:
        texto_atual = values['-caixaDeTexto-']
        novo_texto = texto_atual + ' ' + event
        Janela['-caixaDeTexto-'].update(novo_texto)

Janela.close()