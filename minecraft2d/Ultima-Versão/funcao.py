import var
import random
import pygame
import classe

def gerar_mundo():
    for i in range(37,-1,-1):
        for e in range(49,-1,-1):
            if e == 49:
                if i >= 20 and i<= 38:
                    var.elementos[i][e] = 3
                if i >= 16 and i < 20:
                    if var.elementos[i+1][e] <= 1:
                        var.elementos[i][e] = 0
                    if var.elementos[i+1][e] == 2:
                        r = random.randint(1,3)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 1
                    if var.elementos[i+1][e] == 3:
                        r = random.randint(1,5)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 3
                if i >= 1 and i < 16:
                    if var.elementos[i+1][e] <= 1:
                        var.elementos[i][e] = 0
                    if var.elementos[i+1][e] == 2:
                        r = random.randint(1,3)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 1
                    if var.elementos[i+1][e] == 3:
                        r = random.randint(1,5)
                        if r == 1:
                            var.elementos[i][e] = 3
                        if r >= 2:
                            var.elementos[i][e] = 2
            else:
                if i >= 20 and i<= 38:
                    var.elementos[i][e] = 3
                if i >= 16 and i < 20:    
                    if var.elementos[i+1][e] <= 1:
                        var.elementos[i][e] = 0
                    if var.elementos[i+1][e] == 2 and var.elementos[i][e+1] <= 1:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 1
                    if var.elementos[i+1][e] == 2 and var.elementos[i][e+1] >= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 1
                        if r >= 2:
                            var.elementos[i][e] = 2
                    if var.elementos[i+1][e] == 3 and var.elementos[i][e+1] <= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 3
                        if r >= 2:
                            var.elementos[i][e] = 2
                    if var.elementos[i+1][e] == 3 and var.elementos[i][e+1] == 3:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 3
                if i >= 1 and i < 16:
                    if var.elementos[i+1][e] <= 1:
                        var.elementos[i][e] = 0
                    if var.elementos[i+1][e] == 2 and var.elementos[i][e+1] <= 1:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 1
                    if var.elementos[i+1][e] == 2 and var.elementos[i][e+1] >= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 1
                        if r >= 2:
                            var.elementos[i][e] = 2
                    if var.elementos[i+1][e] == 3 and var.elementos[i][e+1] <= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 3
                        if r >= 2:
                            var.elementos[i][e] = 2
                    if var.elementos[i+1][e] == 3 and var.elementos[i][e+1] == 3:
                        r = random.randint(1,10)
                        if r == 1:
                            var.elementos[i][e] = 2
                        if r >= 2:
                            var.elementos[i][e] = 3

def colisao():
    var.player.rect = pygame.Rect(var.player.pos_x, var.player.pos_y, var.pixel_block, var.pixel_block*2)
    var.player.ingnd = False

    var.blocks = []
    for i in range(len(var.elementos)):
        var.blocks.append([])
        for e in range(len(var.elementos[0])):
            var.blocks[i].append(classe.Block(e*var.pixel_block, i*var.pixel_block, var.elementos[i][e]))
    
    var.player.gravity()
    var.player.colision()
    
def desenhar_tela():
    var.screen.blit(var.fundo, (0,0))
    for i in range (38):
        for e in range (50):
            if var.elementos[i][e] == 1:
                var.screen.blit(var.bloco_grama, (e*16,i*16))
            if var.elementos[i][e] == 2:
                var.screen.blit(var.bloco_terra, (e*16,i*16))
            if var.elementos[i][e] == 3:
                var.screen.blit(var.bloco_pedra, (e*16,i*16))
    var.screen.blit(var.player.skin, (var.player.pos_x, var.player.pos_y))

def draw_rect():
    for i in range(len(var.blocks)):
        for e in range(len(var.blocks[0])):
            pygame.draw.rect(var.screen, (255, 0, 0), var.blocks[i][e], 1)