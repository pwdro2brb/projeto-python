import PySimpleGUI as sg
import pandas as pd

sg.theme('DarkTeal4')

layout = [
    [sg.Text('Por favor preencha os seguintes campos: ')],
    [sg.Text('Nome', size=(15,1)), sg.InputText(key='Nome')],
    [sg.Text('Cor favorita', size=(15,1)), sg.Combo(['Verde', 'Azul', 'Vermelho'], key='Cor Favorita')],
    [sg.Text('Eu falo', size=(15,1)),
            sg.Checkbox('Alemão', key='Alemão'),
            sg.Checkbox('Português', key='Brasileiro'),
            sg.Checkbox('Espanhou', key='Espanhou'),
            sg.Checkbox('Inglês', key='Inglês'),
            sg.Checkbox('Mandarin', key='Mandarin'),
        ],
    [sg.Text('Número de crianças', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                         initial_value=0, key='-CRIANÇA-')],
 
    [sg.Submit('Enviar', key='Submit'),sg.Exit('Sair', key='sair')],
]

Janela = sg.Window('App para receber dados daqui e enviar para o excel', layout)


while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED or 'sair':
        break
    if event == 'Submit':
        print(event,values)

Janela.close()

#pip install PySimpleGui
#pip install panda
#pip install openpyxl