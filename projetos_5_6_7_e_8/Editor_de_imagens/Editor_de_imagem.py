import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

def atualiza_imagem(original, blur, contraste, Emboss, Countor, flipx, flipy, Janela):
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contraste))
    
    if Emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if Countor:
        image = image.filter(ImageFilter.CONTOUR())
    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.flip(image)   
         
    bio = BytesIO()
    image.save(bio, format = 'PNG')
    
    Janela['-Imagem-'].update(data = bio.getvalue())

caminho_imagem = 'projetos_5_6_7_e_8\Editor_de_imagens\imagem.PNG'

coluna_controle = sg.Column([
    [sg.Frame('Borrado', layout = [[sg.Slider(range = (0,10), orientation= 'h', key='-blur-')]])],
    [sg.Frame('Contraste', layout = [[sg.Slider(range = (0,10), orientation= 'h', key='-Contraste-')]])],
    [sg.Checkbox('Relevo', key='-Emboss-'), sg.Checkbox('Contorno', key='-Countor-')],
    [sg.Checkbox('Virar x', key='-VirarX-'), sg.Checkbox('Virar y', key='-VirarY-')],
    [sg.Button('Salvar imagem', key='-Salvar-')],
])
coluna_imagem = sg.Column([[sg.Image(caminho_imagem, key='-Imagem-')]])

layout = [
    [coluna_controle, coluna_imagem]
]

original = Image.open(caminho_imagem)
Janela = sg.Window('Editor de imagem', layout)

while True:
    event, values = Janela.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break
    
    atualiza_imagem(
        original, 
        values['-blur-'],
        values['-Contraste-'],
        values['-Emboss-'],
        values['-Countor-'],
        values['-VirarX-'],
        values['-VirarY-'],
        Janela)   
    
Janela.close()