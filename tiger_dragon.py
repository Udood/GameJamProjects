import pygame
import pygame.freetype
from time import sleep
import random
from PodSixNet.Connection import ConnectionListener, connection

class Crosshair(pygame.sprite.Sprite):
    #moves a crosshair on the screen, following the mouse
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/crosshair.png')
        self.rect = self.image.get_rect()
        self.shooting = False
        
    def update(self):
        if self.shooting:
            self.image = pygame.image.load('Assets/boom.png')
        else:
            self.image = pygame.image.load('Assets/crosshair.png')      
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def shoot(self, tiles):
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                self.shooting = True
                tile.update(True) 
                return tile.get_tiger()

    def move(self, tiger, alert, tiles):
        self.shooting = False
        return tiger.move(self.rect, alert, tiles)

    def hit_civvies(self, tiles):
        for tile in tiles:
            if self.rect.colliderect(tile.rect):
                return tile.has_civvies

    def reload(self):
        self.shooting = False

class Tiger(pygame.sprite.Sprite):
    #defines stalking behaviour for the vietcong
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.rect = pygame.Rect
       self.spin = 1

    def reset(self, tiles, alert):
        for tile in tiles:
           if tile.get_tiger():
               tile.set_tiger(False)
               if alert == 2:
                   tile.set_birds(True)
                   tile.update(tile.burnt)
               else:
                   tile.set_birds(False)
                   tile.update(tile.burnt)
               #self.rect = tile.rect

    def reset_birds(self, tiles):
        for tile in tiles:
            if tile.__class__.__name__ == "Tree":
                tile.set_birds(False)
                tile.update(tile.burnt)

    def rile_civvies(self, tiles, screen, id, level):
        for tile in tiles:
            if tile.has_civvies:
               sleep(0.5)
               tile.set_birds(True)
               tile.update(tile.burnt)
               render_screen(screen, id, level, tiles)
               pygame.display.flip()

    def calm_civvies(self, tiles):
        for tile in tiles:
            if tile.has_civvies:
               tile.set_birds(False)
               tile.update(tile.burnt)

    def move(self, aimrect, alert, tiles):
        self.reset(tiles, alert)
        for tile in tiles:
            if aimrect.colliderect(tile.rect):
                tile.set_tiger(True)
                if tile.__class__.__name__ == "Dragon":
                    return True

    def get_adjacent(self, tiles):
        adjacent = []
        for tile in tiles:
            if tile.get_tiger():
                tiger_rect = tile.rect
                adjacent.append(tiger_rect.move(0, -100))
                adjacent.append(tiger_rect.move(100, -100))
                adjacent.append(tiger_rect.move(100, 0))
                adjacent.append(tiger_rect.move(100, 100))
                adjacent.append(tiger_rect.move(0, 100))
                adjacent.append(tiger_rect.move(-100, 100))
                adjacent.append(tiger_rect.move(-100, 0))
                adjacent.append(tiger_rect.move(-100, -100))
        return adjacent
               
class Dragon(pygame.sprite.Sprite):
    #player collision sprite
    def __init__(self, xpos, ypos):
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.image.load('Assets/dragon.png')
       self.rect = self.image.get_rect()
       self.rect.topleft = (xpos, ypos)
       self.has_tiger = False
       self.has_civvies = False
       self.burnt = False
       self.has_birds = False
       self.adjacent  = False

    def set_tiger(self, tiger_value):
        self.has_tiger = tiger_value

    def get_tiger(self):
        return self.has_tiger

    def update(self, burnt):
        if self.has_tiger == False:
            pygame.mixer.Sound.play(pygame.mixer.Sound('Assets/self.ogg'))

    def show_tiger(self):
        self.image = pygame.image.load('Assets/dragon.png')

    def set_birds(self, bird_value):
        self.has_birds = bird_value

    def get_birds(self):
        return self.has_birds

    def set_adjacent(self, value):
        self.adjacent = value

    def get_adjacent(self):
        return self.adjacent

class Stone(pygame.sprite.Sprite):
    #impassable
    def __init__(self, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/boulder.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos, ypos)
        self.has_tiger = False
        self.has_civvies = False
        self.burnt = False
        self.fname = ''
        
    def set_tiger(self, tiger_value):
        self.has_tiger = tiger_value

    def get_tiger(self):
        return self.has_tiger

    def update(self, burnt):
        self.image = pygame.image.load('Assets/boulder.png')

    def show_tiger(self):
        self.image = pygame.image.load('Assets/boulder.png')

    def set_birds(self, bird_value):
        self.has_birds = bird_value

    def get_birds(self):
        return self.has_birds

    def set_adjacent(self, value):
        self.adjacent = value

    def get_adjacent(self):
        return self.adjacent
    
