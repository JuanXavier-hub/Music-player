import PySimpleGUI as sg
import pygame
import os

def toca_musica(musica):
    pygame.mixer.music.load(musica)
    pygame.mixer.music.play()

def pausa_musica():
    pygame.mixer.music.pause()

def para_musica():
    pygame.mixer.music.stop()

def tira_pausa():
    pygame.mixer.music.unpause()

# janela inicial da aplicação

def janela_inicial():
    
    sg.theme('Black')

    layout = [
             [sg.Image('Icones\icons8-apple-music-64.png', pad=(100,100))],
             [sg.Text('', key='titulo', font=('Arial', 10))],
             [
              sg.Button(key='menu', image_source= 'Icones\icons8-cardápio-64.png', pad=(50,50), button_color= 'Black') ,
              sg.Button(key='play_pause', image_source='Icones\icons8-reproduzir-64.png', pad=(50,50), button_color= 'Black'),
              sg.Button(key='stop', image_source='Icones\icons8-parar-64.png', pad=(50,50), button_color= 'Black')
             ]
             ]
    
    return sg.Window('Music Player', layout, element_justification='center', finalize=True)

# janela da lista de reprodução

def janela_menu():
    
    sg.theme('Black')

    layout = [
             [sg.T("Escolha um arquivo para reproduzir")],
             [sg.Listbox(musicas, enable_events=True, size=(100,20), key='musica')],
             [sg.B('Retornar')]
             ]

    return sg.Window('Menu', layout, element_justification='center', finalize=True)

# inicialização de alguns valores

pygame.mixer.init()
musicas = []
musica = ''
paused = False
playing = False
janela1, janela2 = janela_inicial(), None

for arquivo in os.listdir('Músicas'):
    if arquivo.endswith('.mp3'):
        musicas.append(arquivo)

#manipulação de valores / Programa principal (main)

while True:

    janela, evento, valores = sg.read_all_windows()
    if evento == sg.WINDOW_CLOSED:
        break

    # Condições para alternância entre janelas

    elif janela == janela1 and evento == 'menu':
        janela2 = janela_menu()
        janela1.hide()

    elif janela == janela2 and evento == 'Retornar':
        janela1.UnHide()
        janela2.hide()

    # Reprodutor de música

    elif janela == janela2:
        musica = janela['musica'].get()[-1]
 

    elif playing == False:
        if evento == 'play_pause':
            if musica == '':   
                janela['titulo'].update('Selecione uma faixa para tocar')
            else:
                toca_musica('Músicas/' + musica)
                playing = True
                janela['play_pause'].update(image_filename = 'Icones\icons8-pausa-64.png')
                janela['titulo'].update(str(musica))

    elif playing:
        if evento == 'play_pause':
            paused = not paused
            if paused:
                pausa_musica()
                janela['play_pause'].update(image_filename = 'Icones\icons8-reproduzir-64.png') 
            else:
                tira_pausa()
                janela['play_pause'].update(image_filename = 'Icones\icons8-pausa-64.png')                
        elif evento == 'stop':
            para_musica()
            playing, paused = False, False
            janela['play_pause'].update(image_filename = 'Icones\icons8-reproduzir-64.png')   



janela.close()


        
