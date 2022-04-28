#!/usr/bin/python3.8
#!*-*conding=utf-8*-*
import sys
import math
from sys import stdin
import pygame
from pygame.locals import *
from change_theme import colors as COLORS
from change_theme import dark_theme as dark
from settings import BLOCK, BLOCK_0, BLOCK_1, BLOCK_2, BLOCK_3, BLOCKC_4, BLOCK_5, BLOCK_6
from settings import A_BLOCK, B_BLOCK_0, C_BLOCK_1, D_BLOCK_2, E_BLOCK_3, F_BLOCKC_4, G_BLOCK_5, H_BLOCK_6
from settings import BA_BLOCK, BB_BLOCK_0, BC_BLOCK_1, BD_BLOCK_2, BE_BLOCK_3, BF_BLOCKC_4, BG_BLOCK_5, BH_BLOCK_6
from settings import CA_BLOCK, CB_BLOCK_0, CC_BLOCK_1, CD_BLOCK_2, CE_BLOCK_3, CF_BLOCK_4, CG_BLOCK_5
from settings import DISPLAY_CHANGE
from settings import CH_THEME as theme_c
from objects_h import *
# uff  very now longuer time off setting code _ now _process _ contrib _____
# hello programm is it range out

# class Make:
    # def __init__(self,obj, program):
        # self.obj = obj
        # self.program = program
#
#
    # def builder(self):
        # print('this, is make objects_ create _in class')
#
#
#
# build = Make(sys.argv[2], sys.argv[3])
# print('this is name = {} y program is {}'.format(build.obj, build.program))

pygame.init()
POSXH = 951
POSYW = 670
# FOTAGRAME FOR SECONDS

FPS = 128
# BUILD ELEMENTS  __PROCESSING
scr_v = pygame.display.set_mode((POSYW, POSXH), 32)

class Make:
    """processing code objects"""
    def __init__(self, Ablock , Bblock , Cblock , Dblock ,Eblock,  Fblock , Gblock , Hblock ):
        self.Ablock = Ablock # new create block  in the processing cube in screen
        self.Bblock = Bblock
        self.Cblock = Cblock
        self.Dblock = Dblock
        self.Eblock = Eblock
        self.Fblock = Fblock
        self.Gblock = Gblock
        self.Hblock = Hblock
        # self.bck00 =

    def builder(self):
        self.cr = pygame.draw.rect(scr_v, (COLORS[0]), self.Ablock, 1)
        self.cr_0 = pygame.draw.rect(scr_v, (COLORS[0]), self.Bblock, 1)
        self.cr_1 = pygame.draw.rect(scr_v, (COLORS[0]), self.Cblock, 1)
        self.cr_2 = pygame.draw.rect(scr_v, (COLORS[0]), self.Dblock, 1)
        self.cr_3 = pygame.draw.rect(scr_v, (COLORS[0]), self.Eblock, 1)
        self.cr_44 = pygame.draw.rect(scr_v, (COLORS[0]), self.Fblock, 1)
        self.cr_5 = pygame.draw.rect(scr_v, (COLORS[0]), self.Gblock, 1)
        self.cr_6 = pygame.draw.rect(scr_v, (COLORS[0]), self.Hblock, 1)


    def selector(self):
        self.cr = pygame.draw.rect(scr_v, (dark[2]), self.Ablock, 1)
        self.cr_0 = pygame.draw.rect(scr_v, (dark[2]), self.Bblock, 1)
        self.cr_1 = pygame.draw.rect(scr_v, (dark[2]), self.Cblock, 1)
        self.cr_2 = pygame.draw.rect(scr_v, (dark[2]), self.Dblock, 1)
        self.cr_3 = pygame.draw.rect(scr_v, (dark[2]), self.Eblock, 1)
        self.cr_44 = pygame.draw.rect(scr_v, (dark[2]), self.Fblock, 1)
        self.cr_5 = pygame.draw.rect(scr_v, (dark[2]), self.Gblock, 1)
        self.cr_6 = pygame.draw.rect(scr_v, (dark[2]), self.Hblock, 1)

    def selector00(self):
        self.cr = pygame.draw.rect(scr_v, (dark[2]), self.Ablock)
    def selector2(self):
        self.cr_0 = pygame.draw.rect(scr_v, (dark[2]), self.Bblock)
    def selector3(self):
        self.cr_1 = pygame.draw.rect(scr_v, (dark[2]), self.Cblock)
    def selector4(self):
        self.cr_2 = pygame.draw.rect(scr_v, (dark[2]), self.Dblock)
    def selector5(self):
        self.cr_3 = pygame.draw.rect(scr_v, (dark[2]), self.Eblock)
    def selector6(self):
        self.cr_44 = pygame.draw.rect(scr_v, (dark[2]), self.Fblock)
    def selector7(self):
        self.cr_5 = pygame.draw.rect(scr_v, (dark[2]), self.Gblock)
    def selector8(self):
        self.cr_6 = pygame.draw.rect(scr_v, (dark[2]), self.Hblock)

    def detect_coll(self):
        self.cr = pygame.draw.rect(scr_v, (COLORS[0]), self.Ablock)
    def detect_coll_2(self):
        self.cr_0 = pygame.draw.rect(scr_v, (COLORS[0]), self.Bblock)
    def detect_coll_3(self):
        self.cr_1 = pygame.draw.rect(scr_v, (COLORS[0]), self.Cblock)
    def detect_coll_4(self):
        self.cr_2 = pygame.draw.rect(scr_v, (COLORS[0]), self.Dblock)
    def detect_coll_5(self):
        self.cr_3 = pygame.draw.rect(scr_v, (COLORS[0]), self.Eblock)
    def detect_coll_6(self):
        self.cr_44 = pygame.draw.rect(scr_v, (COLORS[0]), self.Fblock)
    def detect_coll_7(self):
        self.cr_5 = pygame.draw.rect(scr_v, (COLORS[0]), self.Gblock)
    def detect_coll_8(self):
        self.cr_6 = pygame.draw.rect(scr_v, (COLORS[0]), self.Hblock)


    # def file2(self, bck00, bck0, bck1, bck2, bck3, bck4 ,bck5, bck6 ):
