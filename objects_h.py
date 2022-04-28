import pygame
import os , sys

def Funx_Z(base_name):
    img_check = os.path.join('/assets/operators/' , base_name)
    img_check.convert()
    obj_sum = pygame.image.load(img_check)


def numbers(_strech_simbols):
    load_num = os.path.join('/assets/operators', number_name)
    load_num.convert()
    obj_num = pygame.image.load(load_num)

def _strech_simbols(_conectSimbols):
    load_sim = os.path.join('/assets/operators', conectSimbols)
    load_sim.convert()
    obj_simb = pygame.image.load(load_sim)
