import PySimpleGUI as sg 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def atualizar_figuras(data):
    axes = figura.axes
    x = [i[0] for i in data]
    y = [int(i[1]) for i in data]
    axes[0].plot(x,y,'r-')
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack()

sg.theme('LightGreen7')

conteudo_tabela = []

layout = [
    [sg.Table(
    headings=['Observações', 'resultados'], 
    values = conteudo_tabela, 
    expand_x = True,
    hide_vertical_scroll = True,
    key='-Tabela-')],
   [sg.Input(key='-input-', expand_x=True), sg.Button('Enviar')],
   [sg.Canvas(key='-canvas-')]    
]

Janela = sg.Window('App de gráfico', layout, finalize = True)

#Chamando o Matpotlib para criar o gráfico
figura = matplotlib.figure.Figure(figsize = (5,4))
figura.add_subplot(111).plot([],[])
figure_canvas_agg = FigureCanvasTkAgg(figura,Janela['-canvas-'].TKCanvas)
figure_canvas_agg.draw()
figure_canvas_agg.get_tk_widget().pack()

while True:
    event, values = Janela.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Enviar':
        novo_valor = values['-input-']
        if novo_valor.isnumeric() or \
           novo_valor.isdecimal:
            conteudo_tabela.append([len(conteudo_tabela) + 1,float(novo_valor)])
            Janela['-Tabela-'].update(conteudo_tabela)
            Janela['-input-'].update('')
            atualizar_figuras(conteudo_tabela)


Janela.close()