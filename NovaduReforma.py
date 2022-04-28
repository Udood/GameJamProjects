import pygame
import random
import pygame.freetype

# our special type of Sprite
class Fanta(pygame.sprite.Sprite):
    def __init__(self, image, xpos, ypos):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)
       self.image = image
       self.rect = self.image.get_rect()
       self.rect.topleft = [xpos, ypos]
       
       self.next_update_time = 0
       self.clicked = False
       self.base_delay = 3390
       self.delay = 3390

    def update(self, current_time, all_sprites):
        if self.clicked == True:
            self.next_update_time = current_time
        if self.next_update_time <= current_time:
            if self.clicked == False and self.next_update_time > 0:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                
            self.clicked = False
            self.delay = self.base_delay - 20*(len(all_sprites)-1)
            self.rect.center = all_sprites[random.randint(0, len(all_sprites)-1)].rect.center
            self.next_update_time = current_time + self.delay

def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("Assets/logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Novadu reforma")

    # loop music non-stop
    pygame.mixer.music.load('Assets/welcome.mp3')
    pygame.mixer.music.play(-1)
     
    # create a white surface on screen
    screen = pygame.display.set_mode((650, 400))
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # init Sprite list
    all_sprites = pygame.sprite.Group()
    novadi = Fanta(pygame.image.load("Assets/Map/latvija.png"), 0, 0)
    aizkraukle = Fanta(pygame.image.load("Assets/Map/Aizkraukle_339x210.png"), 339, 210)
    aizkraukle_1 = Fanta(pygame.image.load("Assets/Map/Aizkraukle_1_336x230.png"), 336, 230)
    aizkraukle_2 = Fanta(pygame.image.load("Assets/Map/Aizkraukle_2_386x204.png"), 386, 204)
    aizkraukle_3 = Fanta(pygame.image.load("Assets/Map/Aizkraukle_3_382x233.png"), 382, 233)
    aizkraukle_4 = Fanta(pygame.image.load("Assets/Map/Aizkraukle_4_355x262.png"), 355, 262)
    aluksne = Fanta(pygame.image.load("Assets/Map/Aluksne_474x74.png"), 474, 74)
    aluksne_1 = Fanta(pygame.image.load("Assets/Map/Aluksne_1_474x79.png"), 474, 79)
    aluksne_2 = Fanta(pygame.image.load("Assets/Map/Aluksne_2_501x76.png"), 501, 76)
    aluksne_3 = Fanta(pygame.image.load("Assets/Map/Aluksne_3_530x81.png"), 530, 81)
    aluksne_4 = Fanta(pygame.image.load("Assets/Map/Aluksne_4_558x86.png"), 558, 86)
    balvi = Fanta(pygame.image.load("Assets/Map/Balvi_531x125.png"), 531, 125)
    balvi_1 = Fanta(pygame.image.load("Assets/Map/Balvi_1_534x135.png"), 534, 135)
    balvi_2 = Fanta(pygame.image.load("Assets/Map/Balvi_2_525x164.png"), 525, 164)
    balvi_3 = Fanta(pygame.image.load("Assets/Map/Balvi_3_566x122.png"), 566, 122)
    balvi_4 = Fanta(pygame.image.load("Assets/Map/Balvi_4_563x161.png"), 563, 161)
    bauska = Fanta(pygame.image.load("Assets/Map/Bauska_265x225.png"), 265, 225)
    bauska_1 = Fanta(pygame.image.load("Assets/Map/Bauska_1_276x226.png"), 276, 226)
    bauska_2 = Fanta(pygame.image.load("Assets/Map/Bauska_2_303x224.png"), 303, 224)
    bauska_3 = Fanta(pygame.image.load("Assets/Map/Bauska_3_264x257.png"), 264, 257)
    bauska_4 = Fanta(pygame.image.load("Assets/Map/Bauska_4_303x257.png"), 303, 257)
    cesis = Fanta(pygame.image.load("Assets/Map/Cesis_349x103.png"), 349, 103)
    cesis_1 = Fanta(pygame.image.load("Assets/Map/Cesis_1_350x102.png"), 350, 102)
    cesis_2 = Fanta(pygame.image.load("Assets/Map/Cesis_2_359x143.png"), 359, 143)
    cesis_3 = Fanta(pygame.image.load("Assets/Map/Cesis_3_398x104.png"), 398, 104)
    cesis_4 = Fanta(pygame.image.load("Assets/Map/Cesis_4_400x144.png"), 400, 144)
    daugavpils = Fanta(pygame.image.load("Assets/Map/Daugavpils_441x305.png"), 441, 305)
    daugavpils_1 = Fanta(pygame.image.load("Assets/Map/Daugavpils_1_440x309.png"), 440, 309)
    daugavpils_2 = Fanta(pygame.image.load("Assets/Map/Daugavpils_2_496x309.png"), 496, 309)
    daugavpils_3 = Fanta(pygame.image.load("Assets/Map/Daugavpils_3_469x340.png"), 469, 340)
    daugavpils_4 = Fanta(pygame.image.load("Assets/Map/Daugavpils_4_500x340.png"), 500, 340)
    dobele = Fanta(pygame.image.load("Assets/Map/Dobele_169x210.png"), 169, 210)
    dobele_1 = Fanta(pygame.image.load("Assets/Map/Dobele_1_170x221.png"), 170, 221)
    dobele_2 = Fanta(pygame.image.load("Assets/Map/Dobele_2_163x245.png"), 163, 245)
    dobele_3 = Fanta(pygame.image.load("Assets/Map/Dobele_3_203x213.png"), 203, 213)
    dobele_4 = Fanta(pygame.image.load("Assets/Map/Dobele_4_197x250.png"), 197, 250)
    gulbene = Fanta(pygame.image.load("Assets/Map/Gulbene_456x114.png"), 456, 114)
    #gulbene_1 = Fanta(pygame.image.load("Assets/Map/Gulbene_1_556x177.png"), 556, 177)
    gulbene_2 = Fanta(pygame.image.load("Assets/Map/Gulbene_2_458x151.png"), 458, 140)
    gulbene_3 = Fanta(pygame.image.load("Assets/Map/Gulbene_3_503x124.png"), 503, 124)
    gulbene_4 = Fanta(pygame.image.load("Assets/Map/Gulbene_4_497x141.png"), 497, 141)
    jekabpils = Fanta(pygame.image.load("Assets/Map/Jekabpils_398x229.png"), 398, 229)
    jekabpils_1 = Fanta(pygame.image.load("Assets/Map/Jekabpils_1_388x265.png"), 388, 265)
    jekabpils_2 = Fanta(pygame.image.load("Assets/Map/Jekabpils_2_417x235.png"), 417, 235)
    jekabpils_3 = Fanta(pygame.image.load("Assets/Map/Jekabpils_3_431x275.png"), 431, 275)
    jekabpils_4 = Fanta(pygame.image.load("Assets/Map/Jekabpils_4_453x231.png"), 453, 231)
    jelgava = Fanta(pygame.image.load("Assets/Map/Jelgava_228x196.png"), 228, 196)
    jelgava_1 = Fanta(pygame.image.load("Assets/Map/Jelgava_1_224x241.png"), 224, 241)
    jelgava_2 = Fanta(pygame.image.load("Assets/Map/Jelgava_2_228x194.png"), 228, 194)
    jelgava_3 = Fanta(pygame.image.load("Assets/Map/Jelgava_3_247x214.png"), 247, 216)
    jelgava_4 = Fanta(pygame.image.load("Assets/Map/Jelgava_4_249x240.png"), 249, 240)
    kraslava = Fanta(pygame.image.load("Assets/Map/Kraslava_534x289.png"), 534, 289)
    kraslava_1 = Fanta(pygame.image.load("Assets/Map/Kraslava_1_548x291.png"), 548, 291)
    kraslava_2 = Fanta(pygame.image.load("Assets/Map/Kraslava_2_535x318.png"), 535, 318)
    kraslava_3 = Fanta(pygame.image.load("Assets/Map/Kraslava_3_580x296.png"), 580, 296)
    kraslava_4 = Fanta(pygame.image.load("Assets/Map/Kraslava_4_570x327.png"), 570, 327)
    kraslava_4 = Fanta(pygame.image.load("Assets/Map/Kraslava_4_570x327.png"), 570, 327)
    kuldiga = Fanta(pygame.image.load("Assets/Map/Kuldiga_62x153.png"), 62, 153)
    kuldiga_1 = Fanta(pygame.image.load("Assets/Map/Kuldiga_1_59x157.png"), 59, 157)
    kuldiga_2 = Fanta(pygame.image.load("Assets/Map/Kuldiga_2_80x197.png"), 80, 197)
    kuldiga_3 = Fanta(pygame.image.load("Assets/Map/Kuldiga_3_78x155.png"), 78, 155)
    kuldiga_4 = Fanta(pygame.image.load("Assets/Map/Kuldiga_4_114x151.png"), 114, 151)
    liepaja = Fanta(pygame.image.load("Assets/Map/Liepaja_11x184.png"), 11, 184)
    liepaja_1 = Fanta(pygame.image.load("Assets/Map/Liepaja_1_7x254.png"), 7, 254)
    liepaja_2 = Fanta(pygame.image.load("Assets/Map/Liepaja_2_13x211.png"), 13, 211)
    liepaja_3 = Fanta(pygame.image.load("Assets/Map/Liepaja_3_21x181.png"), 21, 181)
    liepaja_4 = Fanta(pygame.image.load("Assets/Map/Liepaja_4_43x212.png"), 43, 212)
    liepaja_5 = Fanta(pygame.image.load("Assets/Map/Liepaja_5_41x250.png"), 39, 250)
    limbazi = Fanta(pygame.image.load("Assets/Map/Limbazi_304x24.png"), 304, 24)
    limbazi_1 = Fanta(pygame.image.load("Assets/Map/Limbazi_1_298x26.png"), 298, 26)
    limbazi_2 = Fanta(pygame.image.load("Assets/Map/Limbazi_2_306x75.png"), 306, 75)
    limbazi_3 = Fanta(pygame.image.load("Assets/Map/Limbazi_3_327x24.png"), 327, 24)
    limbazi_4 = Fanta(pygame.image.load("Assets/Map/Limbazi_4_326x74.png"), 326, 74)
    ludza = Fanta(pygame.image.load("Assets/Map/Ludza_551x190.png"), 551, 190)
    ludza_1 = Fanta(pygame.image.load("Assets/Map/Ludza_1_557x198.png"), 557, 198)
    ludza_2 = Fanta(pygame.image.load("Assets/Map/Ludza_2_585x243.png"), 585, 243)
    ludza_3 = Fanta(pygame.image.load("Assets/Map/Ludza_3_596x191.png"), 596, 191)
    ludza_4 = Fanta(pygame.image.load("Assets/Map/Ludza_4_612x243.png"), 612, 243)
    madona = Fanta(pygame.image.load("Assets/Map/Madona_409x163.png"), 409, 163)
    madona_1 = Fanta(pygame.image.load("Assets/Map/Madona_1_405x178.png"), 405, 178)
    madona_2 = Fanta(pygame.image.load("Assets/Map/Madona_2_433x162.png"), 433, 162)
    madona_3 = Fanta(pygame.image.load("Assets/Map/Madona_3_433x199.png"), 433, 199)
    madona_4 = Fanta(pygame.image.load("Assets/Map/Madona_4_465x167.png"), 465, 167)
    madona_5 = Fanta(pygame.image.load("Assets/Map/Madona_5_470x203.png"), 470, 203)
    ogre = Fanta(pygame.image.load("Assets/Map/Ogre_319x181.png"), 319, 181)
    ogre_1 = Fanta(pygame.image.load("Assets/Map/Ogre_1_320x188.png"), 320, 188)
    ogre_2 = Fanta(pygame.image.load("Assets/Map/Ogre_2_323x211.png"), 323, 211)
    ogre_3 = Fanta(pygame.image.load("Assets/Map/Ogre_3_369x183.png"), 369, 183)
    ogre_4 = Fanta(pygame.image.load("Assets/Map/Ogre_4_404x178.png"), 404, 178)
    preili = Fanta(pygame.image.load("Assets/Map/Preili_462x244.png"), 462, 244)
    preili_1 = Fanta(pygame.image.load("Assets/Map/Preili_1_463x252.png"), 463, 252)
    preili_2 = Fanta(pygame.image.load("Assets/Map/Preili_2_502x250.png"), 502, 250)
    rezekne = Fanta(pygame.image.load("Assets/Map/Rezekne_520x201.png"), 520, 201)
    #rezekne_1 = Fanta(pygame.image.load("Assets/Map/Rezekne_1_514x265.png"), 514, 265)
    rezekne_2 = Fanta(pygame.image.load("Assets/Map/Rezekne_2_530x259.png"), 530, 259)
    rezekne_3 = Fanta(pygame.image.load("Assets/Map/Rezekne_3_541x208.png"), 541, 208)
    rezekne_4 = Fanta(pygame.image.load("Assets/Map/Rezekne_4_559x256.png"), 559, 256)
    riga = Fanta(pygame.image.load("Assets/Map/Riga_247x134.png"), 247, 134)
    riga_1 = Fanta(pygame.image.load("Assets/Map/Riga_1_230x178.png"), 230, 178)
    riga_2 = Fanta(pygame.image.load("Assets/Map/Riga_2_276x147.png"), 276, 147)
    riga_3 = Fanta(pygame.image.load("Assets/Map/Riga_3_254x201.png"), 254, 201)
    riga_4 = Fanta(pygame.image.load("Assets/Map/Riga_4_307x129.png"), 307, 129)
    riga_5 = Fanta(pygame.image.load("Assets/Map/Riga_5_304x161.png"), 304, 161)
    saldus = Fanta(pygame.image.load("Assets/Map/Saldus_104x192.png"), 104, 192)
    saldus_1 = Fanta(pygame.image.load("Assets/Map/Saldus_1_118x187.png"), 118, 187)
    saldus_2 = Fanta(pygame.image.load("Assets/Map/Saldus_2_140x201.png"), 140, 201)
    saldus_3 = Fanta(pygame.image.load("Assets/Map/Saldus_3_100x235.png"), 100, 235)
    saldus_4 = Fanta(pygame.image.load("Assets/Map/Saldus_4_139x236.png"), 139, 236)
    talsi = Fanta(pygame.image.load("Assets/Map/Talsi_128x61.png"), 128, 61)
    talsi_1 = Fanta(pygame.image.load("Assets/Map/Talsi_1_126x61.png"), 126, 61)
    talsi_2 = Fanta(pygame.image.load("Assets/Map/Talsi_2_128x120.png"), 128, 120)
    talsi_3 = Fanta(pygame.image.load("Assets/Map/Talsi_3_159x83.png"), 159, 83)
    talsi_4 = Fanta(pygame.image.load("Assets/Map/Talsi_4_162x114.png"), 162, 114)
    tukums = Fanta(pygame.image.load("Assets/Map/Tukums_150x137.png"), 150, 137)
    #tukums_1 = Fanta(pygame.image.load("Assets/Map/Tukums_1_188x234.png"), 188, 180)
    tukums_2 = Fanta(pygame.image.load("Assets/Map/Tukums_2_148x158.png"), 148, 158)
    tukums_3 = Fanta(pygame.image.load("Assets/Map/Tukums_3_153x186.png"), 153, 186)
    tukums_4 = Fanta(pygame.image.load("Assets/Map/Tukums_4_194x185.png"), 194, 185)
    valka = Fanta(pygame.image.load("Assets/Map/Valka_406x27.png"), 406, 27)
    valka_1 = Fanta(pygame.image.load("Assets/Map/Valka_1_406x35.png"), 406, 35)
    valka_2 = Fanta(pygame.image.load("Assets/Map/Valka_2_437x41.png"), 437, 41)
    valka_3 = Fanta(pygame.image.load("Assets/Map/Valka_3_416x86.png"), 416, 86)
    valka_4 = Fanta(pygame.image.load("Assets/Map/Valka_4_448x85.png"), 448, 85)
    valmiera = Fanta(pygame.image.load("Assets/Map/Valmiera_351x4.png"), 351, 4)
    valmiera_1 = Fanta(pygame.image.load("Assets/Map/Valmiera_1_349x11.png"), 349, 11)
    valmiera_2 = Fanta(pygame.image.load("Assets/Map/Valmiera_2_381x8.png"), 381, 8)
    valmiera_3 = Fanta(pygame.image.load("Assets/Map/Valmiera_3_360x64.png"), 360, 64)
    valmiera_4 = Fanta(pygame.image.load("Assets/Map/Valmiera_4_383x65.png"), 383, 65)
    ventspils = Fanta(pygame.image.load("Assets/Map/Ventspils_51x73.png"), 51, 73)
    ventspils_1 = Fanta(pygame.image.load("Assets/Map/Ventspils_1_52x120.png"), 52, 120)
    ventspils_2 = Fanta(pygame.image.load("Assets/Map/Ventspils_2_63x82.png"), 63, 82)
    ventspils_3 = Fanta(pygame.image.load("Assets/Map/Ventspils_3_100x73.png"), 100, 73)
    ventspils_4 = Fanta(pygame.image.load("Assets/Map/Ventspils_4_96x120.png"), 96, 120)
    
    marker = Fanta(pygame.image.load("Assets/mazapuce.png"), 0, 0)
    all_sprites.add(novadi)
    all_sprites.add(aizkraukle)
    all_sprites.add(aluksne)
    all_sprites.add(balvi)
    all_sprites.add(bauska)
    all_sprites.add(cesis)
    all_sprites.add(daugavpils)
    all_sprites.add(dobele)
    all_sprites.add(gulbene)
    all_sprites.add(jekabpils)
    all_sprites.add(jelgava)
    all_sprites.add(kraslava)
    all_sprites.add(kuldiga)
    all_sprites.add(liepaja)
    all_sprites.add(limbazi)
    all_sprites.add(ludza)
    all_sprites.add(madona)
    all_sprites.add(ogre)
    all_sprites.add(preili)
    all_sprites.add(rezekne)
    all_sprites.add(riga)
    all_sprites.add(saldus)
    all_sprites.add(talsi)
    all_sprites.add(tukums)
    all_sprites.add(valka)
    all_sprites.add(valmiera)
    all_sprites.add(ventspils)
     
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        time = pygame.time.get_ticks()
        marker.update(time, all_sprites.sprites())
        
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        screen.blit(marker.image, marker.rect)

        #score
        font = pygame.freetype.SysFont('Arial', 24)
        font.render_to(screen, (0, 0), "Score: " + str(round(time/1000)), (0, 0, 0))
        
        pygame.display.flip()
                
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in all_sprites.sprites() if s.rect.collidepoint(pos)]
                if aizkraukle in clicked_sprites:
                    all_sprites.add(aizkraukle_1)
                    all_sprites.add(aizkraukle_2)
                    all_sprites.add(aizkraukle_3)
                    all_sprites.add(aizkraukle_4)

                if aluksne in clicked_sprites:
                    all_sprites.add(aluksne_1)
                    all_sprites.add(aluksne_2)
                    all_sprites.add(aluksne_3)
                    all_sprites.add(aluksne_4)

                if balvi in clicked_sprites:
                    all_sprites.add(balvi_1)
                    all_sprites.add(balvi_2)
                    all_sprites.add(balvi_3)
                    all_sprites.add(balvi_4)

                if bauska in clicked_sprites:
                    all_sprites.add(bauska_1)
                    all_sprites.add(bauska_2)
                    all_sprites.add(bauska_3)
                    all_sprites.add(bauska_4)

                if cesis in clicked_sprites:
                    all_sprites.add(cesis_1)
                    all_sprites.add(cesis_2)
                    all_sprites.add(cesis_3)
                    all_sprites.add(cesis_4)

                if daugavpils in clicked_sprites:
                    all_sprites.add(daugavpils_1)
                    all_sprites.add(daugavpils_2)
                    all_sprites.add(daugavpils_3)
                    all_sprites.add(daugavpils_4)

                if dobele in clicked_sprites:
                    all_sprites.add(dobele_1)
                    all_sprites.add(dobele_2)
                    all_sprites.add(dobele_3)
                    all_sprites.add(dobele_4)

                if gulbene in clicked_sprites:
                    #all_sprites.add(gulbene_1)
                    all_sprites.add(gulbene_2)
                    all_sprites.add(gulbene_3)
                    all_sprites.add(gulbene_4)

                if jekabpils in clicked_sprites:
                    all_sprites.add(jekabpils_1)
                    all_sprites.add(jekabpils_2)
                    all_sprites.add(jekabpils_3)
                    all_sprites.add(jekabpils_4)

                if jelgava in clicked_sprites:
                    all_sprites.add(jelgava_1)
                    all_sprites.add(jelgava_2)
                    all_sprites.add(jelgava_3)
                    all_sprites.add(jelgava_4)

                if kraslava in clicked_sprites:
                    all_sprites.add(kraslava_1)
                    all_sprites.add(kraslava_2)
                    all_sprites.add(kraslava_3)
                    all_sprites.add(kraslava_4)

                if kuldiga in clicked_sprites:
                    all_sprites.add(kuldiga_1)
                    all_sprites.add(kuldiga_2)
                    all_sprites.add(kuldiga_3)
                    all_sprites.add(kuldiga_4)
                    
                if liepaja in clicked_sprites:
                    all_sprites.add(liepaja_1)
                    all_sprites.add(liepaja_2)
                    all_sprites.add(liepaja_3)
                    all_sprites.add(liepaja_4)
                    all_sprites.add(liepaja_5)
                    
                if limbazi in clicked_sprites:
                    all_sprites.add(limbazi_1)
                    all_sprites.add(limbazi_2)
                    all_sprites.add(limbazi_3)
                    all_sprites.add(limbazi_4)

                if ludza in clicked_sprites:
                    all_sprites.add(ludza_1)
                    all_sprites.add(ludza_2)
                    all_sprites.add(ludza_3)
                    all_sprites.add(ludza_4)

                if madona in clicked_sprites:
                    all_sprites.add(madona_1)
                    all_sprites.add(madona_2)
                    all_sprites.add(madona_3)
                    all_sprites.add(madona_4)
                    all_sprites.add(madona_5)

                if ogre in clicked_sprites:
                    all_sprites.add(ogre_1)
                    all_sprites.add(ogre_2)
                    all_sprites.add(ogre_3)
                    all_sprites.add(ogre_4)
                    
                if preili in clicked_sprites:
                    all_sprites.add(preili_1)
                    all_sprites.add(preili_2)
                    
                if rezekne in clicked_sprites:
                    #all_sprites.add(rezekne_1)
                    all_sprites.add(rezekne_2)
                    all_sprites.add(rezekne_3)
                    all_sprites.add(rezekne_4)

                if riga in clicked_sprites:
                    all_sprites.add(riga_1)
                    all_sprites.add(riga_2)
                    all_sprites.add(riga_3)
                    all_sprites.add(riga_4)
                    all_sprites.add(riga_5)

                if saldus in clicked_sprites:
                    all_sprites.add(saldus_1)
                    all_sprites.add(saldus_2)
                    all_sprites.add(saldus_3)
                    all_sprites.add(saldus_4)

                if talsi in clicked_sprites:
                    all_sprites.add(talsi_1)
                    all_sprites.add(talsi_2)
                    all_sprites.add(talsi_3)
                    all_sprites.add(talsi_4)

                if tukums in clicked_sprites:
                    #all_sprites.add(tukums_1)
                    all_sprites.add(tukums_2)
                    all_sprites.add(tukums_3)
                    all_sprites.add(tukums_4)

                if valka in clicked_sprites:
                    all_sprites.add(valka_1)
                    all_sprites.add(valka_2)
                    all_sprites.add(valka_3)
                    all_sprites.add(valka_4)
                    
                if valmiera in clicked_sprites:
                    all_sprites.add(valmiera_1)
                    all_sprites.add(valmiera_2)
                    all_sprites.add(valmiera_3)
                    all_sprites.add(valmiera_4)
                    
                if ventspils in clicked_sprites:
                    all_sprites.add(ventspils_1)
                    all_sprites.add(ventspils_2)
                    all_sprites.add(ventspils_3)
                    all_sprites.add(ventspils_4)
                    
                if marker.rect.collidepoint(pos):
                    marker.clicked = True
                    time = pygame.time.get_ticks()
                    marker.update(time, all_sprites.sprites())
                    
                    screen.blit(background, (0, 0))
                    all_sprites.draw(screen)
                    screen.blit(marker.image, marker.rect)
                    pygame.display.flip()
                    
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                pygame.mixer.music.stop()
                font.render_to(screen, (0, 25), "Tu netiki līdzi reformai!", (0, 0, 0))
                pygame.display.flip()
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
