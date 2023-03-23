import PySimpleGUI as sg

layout = [
    []
]


Janela =  sg.Window('Editor de imagem', layout)

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
Janela.close()