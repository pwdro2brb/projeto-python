import PySimpleGUI as sg

layout = [
    [
        sg.Input(key='-Input-'),
        sg.Spin(['Km para milhas', 'kg para g', 'segundo para minuto'], key='-Unidades-'),
        sg.Button('Converter', key='-Converter-')
    ],

    [sg.Text('Saída', key='-saida-')]
]

Janela = sg.Window('converter', layout)

while True: 
  event, values = Janela.read()

  if event == sg.WIN_CLOSED:
    break

  if event == '-Converter-':
    input_value = values['-Input-']
    if input_value.isnumeric():
      input_value = float(input_value)
      match values['-Unidades-']:
        case 'Km para milhas':
          output = input_value * 0.6214
          output_string = f'{input_value} Km é {output} milhas.'

      Janela['-saida-'].update(output_string)


Janela.close()