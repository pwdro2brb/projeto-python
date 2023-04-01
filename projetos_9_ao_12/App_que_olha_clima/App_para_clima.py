import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

def get_weater_data(location):
    url = f'https://www.google.com/search?q=wheater+{location.replace(" ","")}'
    session = requests.Session()
    session.headers['User-agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
    Html = session.get(url)
    
    soup = bs(Html.text, 'html.parser')
    name = soup.find("div", attrs={'id':'wob_loc'}).text
    time = soup.find('div', attrs={'id':'wob_dts'}).text
    wheather = soup.find('span', attrs={'id':'wob_dc'}).text
    temp = soup.find('span', attrs={'id':'wob_tm'}).text
    return name, time, wheather, temp 

sg.theme('reddit')

Coluna_imagem = sg.Column([[sg.Image(key = '-Imagem-', background_color='#FFFFFF')]])
coluna_info = sg.Column([
    [sg.Text('', key = '-Localizacao-', font = 'Calibri 30', background_color = '#FF0000', text_color='#FFFFFf', pad = 0, visible = False)],
    [sg.Text('', key = '-Tempo-', font = 'Calibri 16', background_color = '#000000', pad = 0, visible = False, text_color='#FFFFFF')],
    [sg.Text('', key = '-Temp-', font = 'Calibri 16', pad = (0,10), background_color = '#FFFFFF', visible = False, text_color='#000000', justification = 'center')],
])

layout = [
    [sg.Input(expand_x = True, key = '-Input-'),sg.Button('Entrar', button_color='#000000', border_width=0)],
    [Coluna_imagem, coluna_info]
]

Janela = sg.Window('App_para_clima', layout)

while True:
    event, values =  Janela.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'Entrar':
        name, time, wheather, temp = get_weater_data(values['-Input-'])
        Janela['-Localizacao-'].update(name, visible = True)
        Janela['-Tempo-'].update(time, visible = True)
        Janela['-Temp-'].update(temp, visible = True)
        Janela['-Imagem-'].update('projetos_9_ao_12\App_que_olha_clima\Imagens\Gelado.png')

Janela.close()