class Makker:
    def __init__(self, bck00, bck0, bck1, bck2, bck3, bck4, bck5  , bck6):
        self.bck00 = bck00
        self.bck0 = bck0
        self.bck1 = bck1
        self.bck2 = bck2
        self.bck3 = bck3
        self.bck4 = bck4
        self.bck5 = bck5

        self.bck6 = bck6
        # comments comments
    def file2(self):
        self.bck00 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck00 ,1)
        self.bck_0 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck0 ,1)
        self.bck_1 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck1 ,1)
        self.bck_2 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck2 ,1)
        self.bck_3 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck3 ,1)
        self.bck_4 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck4 ,1)
        self.bck_5 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck5 ,1)
        self.bck_6 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck6 ,1)


    def sectionchange(self):
        self.bck00 = pygame.draw.rect(scr_v, (dark[2]), self.bck00 ,1)
        self.bck_0 = pygame.draw.rect(scr_v, (dark[2]), self.bck0 ,1)
        self.bck_1 = pygame.draw.rect(scr_v, (dark[2]), self.bck1 ,1)
        self.bck_2 = pygame.draw.rect(scr_v, (dark[2]), self.bck2 ,1)
        self.bck_3 = pygame.draw.rect(scr_v, (dark[2]), self.bck3 ,1)
        self.bck_4 = pygame.draw.rect(scr_v, (dark[2]), self.bck4 ,1)
        self.bck_5 = pygame.draw.rect(scr_v, (dark[2]), self.bck5 ,1)
        self.bck_6 = pygame.draw.rect(scr_v, (dark[2]), self.bck6 ,1)
    def sectionchange_LAST(self):
        self.bck00 = pygame.draw.rect(scr_v, (dark[2]), self.bck00)
    def sectionchange_0(self):
        self.bck_0 = pygame.draw.rect(scr_v, (dark[2]), self.bck0 )
    def sectionchange_1(self):
        self.bck_1 = pygame.draw.rect(scr_v, (dark[2]), self.bck1 )
    def sectionchange_2(self):
        self.bck_2 = pygame.draw.rect(scr_v, (dark[2]), self.bck2 )
    def sectionchange_3(self):
        self.bck_3 = pygame.draw.rect(scr_v, (dark[2]), self.bck3 )
    def sectionchange_4(self):
        self.bck_4 = pygame.draw.rect(scr_v, (dark[2]), self.bck4 )
    def sectionchange_5(self):
        self.bck_5 = pygame.draw.rect(scr_v, (dark[2]), self.bck5 )
    def sectionchange_6(self):
        self.bck_6 = pygame.draw.rect(scr_v, (dark[2]), self.bck6 )


    def detects_ctl(self):
        self.bck00 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck00)
    def detects_ctl_0(self):
        self.bck_0 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck0 )
    def detects_ctl_1(self):
        self.bck_1 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck1 )
    def detects_ctl_2(self):
        self.bck_2 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck2 )
    def detects_ctl_3(self):
        self.bck_3 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck3 )
    def detects_ctl_4(self):
        self.bck_4 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck4 )
    def detects_ctl_5(self):
        self.bck_5 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck5 )
    def detects_ctl_6(self):
        self.bck_6 = pygame.draw.rect(scr_v, (COLORS[0]), self.bck6 )


