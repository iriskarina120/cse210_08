import pygame
import random

pygame.init()
pygame.mouse.set_visible(0)

class Artifact(pygame.sprite.Sprite):
    """ This class represents the Artifacts like gems and rocks """
    def __init__(self):
        super().__init__() 
        self.image = ""
        self.color = " " 
        self.rect = ""

    def reset_pos(self):        
        self.rect.y = random.randrange(-300, 50)
        self.rect.x = random.randrange(0, 900)

    def update(self):       
        self.rect.y += 4
        if self.rect.y > 900:
            self.reset_pos()

class Gema(Artifact, pygame.sprite.Sprite):
    """ This class represents the gems"""
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("gem.png").convert()
        self.image.set_colorkey(BLACK) 
        self.rect = self.image.get_rect()
    
    def earn_points(self, score):        
        return score + 1         

class Roca(Artifact, pygame.sprite.Sprite):
    """ This class represents the rocs"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

    def lose_points(self, score):        
        return score - 1     

class Player(pygame.sprite.Sprite):
    """ This class represents the main character Player """       
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("saucer.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = 900 / 2      
        self.speed = [0.5, -0.5] 

    def update(self):
        """ Actualize player's location """       
        pos = pygame.mouse.get_pos()      
        self.rect.x = pos[0]     

class SpecialEffects:
    def __init__(self):
         self.backg = ""
         self.music = ""
         self.sound_rock = ""
         self.sound_gem = ""   
    
    def load_backgrounds(self):
        self.backg = pygame.image.load("space_background.jpg")
        pygame.image.load("space_background.jpg").convert() 
        screen.blit(self.backg, [0, 0])
    
    def backg_music(self):
        self.music = pygame.mixer.music.load("plumbum-rain.wav")
        pygame.mixer.music.play()
    
    def sound_col_rock(self):
        self.sound_rock = pygame.mixer.Sound("kretopi__synthweapon-003.wav")
        self.sound_rock.play()
    
    def sound_col_gem(self):
        self.sound_gem = pygame.mixer.Sound("got_point.mp3")
        self.sound_gem.play()
    
class Message:
    def __init__(self):
        self.message = ""

    def colide_gem(self):
        self.message = "Hurrah! You got 1 point!"
        return self.message

    def colide_rock(self):
        self.message = "Ups! You lost 1 point!"
        return self.message

BLUE = [12, 44, 146]
GREEN = [46, 189, 20]
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
RED = [255, 0, 0]

#My screen
dimensions = [900, 700] 
screen = pygame.display.set_mode(dimensions)

effects = SpecialEffects()
music = effects.backg_music() 

# This is a list of all the sprites.
lista_de_todos_los_sprites = pygame.sprite.Group() 
# This list represents each artifact in the game.
lista_artifacts = pygame.sprite.Group()
lista_gemas = pygame.sprite.Group()
lista_rocks = pygame.sprite.Group()

for i in range(60):
    gema =Gema() 
    # setting the gems' location 
    gema.rect.x = random.randrange(0, 900)
    gema.rect.y = random.randrange(-3500, 100)     
    lista_gemas.add(gema)
    lista_de_todos_los_sprites.add(gema)
    lista_artifacts.add(gema)

for i in range(60):
    rock = Roca() 
    # setting the rocks' location 
    rock.rect.x = random.randrange(0, 900)
    rock.rect.y = random.randrange(-3500, 100)     
    lista_rocks.add(rock)
    lista_de_todos_los_sprites.add(rock)
    lista_artifacts.add(rock)  

player = Player()
lista_de_todos_los_sprites.add(player)
reloj = pygame.time.Clock()
player.rect.y = 600
done = False

# -------- Instruction Page Loop -----------
while not done :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            done = True

    # Limit to 60 frames per second
    reloj.tick(60)
    screen.fill(WHITE)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Main program loop
hecho = False
score = 0
while not hecho:                           

    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT: 
            hecho = True       

    """--- Game logical---""" 

    lista_de_todos_los_sprites.update()

    artifact = Artifact()          

    gem_hit = pygame.sprite.spritecollide(player, lista_gemas, True)
    rock_hit = pygame.sprite.spritecollide(player, lista_rocks, True)         

    for artifact in gem_hit:                                
            
            effects.sound_col_gem()            
            gema =Gema() 
            # setting the gems' location 
            gema.rect.x = random.randrange(0, 900)
            gema.rect.y = random.randrange(-3500, 50)     
            lista_gemas.add(gema)
            lista_de_todos_los_sprites.add(gema)
            lista_artifacts.add(gema)                   
            score -= 1   
           
    for artifact in rock_hit:           
            effects.sound_col_rock()  
            rock = Roca() 
            # setting the rocks' location 
            rock.rect.x = random.randrange(0, 900)
            rock.rect.y = random.randrange(-3500, 50)     
            lista_rocks.add(rock)
            lista_de_todos_los_sprites.add(rock)
            lista_artifacts.add(rock)
            score += 1 

    font = pygame.font.Font(None, 40)
    points = font.render('SCORE = '+str(score), 
    True, (200,200,200), (0,0,0) )                  
    rectanglePoints = points.get_rect()           
    rectanglePoints.left = 10                           
    rectanglePoints.top = 10        
    pygame.display.flip()
    
    screen.fill(WHITE)    
    
    backg = effects.load_backgrounds()   
    lista_de_todos_los_sprites.draw(screen)
    print_score = screen.blit(points, rectanglePoints)
   
    pygame.display.flip()
    
    reloj.tick(110)

pygame.quit()