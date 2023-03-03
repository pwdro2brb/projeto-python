import PySimpleGUI as sg

sg.theme('DarkGrey6')
sg.set_options(font = 'Franklin 18', button_element_size=(3,3))
button_size =(6,3)

layout = [
    [sg.Text('Saída', font='Franklin 26', justification = 'right', expand_x = True, pad = (10,20))],
    [sg.Button('Limpar',expand_x=True), sg.Button('Enter', expand_x=True)],
    [sg.Button('7', size = button_size), sg.Button('8', size = button_size),sg.Button('9', size = button_size),sg.Button('*', size = button_size)],
    [sg.Button('4', size = button_size), sg.Button('5', size = button_size),sg.Button('6', size = button_size),sg.Button('/', size = button_size)],
    [sg.Button('1', size = button_size), sg.Button('2', size = button_size),sg.Button('3', size = button_size),sg.Button('-', size = button_size)],
    [sg.Button('0', expand_x=True), sg.Button('.', size = button_size),sg.Button('+', size = button_size)]
    ]


Janela = sg.Window('Calculadora', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

Janela.close() 