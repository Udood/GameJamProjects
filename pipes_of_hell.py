import pygame
import pygame.freetype
import time
import random

# turnable Pipe, 4 randomized variations. Position is kept to check neighbour Pipes in the grid for route finding
class Pipe(pygame.sprite.Sprite):
    def __init__(self, xpos, ypos):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.fname = 'Assets/pipe_' + str(random.randint(1,4))
        self.image = pygame.image.load(self.fname + '.png')
        self.rect = self.image.get_rect()
        if self.fname == 'Assets/pipe_1':
            self.up = 1
            self.down = 1
            self.left = 0
            self.right = 0
        elif self.fname == 'Assets/pipe_2':
            self.up = 1
            self.down = 0
            self.left = 0
            self.right = 1
        elif self.fname == 'Assets/pipe_3':
            self.up = 1
            self.down = 1
            self.left = 0
            self.right = 1
        elif self.fname == 'Assets/pipe_4':
            self.up = 1
            self.down = 1
            self.left = 1
            self.right = 1
        self.temp = 0
        self.xpos = xpos
        self.ypos = ypos

    def update(self):
        self.image = pygame.transform.rotate(self.image, 90)
        self.temp = self.up
        self.up = self.right
        self.right = self.down
        self.down = self.left
        self.left = self.temp

    def get_xpos(self):
        return self.xpos

    def get_ypos(self):
        return self.ypos

