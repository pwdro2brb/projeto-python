import PySimpleGUI as sg

sg.theme('DarkTeal4')

layout = [
    [sg.Text('Por favor preencha os seguintes campos: ')],
    [sg.Text('Nome', size=(15,1)), sg.InputText(key='Nome')],
    [sg.Submit('Enviar', key='Submit'),sg.Exit('Sair', key='sair')]
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