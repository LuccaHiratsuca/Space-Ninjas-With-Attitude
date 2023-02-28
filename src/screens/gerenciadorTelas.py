# classe que irá gerenciar as telas do jogo

import pygame
import screens.chooseWeapon as chooseWeapon
import screens.home as home
import screens.derrota as derrota
import screens.vitoria as vitoria
import fases.level

class GerenciadorTelas():
    def __init__(self, display,updates={}, restart=False):
        self.display = display
        self.current_screen_string = 'home'
        self.updates = updates
        self.previous_screen = ['home']
        self.restart = restart
    

    def atualiza(self):
        if self.current_screen_string == 'home' :
            self.current_screen = home.Home(self.display)
            self.previous_screen.append('home')
        elif (self.current_screen_string == 'chooseWeapon' and self.previous_screen[-1] != 'chooseWeapon') or self.restart:
            self.current_screen = chooseWeapon.chooseWeapon(self.display)
            self.previous_screen.append('chooseWeapon')
        elif (self.current_screen_string == 'level' and self.previous_screen[-1] != 'level') or self.restart:
            self.current_screen = fases.level.level(self.display, self.updates)
            self.previous_screen.append('level')
        elif self.current_screen_string == 'derrota' and self.previous_screen[-1] != 'derrota':
            self.current_screen = derrota.Derrota(self.display)
            self.previous_screen.append('derrota')
        elif self.current_screen_string == 'vitoria' and self.previous_screen[-1] != 'vitoria':
            self.current_screen = vitoria.Vitoria(self.display)
            self.previous_screen.append('vitoria')
        return self.current_screen.atualiza_estado()
    
    def game_loop(self):
        while self.atualiza():
            self.desenha()

    def set_state(self, next_screen):
        self.current_screen_string = next_screen
        self.game_loop()


    def desenha(self):
        if self.current_screen_string == 'home' and self.previous_screen[-1] != 'home' :
            self.current_screen = home.Home(self.display)
            self.previous_screen.append('home')
        elif self.current_screen_string == 'chooseWeapon' and self.previous_screen[-1] != 'chooseWeapon':
            self.current_screen = chooseWeapon.chooseWeapon(self.display)
            self.previous_screen.append('chooseWeapon')
        elif self.current_screen_string == 'level' and self.previous_screen[-1] != 'level':
            self.current_screen = fases.level.level(self.display, self.updates)
            self.previous_screen.append('level')
        elif self.current_screen_string == 'derrota' and self.previous_screen[-1] != 'derrota':
            self.current_screen = derrota.Derrota(self.display)
            self.previous_screen.append('derrota')
        elif self.current_screen_string == 'vitoria' and self.previous_screen[-1] != 'vitoria':
            self.current_screen = vitoria.Vitoria(self.display)
            self.previous_screen.append('vitoria')
        self.current_screen.desenha(self.display)


        

    def finaliza(self):
        pygame.quit()
