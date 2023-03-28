import PySimpleGUI as sg
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO

def atualiza_imagem(original, blur, contraste, Emboss, Countor, flipx, flipy, Janela):
    global image
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

caminho_imagem = sg.popup_get_file('Open',no_window=True)

coluna_controle = sg.Column([
    [sg.Frame('Borrado', layout = [[sg.Slider(range = (0,10), orientation= 'h', key='-blur-')]])],
    [sg.Frame('Contraste', layout = [[sg.Slider(range = (0,10), orientation= 'h', key='-Contraste-')]])],
    [sg.Checkbox('Relevo', key='-Emboss-'), sg.Checkbox('Contorno', key='-Countor-')],
    [sg.Checkbox('Virar x', key='-VirarX-'), sg.Checkbox('Virar y', key='-VirarY-')],
    [sg.Button('Salvar imagem', key='-Salvar-')],
])
coluna_imagem = sg.Column([[sg.Image(caminho_imagem, key='-Imagem-')]])

layout = [
    [coluna_controle, coluna_imagem, sg.Button('Sair',key='-Sair-')]
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
    
    if event == '-Salvar-':
        salvar_caminho = sg.popup_get_file('Save', save_as = True, no_window = True) + '.png'
        image.save(salvar_caminho, 'PNG')
        sg.popup('Alteração da imagem salva')
        
    if event == '-Sair-':
        Janela.close()
        
Janela.close()