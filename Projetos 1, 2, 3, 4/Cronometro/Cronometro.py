import PySimpleGUI as sg
from time import time

def create_window():
  sg.theme('black')
  layout = [
     [sg.Push(),sg.Image('Cronometro/cross.png',size =(10,10), pad = 0, enable_events=True, key = '-Fechar-')],
     [sg.VPush()],
     [sg.Text('Tempo', font = 'Young 50', key = '-TEMPO-')],
     [   sg.Button('Começar', button_color = ('#FFFFFF','#FF0000'), border_width= 0, key =  '-ComeçoPara-'), 
         sg.Button('Voltas',button_color = ('#FFFFFF','#FF0000'), border_width= 0, key = '-Volta-', visible = False)],
     [sg.Column([[]], key = '-Voltas-')],
     [sg.VPush()]
   ] 
 
  return sg.Window('Cronometro', 
         layout,
         size =(300,300),
         no_titlebar= True,
         element_justification = 'center')



Janela = create_window()
start_time = 0
active = False
quantidade_volta = 1

while True:
    event, values = Janela.read(timeout = 10)
    if event in (sg.WIN_CLOSED,  '-Fechar-'):
        break

    if event == '-ComeçoPara-':
        if active:
            # De active até Pare
            active = False
            Janela['-ComeçoPara-'].update('Recomeçar')
            Janela['-Volta-'].update(visible =  False)
        else:
            #De Pare para Recomeçar

            if start_time > 0:
                Janela.close
                Janela = create_window()
                start_time = 0
                quantidade_volta = 1

            # De start até active
            else:
             start_time = time()
             active = True
             Janela['-ComeçoPara-'].update('Pare')
             Janela['-Volta-'].update(visible = True)


    if active:
        elapsed_time = round(time() - start_time,1)
        Janela['-TEMPO-'].update(elapsed_time)

    if event == '-Volta-':
       Janela.extend_layout(Janela['-Voltas-'], [[sg.Text(quantidade_volta), sg.VSeparator(), sg.Text(elapsed_time)]])
       quantidade_volta += 1 

Janela.close()