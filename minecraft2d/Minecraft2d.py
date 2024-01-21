import pygame
pygame.init() 
import random

x = 25*16
y = 13*16
velocidade = 16
fundo = pygame.image.load('img/fundo.png')
personagem = pygame.image.load('img/personagem.png')
bloco_grama = pygame.image.load('img/bloco_grama.png')
bloco_terra = pygame.image.load('img/bloco_terra.png')
bloco_pedra = pygame.image.load('img/bloco_pedra.png')

janela = pygame.display.set_mode((800,608))
pygame.display.set_caption("Minecraft 2d")
elementos = []
for i in range(38):
    elementos.append([])
    for e in range(50):
        elementos[i].append(0)

def gerar_mundo():
    for i in range(37,-1,-1):
        for e in range(49,-1,-1):
            if e == 49:
                if i >= 20 and i<= 38:
                    elementos[i][e] = 3
                if i >= 16 and i < 20:
                    if elementos[i+1][e] <= 1:
                        elementos[i][e] = 0
                    if elementos[i+1][e] == 2:
                        r = random.randint(1,3)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 1
                    if elementos[i+1][e] == 3:
                        r = random.randint(1,5)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 3
                if i >= 1 and i < 16:
                    if elementos[i+1][e] <= 1:
                        elementos[i][e] = 0
                    if elementos[i+1][e] == 2:
                        r = random.randint(1,3)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 1
                    if elementos[i+1][e] == 3:
                        r = random.randint(1,5)
                        if r == 1:
                            elementos[i][e] = 3
                        if r >= 2:
                            elementos[i][e] = 2
            else:
                if i >= 20 and i<= 38:
                    elementos[i][e] = 3
                if i >= 16 and i < 20:    
                    if elementos[i+1][e] <= 1:
                        elementos[i][e] = 0
                    if elementos[i+1][e] == 2 and elementos[i][e+1] <= 1:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 1
                    if elementos[i+1][e] == 2 and elementos[i][e+1] >= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 1
                        if r >= 2:
                            elementos[i][e] = 2
                    if elementos[i+1][e] == 3 and elementos[i][e+1] <= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 3
                        if r >= 2:
                            elementos[i][e] = 2
                    if elementos[i+1][e] == 3 and elementos[i][e+1] == 3:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 3
                if i >= 1 and i < 16:
                    if elementos[i+1][e] <= 1:
                        elementos[i][e] = 0
                    if elementos[i+1][e] == 2 and elementos[i][e+1] <= 1:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 1
                    if elementos[i+1][e] == 2 and elementos[i][e+1] >= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 1
                        if r >= 2:
                            elementos[i][e] = 2
                    if elementos[i+1][e] == 3 and elementos[i][e+1] <= 2:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 3
                        if r >= 2:
                            elementos[i][e] = 2
                    if elementos[i+1][e] == 3 and elementos[i][e+1] == 3:
                        r = random.randint(1,10)
                        if r == 1:
                            elementos[i][e] = 2
                        if r >= 2:
                            elementos[i][e] = 3

gerar_mundo()
janela_aberta = True
while janela_aberta:
    pygame.time.delay(200)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comando = pygame.key.get_pressed()
    if comando[pygame.K_d]:
        x += velocidade
    if comando[pygame.K_a]:
        x -= velocidade
    if comando[pygame.K_w]:
        y -= velocidade
    if comando[pygame.K_s]:
        y += velocidade
    if comando[pygame.K_r]:
        gerar_mundo()

    janela.blit(fundo, (0,0))
    for i in range (38):
        for e in range (50):
            if elementos[i][e] == 1:
                janela.blit(bloco_grama, (e*16,i*16))
            if elementos[i][e] == 2:
                janela.blit(bloco_terra, (e*16,i*16))
            if elementos[i][e] == 3:
                janela.blit(bloco_pedra, (e*16,i*16))
    janela.blit(personagem, (x,y))
    pygame.display.update()

pygame.quit()