class Tree(pygame.sprite.Sprite):
    #destroyable cover for the Tiger
    def __init__(self, xpos, ypos, burnt, civvies):
       pygame.sprite.Sprite.__init__(self)
       self.burnt = burnt
       self.has_civvies = civvies
       if self.burnt:
           self.fname = 'Assets/burnt'
           self.image = pygame.image.load('Assets/burnt.png')
       else:
           self.fname = 'Assets/tree_' + str(random.randint(1,4))
           self.image = pygame.image.load(self.fname + '.png')
       self.rect = self.image.get_rect()
       self.rect.topleft = (xpos, ypos)
       self.has_tiger = False
       self.has_birds = False
       self.adjacent  = False

    def update(self, burnt):
        self.burnt = burnt
        if self.burnt:
            if self.has_tiger:
                self.image = pygame.image.load('Assets/tiger.png')
            else:
                if self.adjacent:
                    self.image = pygame.image.load('Assets/burnt_a.png')
                else:
                    self.image = pygame.image.load('Assets/burnt.png')
        else:
            if self.has_birds:
                self.image = pygame.image.load(self.fname + '_alert.png')
            else:
                if self.adjacent:
                    self.image = pygame.image.load(self.fname + '_a.png')
                else:
                    self.image = pygame.image.load(self.fname + '.png')
           
    def set_tiger(self, tiger_value):
        self.has_tiger = tiger_value
        if self.has_tiger and self.burnt:
            self.image = pygame.image.load('Assets/tiger.png')
        elif not self.has_tiger and self.burnt:
            self.image = pygame.image.load('Assets/burnt.png')

    def get_tiger(self):
        return self.has_tiger

    def show_tiger(self):
        if self.has_tiger and not self.burnt:
            self.image = pygame.image.load('Assets/tiger_blink.png')

    def set_birds(self, bird_value):
        self.has_birds = bird_value

    def get_birds(self):
        return self.has_birds

    def set_adjacent(self, value):
        self.adjacent = value

    def get_adjacent(self):
        return self.adjacent
            

