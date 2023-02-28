import PySimpleGUI as sg

layout = [
    [sg.Text('Texto'),sg.Spin(['Item 1', 'Item 2'])],
    [sg.Button('Botão')],
    [sg.Input()],
    [sg.Text('Teste'), sg.Button('Apenas para teste')]
]

Janela = sg.Window('converter', layout)

while True: 
  event, values = Janela.read()

  if event == sg.WIN_CLOSED:
    break
Janela.close()