class Makjob:
    "style"
    def __init__(self, mkbck00, mkbck_v, mkbck_w, mkbck_x, mkbck_y, mkbck_z , mkbck_0, mkbck_1):
        self.mkbck00 = mkbck00
        self.mkbck_v = mkbck_v
        self.mkbck_w = mkbck_w
        self.mkbck_x = mkbck_x
        self.mkbck_y = mkbck_y
        self.mkbck_z = mkbck_z
        self.mkbck_0 = mkbck_0
        self.mkbck_1 = mkbck_1
        # self.operators = lambda operators: operators * 2
    # def file3(self, mkbck00, mkbck_v, mkbck_w, mkbck_x, mkbck_y, mkbck_z, mkbck_0 ):
    def file3(self):
        self.mkbck = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck00, 1)
        self.mkbck_A = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_v, 1)
        self.mkbck_B = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_w, 1)
        self.mkbck_C = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_x, 1)
        self.mkbck_D = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_y, 1)
        self.mkbck_E = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_z, 1)
        self.mkbck_F = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_0, 1)
        self.mkbck_G = pygame.draw.rect(scr_v, (COLORS[0]), self.mkbck_1, 1)
        # self.mkbck = pygame.draw.rect(scr_v, (COLORS[0]), self.)

    def changeassign(self):
        self.mkbck = pygame.draw.rect(scr_v, (dark[2]), self.mkbck00, 1)
        self.mkbck_A = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_v, 1)
        self.mkbck_B = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_w, 1)
        self.mkbck_C = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_x, 1)
        self.mkbck_D = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_y, 1)
        self.mkbck_E = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_z, 1)
        self.mkbck_F = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_0, 1)
        self.mkbck_G = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_1, 1)
    def reassignB(self):
        self.mkbck = pygame.draw.rect(scr_v, (dark[2]), self.mkbck00)
    def reassign_0(self):
        self.mkbck_A = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_v)
    def reassign_1(self):
        self.mkbck_B = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_w)
    def reassign_2(self):
        self.mkbck_C = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_x)
    def reassign_3(self):
        self.mkbck_D = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_y)
    def reassign_4(self):
        self.mkbck_E = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_z)
    def reassign_5(self):
        self.mkbck_F = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_0)
    def reassign_6(self):
        self.mkbck_G = pygame.draw.rect(scr_v, (dark[2]), self.mkbck_1)
        #Use lambda X:X = X
    def detecting_sensor(self):
        self.mkbck = pygame.draw.rect(scr_v, (dark[0]), self.mkbck00)
    def detecting_sensor_0(self):
        self.mkbck_A = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_v)
    def detecting_sensor_1(self):
        self.mkbck_B = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_w)
    def detecting_sensor_2(self):
        self.mkbck_C = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_x)
    def detecting_sensor_3(self):
        self.mkbck_D = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_y)
    def detecting_sensor_4(self):
        self.mkbck_E = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_z)
    def detecting_sensor_5(self):
        self.mkbck_F = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_0)
    def detecting_sensor_6(self):
        self.mkbck_G = pygame.draw.rect(scr_v, (dark[0]), self.mkbck_1)

