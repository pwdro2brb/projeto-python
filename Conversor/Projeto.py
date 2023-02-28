import PySimpleGUI as sg

layout = [
    [sg.Text('Texto', enable_events= True, key = '-Text-'),sg.Spin(['Item 1', 'Item 2'])],
    [sg.Button('Botão', key= 'Button1')],
    [sg.Input(key = ('-Input-'))],
    [sg.Text('Teste'), sg.Button('Apenas para teste', key = 'Button2')]
]

Janela = sg.Window('converter', layout)

while True: 
  event, values = Janela.read()

  if event == sg.WIN_CLOSED:
    break
  if event == 'Button1':
   Janela['-Text-'].update(values['-Input-'])

  if event == 'Button2':
    print('Você apertou outro botão')
    Janela['Button2'].update(visible = False)
    
  if event == '-Text-':
    print('Você apertou texto')

  
Janela.close()