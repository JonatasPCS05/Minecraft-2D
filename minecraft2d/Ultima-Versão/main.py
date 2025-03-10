#Colisão e gravidade adicionadas, a colisão ainda está faltando as laterais

import pygame
pygame.init()
import classe
import var
import funcao


def main():
    var.screen = pygame.display.set_mode((800,608))
    pygame.display.set_caption("Minecraft 2d")

    var.player = classe.Entity(25*var.pixel_block, 13*var.pixel_block, 1, 0, var.personagem)

    for i in range(38):
        var.elementos.append([])
        for e in range(51):
            var.elementos[i].append(0)

    funcao.gerar_mundo()

    clock = pygame.time.Clock()
    fps = 60

    janela_aberta = True
    while janela_aberta:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                janela_aberta = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    funcao.gerar_mundo()
        
        comando = pygame.key.get_pressed()
        if comando[pygame.K_d] and var.player.d:
            var.player.pos_x += var.player.vel_x
        if comando[pygame.K_a] and var.player.a:
            var.player.pos_x -= var.player.vel_x
        if comando[pygame.K_w] and var.player.ingnd == True:
            var.player.ingnd = False
            var.player.vel_y = -5
            var.player.pos_y += var.player.vel_y
        #if comando[pygame.K_s]:
            #player.pos_y += player.vel_y

        funcao.colisao()
        #player.gravity()

        funcao.desenhar_tela()
        funcao.draw_rect()
        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()