# moves around randomly. Pipe messing logic is outside the class, in main method
class Angel(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/angel.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (300,300)
        self.xstep = 0
        self.ystep = 0
        self.last_update = 0
        self.update_delay = 1000

    def update(self):
        # change movement patter every so often
        if pygame.time.get_ticks() > self.last_update + self.update_delay:
            self.last_update = pygame.time.get_ticks()
            self.xstep = random.randint(-1,1)
            self.ystep = random.randint(-1,1)
        # but do not stray out of bounds
        if self.rect.x == 0:
            self.xstep = 1
        elif self.rect.x == 1000:
            self.xstep = -1
        if self.rect.y == 0:
            self.ystep = 1
        elif self.rect.y == 700:
            self.ystep = -1
        self.rect.x = self.rect.x + self.xstep
        self.rect.y = self.rect.y + self.ystep
            
class Cursor(pygame.sprite.Sprite):
#moves a Sprite on the screen, following the mouse
    def __init__(self):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/cursor.png')
        #rect is a rectangular border associated with the object aka 'hitbox'
        self.rect = pygame.Rect(0, 0, 5, 5)
        
    def update(self):      
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos

# just stands there and animates occasionally
class Satan(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/demon_180_1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (655, 820)
        self.state = 'closed'

    def update(self):
        if random.randint(0,100) > 95:
            if self.state == 'closed':
                self.image = pygame.image.load('Assets/demon_180_2.png')
                self.state = 'open'
            else:
                self.image = pygame.image.load('Assets/demon_180_1.png')
                self.state = 'closed'

# rises to top, spills over and triggers scoring
class Pot(pygame.sprite.Sprite):
    def __init__(self):
        # call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/pot_1.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (15, 800)
        self.update_delay = 5000
        self.last_update = 0

    def update(self):
        if pygame.time.get_ticks() > self.last_update + self.update_delay:
            self.last_update = pygame.time.get_ticks()
            self.rect.y = self.rect.y - 225
            if self.rect.y < -100:
                self.image = pygame.image.load('Assets/pot_1.png')
                self.rect.y = 820
            elif self.rect.y < 100:
                self.image = pygame.image.load('Assets/pot_2.png')
                update_score()
        
# defining variables outside functions makes the global
screen = pygame.display.set_mode((1000, 1000))
grid = [[Pipe(i, j) for j in range(8)] for i in range(8)]   #a 2D array of Pipe sprites so specific pipe can be accessed by position
pots_remaining = 3
baths_target = 2

# draw screen-specific objects like menu texts or the pipe-grid
def render_screen(id, gridbox, diff):
    global pots_remaining
    global baths_target
    ffont = pygame.freetype.SysFont('arialblack', 24)
    font = pygame.freetype.SysFont('arial', 16)
    logo = pygame.image.load('Assets/logo.png').convert()    
    
    if id == 'intro' or id == 'win' or id == 'lose':
        font.render_to(screen, (420, 240), "Acolyte", (255, 100, 0))
        font.render_to(screen, (420, 280), "Devotee", (255, 100, 0))
        font.render_to(screen, (420, 320), "Fanatic", (255, 100, 0))
        if diff == 1:
            screen.blit(logo, (380, 230))
        elif diff == 2:
            screen.blit(logo, (380, 270))
        elif diff == 3:
            screen.blit(logo, (380, 310))
        
        ffont.render_to(screen, (400, 400), "G", (255, 0, 0))
        font.render_to(screen, (420, 400), "lory to THE SATAN", (255, 100, 0))
        ffont.render_to(screen, (400, 440), "H", (255, 0, 0))
        font.render_to(screen, (420, 440), "ow to serve", (255, 100, 0))
        ffont.render_to(screen, (400, 480), "Q", (255, 0, 0))
        font.render_to(screen, (420, 480), "uit", (255, 100, 0))
        if id == 'win' or id == 'lose':
            adjust_globals(1)   # reset globals upon game end
        if id == 'win':
            ffont.render_to(screen, (420, 50), "YOU WON!", (255, 0, 0))
        if id == 'lose':
            ffont.render_to(screen, (420, 50), "YOU LOST!", (255, 0, 0))
    elif id == 'learn':
        font.render_to(screen, (220, 280), "SATAN wishes to bathe in the blood of sinners! Connect pipes and sate his dark desire.", (0, 0, 0))
        font.render_to(screen, (220, 320), "Make sure path for the flow is available once pot reaches the intake.", (0, 0, 0))
        font.render_to(screen, (220, 360), "Angels will mess with your work, but can be temporarily banished by clicking on them.", (0, 0, 0))
        ffont.render_to(screen, (400, 400), "G", (255, 0, 0))
        font.render_to(screen, (420, 400), "lory to THE SATAN", (255, 100, 0))
    elif id == 'level':
        gridbox.draw(screen)
    
def get_flow(pipe, direction):
    xpos = pipe.get_xpos()
    ypos = pipe.get_ypos()
    if direction == 'up':
        if ypos == 0:
            return False
        if pipe.up == 1 and grid[xpos][ypos-1].down == 1:
            return True
        else:
            return False
    elif direction == 'down':
        if ypos == len(grid[0])-1: # position starts count from 0, but length from 1
            return False
        if pipe.down == 1 and grid[xpos][ypos+1].up == 1:
            return True
        else:
            return False
    elif direction == 'left':
        if xpos == 0:
            return False
        if pipe.left == 1 and grid[xpos-1][ypos].right == 1:
            return True
        else:
            return False
    elif direction == 'right':
        if xpos == len(grid)-1:
            return False
        if pipe.right == 1 and grid[xpos+1][ypos].left == 1:
            return True
        else:
            return False

def route(start_x, start_y, end_x, end_y):
    # start by adding one Pipe to loop set
    unexplored = [grid[start_x][start_y]]
    for pipe in unexplored:
        xpos = pipe.get_xpos()
        ypos = pipe.get_ypos()
        if xpos == end_x and ypos == end_y:
            return True
        # add more Pipes to set as we go, where flow exists and Pipe not yet in loop set
        # either we find the end Pipe or finish the loop and auto-false
        if get_flow(grid[xpos][ypos], 'up'):
            if grid[xpos][ypos-1] not in unexplored:
                unexplored.append(grid[xpos][ypos-1])
        if get_flow(grid[xpos][ypos], 'down'):
            if grid[xpos][ypos+1] not in unexplored:
                unexplored.append(grid[xpos][ypos+1])
        if get_flow(grid[xpos][ypos], 'left'):
            if grid[xpos-1][ypos] not in unexplored:
                unexplored.append(grid[xpos-1][ypos])
        if get_flow(grid[xpos][ypos], 'right'):
            if grid[xpos+1][ypos] not in unexplored:
                unexplored.append(grid[xpos+1][ypos])
    return False

def update_score():
    global pots_remaining #need to add global to be able to change, otherwise treated as local variable
    global baths_target
    pots_remaining -= 1
    if route(0, 0, 7, 7):
        baths_target -= 1
        
def draw_score():
    ffont = pygame.freetype.SysFont('arialblack', 24)
    font = pygame.freetype.SysFont('arial', 32)

    ffont.render_to(screen, (400, 100), "POTS REMAIN:", (255, 0, 0))
    font.render_to(screen, (600, 100), str(pots_remaining), (255, 100, 0))
    ffont.render_to(screen, (400, 150), "BLOODBATHS DESIRED:", (255, 0, 0))
    font.render_to(screen, (720, 150), str(baths_target), (255, 100, 0))

def adjust_globals(diff):
    global pots_remaining
    global baths_target
    if diff == 1:
        pots_remaining = 3
        baths_target = 2
    if diff == 2:
        pots_remaining = 4
        baths_target = 3
    if diff == 3:
        pots_remaining = 5
        baths_target = 4
    
def main():
    pygame.init()
    pygame.display.set_caption('Pipes of Hell')
    pygame.mouse.set_visible(0)
    logo = pygame.image.load('Assets/logo.png')
    pygame.display.set_icon(logo)
    
    headfont = pygame.freetype.SysFont('arialblack', 24)
    screen_id = 'intro'

    # create a white surface on screen
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))     #blit draws to the screen
    pygame.display.flip()               #flip refreshes the screen

    #initiate our objects
    offset_x = 200
    offset_y = 200

    #initialize grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j].rect.topleft = (70*i+offset_x, 70*j+offset_y)

    pygame.mixer.music.load('Assets/Sound/game_music.mp3')
    channel = pygame.mixer.Channel(1)
                
    cursor = Cursor()
    michael = Angel()
    gabriel = Angel()
    raphael = Angel()
    demon = Satan()
    pot = Pot()
    frame = pygame.sprite.Sprite()
    frame.image = pygame.image.load('Assets/frame.png')
    frame.rect = frame.image.get_rect()
    shower = pygame.image.load('Assets/shower_250.png')
    statics = pygame.sprite.Group(frame)    #these groups will have more objects eventually
    dynamics = pygame.sprite.Group(cursor, michael, demon, pot)
    gridbox = pygame.sprite.Group(grid)

    #hitboxes for menu and cursor
    #here and in keyboard events GHE stands for Glory How and Quit
    menu_g = pygame.Rect(400, 400, 130, 20)
    menu_h = pygame.Rect(400, 440, 130, 20)
    menu_q = pygame.Rect(400, 480, 130, 20)
    menu_d1 = pygame.Rect(420, 240, 130, 20)
    menu_d2 = pygame.Rect(420, 280, 130, 20)
    menu_d3 = pygame.Rect(420, 320, 130, 20)

    diff = 1

    # define a variable to control the main loop
    running = True
    while running:   
        # handle events in the queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.mixer.music.stop()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_g:
                screen_id = 'level'
                channel.play(pygame.mixer.Sound('Assets/Sound/click_play.ogg'))
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
                screen_id = 'learn'
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
                pygame.mixer.music.stop()
            elif event.type == pygame.MOUSEBUTTONDOWN and screen_id != 'level':
                if screen_id == 'intro' or screen_id == 'win' or screen_id == 'lose':
                    #check for collision of cursor and menu hitboxes
                    if cursor.rect.colliderect(menu_g): 
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_g))
                    elif cursor.rect.colliderect(menu_h):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_h))
                    elif cursor.rect.colliderect(menu_q):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_q))
                    #check for collision of cursor and difficulty hitboxes
                    elif cursor.rect.colliderect(menu_d1):
                        diff = 1
                        if dynamics.has(gabriel):
                            dynamics.remove(gabriel)
                        if dynamics.has(raphael):
                            dynamics.remove(raphael)
                        adjust_globals(diff)
                    elif cursor.rect.colliderect(menu_d2):
                        diff = 2
                        if dynamics.has(raphael):
                            dynamics.remove(raphael)
                        if not dynamics.has(gabriel):
                            dynamics.add(gabriel)
                        adjust_globals(diff)
                    elif cursor.rect.colliderect(menu_d3):
                        diff = 3
                        if not dynamics.has(raphael):
                            dynamics.add(raphael)
                        if not dynamics.has(gabriel):
                            dynamics.add(gabriel)
                        adjust_globals(diff)
                elif screen_id == 'learn':
                    if cursor.rect.colliderect(menu_g):
                        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_g))
            elif event.type == pygame.MOUSEBUTTONDOWN and screen_id == 'level':
                # turn pipes on click
                for pipe in gridbox:
                    if cursor.rect.colliderect(pipe.rect):
                            pipe.update()
                # teleport angel away on click
                if cursor.rect.colliderect(michael.rect):
                    michael.rect.topleft = (2000, 2000)
                    channel.play(pygame.mixer.Sound('Assets/Sound/angel.ogg'))
                if cursor.rect.colliderect(gabriel.rect):
                    gabriel.rect.topleft = (2000, 2000)
                    channel.play(pygame.mixer.Sound('Assets/Sound/angel.ogg'))
                if cursor.rect.colliderect(raphael.rect):
                    raphael.rect.topleft = (2000, 2000)
                    channel.play(pygame.mixer.Sound('Assets/Sound/angel.ogg'))

        # turn pipes angel is sitting on                
        for pipe in gridbox: 
            if michael.rect.colliderect(pipe.rect) or (gabriel.rect.colliderect(pipe.rect) and diff > 1) or (raphael.rect.colliderect(pipe.rect) and diff > 2):
                # modulate turning frequency
                if random.randint(0,100) > 95:
                     pipe.update()
        # modulate teleport frequency
        if random.randint(0,1000) > 997:
            michael.rect.topleft = (random.randint(200,800), random.randint(200,700))
        if random.randint(0,1000) > 997:
            gabriel.rect.topleft = (random.randint(200,800), random.randint(200,700))
        if random.randint(0,1000) > 997:
            raphael.rect.topleft = (random.randint(200,800), random.randint(200,700))

        statics.draw(screen)                        #draw static stuff first
        render_screen(screen_id, gridbox, diff)
        if screen_id == 'level':
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(1)
            draw_score()
            if pots_remaining < baths_target:
                screen_id = 'lose'
                channel.play(pygame.mixer.Sound('Assets/Sound/lose_' + str(random.randint(1, 2)) + '.ogg'))
            if baths_target == 0:
                screen_id = 'win'
                channel.play(pygame.mixer.Sound('Assets/Sound/win.ogg'))
        else:
            pygame.mixer.music.stop()
            pygame.mixer.music.rewind()
        dynamics.update()                               #update state of changeable Sprites and draw those
        dynamics.draw(screen)
        if pot.rect.y < 100 and route(0, 0, 7, 7):      #pot in upmost position and flow exists
            screen.blit(shower, (625, 790))
            channel.play(pygame.mixer.Sound('Assets/Sound/shower.ogg'))
        headfont.render_to(screen, (400, 10), "PIPES OF HELL", (0, 0, 0))
        pygame.display.flip()               #refresh display

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
