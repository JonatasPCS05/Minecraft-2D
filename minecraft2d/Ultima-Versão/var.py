import pygame

#fixas
pixel_block = 16
vel_gravity = 0.5

#mudam
elementos = []
blocks = []
player = []
screen = []

#skins
fundo = pygame.image.load('img/fundo.png')
personagem = pygame.image.load('img/personagem.png')
bloco_grama = pygame.image.load('img/bloco_grama.png')
bloco_terra = pygame.image.load('img/bloco_terra.png')
bloco_pedra = pygame.image.load('img/bloco_pedra.png')