class Picture(pygame.sprite.Sprite):
    #general menu graphics
    def __init__(self, path, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (xpos, ypos)
        
def render_screen(screen, id, next_level, tiles):
        ffont = pygame.freetype.SysFont('arialblack', 24)
        font = pygame.freetype.SysFont('arial', 16)
        
        if id == 'intro':
            ffont.render_to(screen, (275, 180), "H", (255, 0, 0))
            font.render_to(screen, (292, 180), "unt is on", (255, 100, 0))
            ffont.render_to(screen, (275, 220), "L", (255, 0, 0))
            font.render_to(screen, (292, 220), "earn the Rules", (255, 100, 0))
            ffont.render_to(screen, (275, 260), "Q", (255, 0, 0))
            font.render_to(screen, (292, 260), "uit", (255, 100, 0))
            tiles.empty()
        elif id == 'win':
            ffont.render_to(screen, (250, 66), "YOU WIN!", (0, 0, 0))
            ffont.render_to(screen, (275, 200), "H", (255, 0, 0))
            font.render_to(screen, (292, 200), "unt again", (255, 100, 0))
            ffont.render_to(screen, (275, 240), "Q", (255, 0, 0))
            font.render_to(screen, (292, 240), "uit", (255, 100, 0))
            tiles.empty()
            win_pic = pygame.sprite.Group(Picture('Assets/win.png', 275, 90))
            win_pic.draw(screen)
        elif id == 'lose': 
            ffont.render_to(screen, (250, 66), "YOU LOSE!", (0, 0, 0))
            ffont.render_to(screen, (275, 200), "H", (255, 0, 0))
            font.render_to(screen, (292, 200), "unt again", (255, 100, 0))
            ffont.render_to(screen, (275, 240), "Q", (255, 0, 0))
            font.render_to(screen, (292, 240), "uit", (255, 100, 0))
            tiles.empty()
            lose_pic = pygame.sprite.Group(Picture('Assets/lose.png', 275, 90))
            lose_pic.draw(screen)
        elif id == 'learn':
            font.render_to(screen, (90, 180), "Dragon must shoot the Tiger before he can reach your position!", (0, 0, 0))
            font.render_to(screen, (90, 196), "Tiger must stalk the Dragon unseen! Moves as King piece.", (0, 0, 0))
            font.render_to(screen, (90, 212), "50% chance for move to show Alert on tile Tiger just left", (0, 0, 0))
            font.render_to(screen, (90, 228), "Burned tiles expose Tiger completely.", (0, 0, 0))
            ffont.render_to(screen, (275, 280), "H", (255, 0, 0))
            font.render_to(screen, (292, 280), "unt is on", (255, 100, 0))
            tiles.empty()
        elif id == 'level':
            if not tiles:
                load_level(next_level, tiles)
            tiles.draw(screen)
            
def load_level(level, tiles):
    xpos = 75
    ypos = 50
    layout = open('Levels/' + str(level) + '.txt')
        
    for line in layout:
        for char in line:
            if char == 'T':
                tiles.add(Tree(xpos, ypos, False, False))
            elif char == 'B':
                tiles.add(Tree(xpos, ypos, True, False))
            elif char == 'V':
                tiles.add(Tree(xpos, ypos, False, False))
                tree = tiles.get_top_sprite()
                tree.set_tiger(True)
            elif char == 'D':
                tiles.add(Dragon(xpos, ypos))
            elif char == 'C':
                tiles.add(Tree(xpos, ypos, False, True))
            xpos = xpos + 100
        ypos = ypos + 100
        xpos = 75
    layout.close()

class TigerDragonGame(ConnectionListener):
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((640, 900))
        pygame.display.set_caption('Stalking Tiger - Roaring Dragon')
        pygame.mouse.set_visible(0)
        logo = pygame.image.load('Assets/logo.png')
        pygame.display.set_icon(logo)
        
        self.headfont = pygame.freetype.SysFont('arialblack', 24)
        self.screen_id = 'intro'
        self.next_level = 1

        # create a white surface on screen
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

        self.aim = Crosshair()
        self.vietcong = Tiger()
        frame = pygame.sprite.Sprite()
        frame.image = pygame.image.load('Assets/frame.png')
        frame.rect = frame.image.get_rect()
        self.statics = pygame.sprite.Group(frame)
        self.dynamics = pygame.sprite.Group(self.aim)
        self.tiles = pygame.sprite.LayeredUpdates()

        self.menu_h = pygame.Rect(0, 0, 130, 20)
        self.menu_l = pygame.Rect(0, 0, 130, 20)
        self.menu_q = pygame.Rect(0, 0, 130, 20)
        self.pinpoint = pygame.Rect(0, 0, 5, 5)

        pygame.mixer.music.load('Assets/background.mp3')
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(-1)
        self.channel = pygame.mixer.Channel(1)
        self.channel.play(pygame.mixer.Sound('Assets/intro.ogg'))
        self.Connect(("80.232.247.149", 12345))
        self.connected = False
        self.cooldown = 10
        self.blinker = 100
        self.blinker_on = True
        self.turn = False
        self.tiger = False
        self.dragon = False
        
    def update(self):
        self.cooldown -= 1
        connection.Pump()
        self.Pump()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                connection.Send("QUIT pressed")
                return False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_h and self.screen_id != 'level' and self.screen_id != 'GG':
                self.channel.stop()
                if self.screen_id == 'lose':
                    self.channel.play(pygame.mixer.Sound('Assets/replay.ogg'))
                else:
                    while not self.connected:
                        self.Pump()
                        connection.Pump()
                        sleep(0.01)
                    if self.num == 0:
                        self.turn = True
                        self.tiger = True
                        self.dragon = False
                    else:
                        self.turn = False
                        self.tiger = False
                        self.dragon = True
                        
                    self.channel.play(pygame.mixer.Sound('Assets/start.ogg'))
                self.screen_id = 'level'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
                connection.Send("HELP pressed")
                self.screen_id = 'learn'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                connection.Send("QUIT pressed")
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN and self.screen_id != 'level':
                self.pinpoint.center = (self.aim.rect.centerx, self.aim.rect.centery)
                if self.screen_id == 'intro':   
                    self.menu_h.topleft = (275, 180)
                    self.menu_l.topleft = (275, 220)
                    self.menu_q.topleft = (275, 260)
                    if self.pinpoint.colliderect(self.menu_h):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_h))
                    elif self.pinpoint.colliderect(self.menu_l):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_l))
                    elif self.pinpoint.colliderect(self.menu_q):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q))
                elif self.screen_id == 'learn':
                    self.menu_h.topleft = (275, 280)
                    if self.pinpoint.colliderect(self.menu_h):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_h))
                elif self.screen_id == 'win' or self.screen_id == 'lose':
                    self.menu_h.topleft = (275, 200)
                    self.menu_q.topleft = (275, 240)
                    if self.pinpoint.colliderect(self.menu_h):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_h))
                    elif self.pinpoint.colliderect(self.menu_q):
                       pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q))
            elif event.type == pygame.MOUSEBUTTONDOWN and self.screen_id == 'level' and self.turn == True and self.cooldown <= 0:
                if self.dragon:
                    self.channel.play(pygame.mixer.Sound('Assets/bazooka.ogg'))
                    self.Send({"action": "shoot", "aim_x":self.aim.rect.centerx, "aim_y":self.aim.rect.centery, "gameid": self.gameid, "num": self.num})
                    self.cooldown = 10
                    if self.aim.shoot(self.tiles):
                        self.screen_id = 'win'
                        self.Send({"action": "win", "gameid": self.gameid, "num": self.num})
                        self.channel.queue(pygame.mixer.Sound('Assets/win' + str(random.randint(1,2)) + '.ogg'))
                        self.aim.reload()
                    else:
                        if self.aim.hit_civvies(self.tiles):
                            self.channel.queue(pygame.mixer.Sound('Assets/civilian.ogg'))
                        else:
                            self.channel.queue(pygame.mixer.Sound('Assets/jungle' + str(random.randint(1,3)) + '.ogg'))
                if self.tiger:
                    for target_tile in self.vietcong.get_adjacent(self.tiles):
                        if self.aim.rect.colliderect(target_tile):
                            self.alert = random.randint(1,2)
                            self.Send({"action": "move", "aim_x":self.aim.rect.centerx, "aim_y":self.aim.rect.centery, "gameid": self.gameid, "num": self.num, "alert": self.alert})
                            self.cooldown = 10
                            for tile in self.tiles:
                                tile.set_adjacent(False)
                            if self.aim.move(self.vietcong, self.alert, self.tiles):
                                self.screen_id = 'win'
                                self.Send({"action": "win", "gameid": self.gameid, "num": self.num})
                                self.channel.queue(pygame.mixer.Sound('Assets/win' + str(random.randint(1,2)) + '.ogg'))
                                self.aim.reload()
            elif event.type == pygame.MOUSEBUTTONUP and self.screen_id == 'level':
                if self.aim.shooting == True:
                    self.aim.reload()

        self.blinker -= 1
        if self.blinker <= 0 and self.screen_id == 'level':
            self.vietcong.reset_birds(self.tiles)
            if self.blinker_on:
                self.blinker_on = False
            else:
                self.blinker_on = True
            self.blinker = 100
        if self.tiger and self.screen_id == 'level':
            if self.blinker_on:
                for tile in self.tiles:
                    if tile.__class__.__name__ == "Tree":
                        tile.show_tiger()
            else:
                for tile in self.tiles:
                    if tile.__class__.__name__ == "Tree":
                        tile.update(tile.burnt)

        if self.tiger and self.screen_id == 'level':
            for target_tile in self.vietcong.get_adjacent(self.tiles):
                for tile in self.tiles:
                    if tile.rect.colliderect(target_tile):
                        tile.set_adjacent(True)
        self.refresh_screen()
        return True

    def refresh_screen(self):              
        self.statics.draw(self.screen)
        render_screen(self.screen, self.screen_id, self.next_level, self.tiles)
        self.dynamics.update()
        self.dynamics.draw(self.screen)
        self.headfont.render_to(self.screen, (65, 10), "STALKING TIGER - ROARING DRAGON", (0, 0, 0))
        if self.turn:
            self.headfont.render_to(self.screen, (250, 875), "YOUR TURN!", (0, 0, 0))
        pygame.display.flip()

    def Network_startgame(self, data):
        self.connected = True
        self.num = data["player"]
        self.gameid = data["gameid"]      

    def Network_shoot(self, data):
        self.aim.rect.center = (data["aim_x"], data["aim_y"])
        self.aim.shoot(self.tiles)
        self.aim.reload()
        self.refresh_screen()

    def Network_move(self, data):
        self.aim.rect.center = (data["aim_x"], data["aim_y"])
        self.alert = data["alert"]
        self.aim.move(self.vietcong, self.alert, self.tiles)
        self.aim.reload()
        self.refresh_screen()

    def Network_yourturn(self, data):
        self.turn = data["turn"]

    def Network_lose(self, data):
        self.channel.stop()
        self.channel.play(pygame.mixer.Sound('Assets/die.ogg'))
        self.screen_id = 'lose'
    
def main():
    game = TigerDragonGame()
    
    # define a variable to control the main loop
    running = True
    while running:   
        running = game.update()
        

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
