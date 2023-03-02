
import pygame
import screens.gerenciadorTelas
import os

# Função principal do jogo que inicializa o pygame e o gerenciador de telas
def main(): 
    pygame.init()
    pygame.mixer.init()
    width = 1220
    height = 650
    icon = pygame.image.load(os.path.join('src','assets', 'images', 'icon.png')) # Carrega o ícone do jogo
    pygame.mixer.music.load(os.path.join('src','assets', 'music', 'Risk_of_Rain_2.mp3')) # Carrega a música de fundo
    pygame.mixer.music.play(-1)
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Space Ninjas With Attitude')
    display = pygame.display.set_mode((width, height))
    screen = screens.gerenciadorTelas.GerenciadorTelas(display) # Inicializa o gerenciador de telas
    screen.game_loop()
    screen.finaliza()

if __name__ == '__main__':
    main()