class Operatorss:
        def __init__(self, cblockc, cablockc , cbblockc, ccblockc, cdblockc , ceblockc, cfblockc):
            self.cblockc = cblockc
            self.cablockc = cablockc
            self.cbblockc = cbblockc
            self.ccblockc = ccblockc
            self.cdblockc = cdblockc
            self.ceblockc = ceblockc
            self.cfblockc = cfblockc
            #self.cgblockc = cgblockc
            #self.chblockc = chblockc
        def combinE_F(self,cblockc, cablockc , cbblockc, ccblockc, cdblockc , ceblockc , cfblockc):
            self.combinE = pygame.draw.rect(scr_v, (dark[5]), cblockc, 1)
            self.combinEA = pygame.draw.rect(scr_v, (dark[5]), cablockc, 1)
            self.combinEB = pygame.draw.rect(scr_v, (dark[5]), cbblockc, 1)
            self.combinEC = pygame.draw.rect(scr_v, (dark[5]), ccblockc, 1)
            self.combinED = pygame.draw.rect(scr_v, (dark[5]), cdblockc, 1)
            self.combinEE = pygame.draw.rect(scr_v, (dark[5]), ceblockc, 1)
            self.combinEF = pygame.draw.rect(scr_v, (dark[5]), cfblockc, 1)
            # self.combinEG = pygame.draw.rect(scr_v, (COLORS[0]), cgblockc, 1)
            # self.combinEH = pygame.draw.rect(scr_v, (COLORS[0]), chblockc, 1)
class Display_manger:
    def __init__(self, man_config):
        self.man_config = pygame.draw.rect(scr_v, (COLORS[0]), man_config, 1)
    def manager(self):
        return self.man_config

    def night_h(self, disable_conf):
        self.off_time = pygame.draw.rect(scr_v, (dark[2]), disable_conf, 1)
        #return off_time
# def var_theme():
#     scr_v.fill(COLORS[0])
    # pygame.display.update()
    # eturn BuilderNewTHEme()


