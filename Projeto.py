import PySimpleGUI as Sg

layout = [
    [Sg.Text('Texto')],
    [Sg.Button('Botão')],
    [Sg.Input()]
]

Sg.Window('converter', layout).read()