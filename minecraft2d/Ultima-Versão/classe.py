import pygame
pygame.init()
import var

class Entity:
    def __init__(self, pos_x, pos_y, vel_x, vel_y, skin):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.skin = skin
        self.rect = pygame.Rect(self.pos_x, self.pos_y, var.pixel_block-4, var.pixel_block*2)
        self.ingnd = False
        self.a = True
        self.d = True

    def gravity(self):
        int_x = self.pos_x//var.pixel_block
        int_y = int(self.pos_y//var.pixel_block)

        if var.elementos[int_y+2][int_x] != 0 or (var.elementos[int_y+2][int_x] == 0 and var.elementos[int_y+2][int_x+1] != 0):
            if self.rect.colliderect(var.blocks[int_y+2][int_x]) and self.ingnd == False:
                self.ingnd = True
                self.vel_y = 0
            else:
                self.vel_y += var.vel_gravity
                self.ingnd = False
        else:
            self.vel_y += var.vel_gravity
            self.ingnd = False

        self.pos_y += self.vel_y

    def colision(self):
        int_x = self.pos_x//var.pixel_block
        int_y = int(self.pos_y//var.pixel_block)

        if var.blocks[int_y][int_x].id != 0 or var.blocks[int_y+1][int_x].id != 0:
            self.a = False
        else:
            self.a = True
        
        if var.blocks[int_y][int_x-1].id != 0 or var.blocks[int_y+1][int_x-1].id != 0:
            self.w = False
        else:
            self.w = True

class Block:
    def __init__(self, x, y, id):
        self.rect = pygame.Rect(x, y, var.pixel_block, var.pixel_block)
        self.id = id