def BuilderNewTHEme():
    pygame.init()
    global scr_v
    global POSXH
    global POSYW
    run = True
    while run:
        scr_v.fill(COLORS[0])
        POSXH, POSYW = pygame.mouse.get_pos()
        print('new_pos ', POSXH, POSYW , ' enpy}') # flag possicion
            # print(ick_up)
            # global ick_up
            #if ick_up:
            #    print(ick_up)
            #     __function()

        settup = Make(BLOCK, BLOCK_0, BLOCK_1, BLOCK_2, BLOCK_3, BLOCKC_4, BLOCK_5, BLOCK_6)
        settup.selector()
        setobk = Makker(A_BLOCK, B_BLOCK_0, C_BLOCK_1, D_BLOCK_2, E_BLOCK_3, F_BLOCKC_4, G_BLOCK_5, H_BLOCK_6)
        setobk.sectionchange()
        settbck = Makjob(BA_BLOCK, BB_BLOCK_0, BC_BLOCK_1, BD_BLOCK_2, BE_BLOCK_3, BF_BLOCKC_4, BG_BLOCK_5, BH_BLOCK_6)
        settbck.changeassign()
        new_theme = Settings_theme(theme_c)
        new_theme.theobscure(theme_c)


        oper_change = Operatorss(CA_BLOCK, CB_BLOCK_0, CC_BLOCK_1, CD_BLOCK_2, CE_BLOCK_3, CF_BLOCK_4, CG_BLOCK_5)
        oper_change.combinE_F(CA_BLOCK, CB_BLOCK_0, CC_BLOCK_1, CD_BLOCK_2, CE_BLOCK_3, CF_BLOCK_4, CG_BLOCK_5)
        ddis = Display_manger(DISPLAY_CHANGE)
        ddis.night_h(DISPLAY_CHANGE)
        incrementr  = 0
        posx, posy = pygame.mouse.get_pos()
        incrementr  = 0
        check_point  = [ 'BLOCK', 'BLOCK_0', 'BLOCK_1', 'BLOCK_2', 'BLOCK_3', 'BLOCK_4', 'BLOCK_5', 'BLOCK_6' ]
        # for warrent in check_point:
        #if check_point == BLOCK:
        for t in [1 , 2, 3 , 4, 5, 6, 7, 8, 9 ]:
            incrementr += 1
            if t == 1:
                if BLOCK.collidepoint((POSXH, POSYW)):
                    settup.selector00()
                    pygame.display.update()
                elif A_BLOCK.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_LAST()
                    pygame.display.update()
                elif BA_BLOCK.collidepoint((POSXH, POSYW)):
                    settbck.reassignB()
                    pygame.display.update()


            elif t == 2:
                if BLOCK_0.collidepoint((posx, posy)):
                    settup.selector2()
                    pygame.display.update()
                elif B_BLOCK_0.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_0()
                    pygame.display.update()
                elif BB_BLOCK_0.collidepoint((POSXH, POSYW)):
                    settbck.reassign_0()
                    pygame.display.update()
                print(t)
                # break
                # return t
            elif t == 3:
                if BLOCK_1.collidepoint((posx, posy)):
                    settup.selector3()
                    pygame.display.update()
                elif C_BLOCK_1.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_1()
                    pygame.display.update()
                elif BC_BLOCK_1.collidepoint((POSXH, POSYW)):
                    settbck.reassign_1()
                    pygame.display.update()
                print(t)
                # break
                #return t
            elif t == 4:
                if BLOCK_2.collidepoint((posx, posy)):
                    settup.selector4()
                    pygame.display.update()
                elif D_BLOCK_2.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_2()
                    pygame.display.update()
                elif BD_BLOCK_2.collidepoint((POSXH, POSYW)):
                    settbck.reassign_2()
                    pygame.display.update()

                print(t)
            elif t == 5:
                if BLOCK_3.collidepoint((posx, posy)):
                    settup.selector5()
                    pygame.display.update()
                elif E_BLOCK_3.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_3()
                    pygame.display.update()
                elif BE_BLOCK_3.collidepoint((POSXH, POSYW)):
                    settbck.reassign_3()
                    pygame.display.update()
                print(t)
            elif t == 6:
                if BLOCKC_4.collidepoint((POSXH, POSYW)):
                    settup.selector6()
                    pygame.display.update()
                elif F_BLOCKC_4.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_4()
                    pygame.display.update()
                elif BF_BLOCKC_4.collidepoint((POSXH, POSYW)):
                    settbck.reassign_4()
                    pygame.display.update()

                print(t)
            elif t == 7:
                if BLOCK_5.collidepoint((posx, posy)):
                    settup.selector7()
                    pygame.display.update()
                elif G_BLOCK_5.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_5()
                    pygame.display.update()
                elif BG_BLOCK_5.collidepoint((POSXH, POSYW)):
                    settbck.reassign_5()
                    pygame.display.update()

                print(t)
            elif t == 8:
                if BLOCK_6.collidepoint((posx, posy)):
                    settup.selector8()
                    pygame.display.update()
                elif H_BLOCK_6.collidepoint((POSXH, POSYW)):
                    setobk.sectionchange_6()
                    pygame.display.update()
                elif BH_BLOCK_6.collidepoint((POSXH, POSYW)):
                    settbck.reassign_6()
                    pygame.display.update()

                print(t)



        ick_up = False

        for z in pygame.event.get():
            if z.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            key = pygame.key.get_pressed()
            if z.type == pygame.KEYDOWN:
                if z.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if z.type == pygame.MOUSEBUTTONDOWN:
                if z.button == 1:
                    ick_up = True
                    # print(ick_up)

        pygame.display.init()
        pygame.display.update()






