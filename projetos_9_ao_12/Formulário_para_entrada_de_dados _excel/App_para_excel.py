import PySimpleGUI as sg
import pandas as pd


sg.theme('DarkTeal4')

EXCEL_FILE='projetos_9_ao_12\Formulário_para_entrada_de_dados _excel\Testes_para_codigo.xlsx'
df = pd.read_excel(EXCEL_FILE)

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
 
    [sg.Submit('Enviar', key='Submit'), sg.Button('Limpar'),sg.Exit('Sair', key='sair')],
]

Janela = sg.Window('App para receber dados daqui e enviar para o excel', layout)

def limpar_input():
    for key in values:
        Janela[key]('')
    return None
        

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Limpar':
        limpar_input()
    if event == 'Submit':
        df = df._append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Dados salvados!!!')
        limpar_input()

Janela.close()

#pip install PySimpleGui
#pip install panda
#pip install openpyxl