class Settings_theme:

    def __init__(self, make_color):
        self.make_color = make_color
    def light_theme(self, p):
        print('color building')
        self.light = pygame.draw.rect(scr_v, (COLORS[0]), p, 1)
        # pass
    def theobscure(self, nighttheme):
        pass
        self.obscure = pygame.draw.rect(scr_v, (dark[2]), nighttheme, 1)


    # global click_on
    # if changer.collidepoint((POSXH, POSYW)):
        # if click_on:

            # print('¡collision')
            # scr_v.fill(COLORS[0])
            # pygame.display.update()
    # settup

    # icoN = pygame.image.load('/assets/config.jpg')

    # propertYSs ?

def __function(posx=POSXH , posy=POSYW):
    # scr_v = pygame.display.set_mode((posy, posx), 32)
    #  how render  in build in mode  32 now border now tool border kill window o minimaze window
    global scr_v
    # global click_on
    pygame.display.set_caption('Calpy')
    run = True
    while run:
        scr_v.fill(COLORS[2])
        POSXH , POSYW = pygame.mouse.get_pos() # flag possicion

        print(f"is {POSXH, POSYW}it position ")

        settup = Make(BLOCK, BLOCK_0, BLOCK_1, BLOCK_2, BLOCK_3, BLOCKC_4, BLOCK_5, BLOCK_6)
        settup.builder()
        setobk = Makker(A_BLOCK, B_BLOCK_0, C_BLOCK_1, D_BLOCK_2, E_BLOCK_3, F_BLOCKC_4, G_BLOCK_5, H_BLOCK_6)
        setobk.file2()
        settbck = Makjob(BA_BLOCK, BB_BLOCK_0, BC_BLOCK_1, BD_BLOCK_2, BE_BLOCK_3, BF_BLOCKC_4, BG_BLOCK_5, BH_BLOCK_6)
        settbck.file3()
        new_lighttheme = Settings_theme(theme_c)
        new_lighttheme.light_theme(theme_c)
        # mouse = pygame.mouse.get_pos()
        posx, posy = pygame.mouse.get_pos()

        uper_change = Operatorss(CA_BLOCK, CB_BLOCK_0, CC_BLOCK_1, CD_BLOCK_2, CE_BLOCK_3, CF_BLOCK_4,CG_BLOCK_5)
        uper_change.combinE_F(CA_BLOCK, CB_BLOCK_0, CC_BLOCK_1, CD_BLOCK_2, CE_BLOCK_3, CF_BLOCK_4, CG_BLOCK_5)
        ddis = Display_manger(DISPLAY_CHANGE)
        ddis.manager()

        if theme_c.collidepoint((posx, posy)):
            if click_on:
                BuilderNewTHEme()
        incrementr  = 0
        check_point  = [ 'BLOCK', 'BLOCK_0', 'BLOCK_1', 'BLOCK_2', 'BLOCK_3', 'BLOCK_4', 'BLOCK_5', 'BLOCK_6' ]
        # for warrent in check_point:
        incrementr += 1
        #if check_point == BLOCK:
        for t in [1 , 2, 3 , 4, 5, 7, 8, 9,10  ]:
            if t == 1:
                if BLOCK.collidepoint((POSXH, POSYW)):
                    settup.detect_coll()
                    pygame.display.update()
                elif A_BLOCK.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl()
                    pygame.display.update()
                elif BA_BLOCK.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor()
                    pygame.display.update()


            elif t == 2:
                if BLOCK_0.collidepoint((posx, posy)):
                    settup.detect_coll_2()
                    pygame.display.update()
                elif B_BLOCK_0.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_0()
                    pygame.display.update()
                elif BB_BLOCK_0.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_0()
                    pygame.display.update()
                print(t)
                # break
                # return t
            elif t == 3:
                if BLOCK_1.collidepoint((posx, posy)):
                    settup.detect_coll_3()
                    pygame.display.update()
                elif C_BLOCK_1.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_1()
                    pygame.display.update()
                elif BC_BLOCK_1.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_1()
                    pygame.display.update()
                print(t)
                # break
                #return t
            elif t == 4:
                if BLOCK_2.collidepoint((posx, posy)):
                    settup.detect_coll_4()
                    pygame.display.update()
                elif D_BLOCK_2.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_2()
                    pygame.display.update()
                elif BD_BLOCK_2.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_2()
                    pygame.display.update()

                print(t)
            elif t == 5:
                if BLOCK_3.collidepoint((posx, posy)):
                    settup.detect_coll_5()
                    pygame.display.update()
                elif E_BLOCK_3.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_3()
                    pygame.display.update()
                elif BE_BLOCK_3.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_3()
                    pygame.display.update()
                print(t)
            elif t == 9:
                if BLOCKC_4.collidepoint((POSXH, POSYW)):
                    settup.detect_coll_6()
                    pygame.display.update()
                elif F_BLOCKC_4.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_4()
                    pygame.display.update()
                elif BF_BLOCKC_4.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_4()
                    pygame.display.update()

                print(t)
            elif t == 7:
                if BLOCK_5.collidepoint((posx, posy)):
                    settup.detect_coll_7()
                    pygame.display.update()
                elif G_BLOCK_5.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_5()
                    pygame.display.update()
                elif BG_BLOCK_5.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_5()
                    pygame.display.update()

                print(t)
            elif t == 8:
                if BLOCK_6.collidepoint((posx, posy)):
                    settup.detect_coll_8()
                    pygame.display.update()
                elif H_BLOCK_6.collidepoint((POSXH, POSYW)):
                    setobk.detects_ctl_6()
                    pygame.display.update()
                elif BH_BLOCK_6.collidepoint((POSXH, POSYW)):
                    settbck.detecting_sensor_6()
                    pygame.display.update()

                print(t)

            #    print(t)
                #        return warrent
                # return incrementr

            #print( incrementr , warrent)
            # for zap in :
            #     print(zap)
            #if incrementr == 1:
            #if :
            # elif incrementr == 2:
            #if BLOCK_0.collidepoint((POSXH, POSYW)):
            #    settup.detect_coll()
            #    pygame.display.update()
            #     return incrementr



        # print(posx, posy)
        # for whant in ( BLOCK, BLOCK_0, BLOCK_1, BLOCK_2, BLOCK_3, BLOCK_4, BLOCK_5, BLOCK_6  ):
        #     if whant.collidepoint((posx, posy)):
        #         settbck.detecting_sensor()
        #     if click_on:
        #         BuilderNewTHEme()

                # from presentation import *
                # present()

        print('!collision')
        #settup1 = Make(A_BLOCK, B_BLOCK_0, C_BLOCK_1, D_BLOCK_2, E_BLOCK_3, F_BLOCK_4, G_BLOCK_5, H_BLOCK_6)

        # settup.file2(A_BLOCK, B_BLOCK_0, C_BLOCK_1, D_BLOCK_2, E_BLOCK_3, F_BLOCK_4, G_BLOCK_5, H_BLOCK_6)
        #settup1.file2()
        # settup.file3(BA_BLOCK, BB_BLOCK_0, BC_BLOCK_1, BD_BLOCK_2, BE_BLOCK_3, BF_BLOCK_4, BG_BLOCK_5, BH_BLOCK_6)
        # settup2 = Make(BA_BLOCK, BB_BLOCK_0, BC_BLOCK_1, BD_BLOCK_2, BE_BLOCK_3, BF_BLOCK_4, BG_BLOCK_5, BH_BLOCK_6)
        # settup2.file3()


        click_on = False

        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


            key = pygame.key.get_pressed()
            if x.type == pygame.KEYDOWN:
                if x.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if x.type == MOUSEBUTTONDOWN:
                if x.button == 1:
                    click_on = True


        pygame.display.update()




# nv =  Make( 'tramp' , 'crash' , 'red',  10 )




# print('this is load',nv )
# def function(x):
    # print('hellow_ freind  ',x)
    # sys.exit(0)
    # # pass
#
#
# if __name__ == '__main__':
#
    # print(function(int(sys.argv[1])))
if __name__ == '__main__':

    __function()
