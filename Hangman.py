import pygame
import os
import math
import random
# Running pygame
pygame.init()
# Initializaing variables for the game, such as the window or the lives and colors
words = ["IDE", "INGENIERO", "PROGRAMACION", "PYTHON", "AUDITEXT", "GO"]
word = random.choice(words)
GUESSED = []
hangman = 0
WIDTH =  800
HEIGHT = 500
surface = pygame.display.set_mode((WIDTH,HEIGHT))
color = (255,255,255)
PURPLE = (255,0,255)
BLACK = (0,0,0)
# Buttons

RADIUS =  20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i%13))
  y =  starty + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x,y, chr(A + i),True])
# Font
LETTERFONT = pygame.font.SysFont("Verdana", 30)
LETTERFONT2 = pygame.font.SysFont("Comic Sans", 30)
# Iterate trough the images
images = []
for i in range(7):
  i = pygame.image.load("hangman" + str(i) + ".png")
  images.append(i)
# Setting up the window game
pygame.display.set_caption("Hang Man Made by Pau")
FPS = 60
clock = pygame.time.Clock()

# Func draw

def draw():
  surface.fill(color)

  display_word = ""
  for letter in word:
    if letter in GUESSED:
      display_word += letter + " "
    else:
      display_word +=  "_ "
  text = LETTERFONT2.render(display_word,1,BLACK)
  surface.blit(text, (400,200))
  # Draw buttons
  for letter in letters:
    x, y, ltr, visible = letter
    if visible:
      pygame.draw.circle(surface,PURPLE, (x,y), RADIUS, 3)
      text =  LETTERFONT.render(ltr,1,BLACK)
      surface.blit(text, (x - text.get_width()/2, y - text.get_height()/2 ))
  surface.blit(images[hangman], (150,100))
  pygame.display.flip()
#Setting the game.
run = True
while run:
    clock.tick(FPS)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
          m_x, m_y = pygame.mouse.get_pos()
          for letter in letters:
            x, y, ltr, visible = letter
            if visible:
              distance = math.sqrt((x -  m_x)**2 + (y - m_y)**2)
              if distance <= RADIUS:
                letter[1] = False
                GUESSED.append(ltr)
                if ltr not in word:
                  hangman += 1
    won = True
    for letter in word:
      if letter not in GUESSED:
        won = False
        break
    if won:
      surface.fill(color)
      text = LETTERFONT.render("YOU WON!",1,PURPLE)
      surface.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(5000)
      break
    if hangman == 6:
      surface.fill(color)
      text = LETTERFONT.render("YOU LOSE!",1,PURPLE)
      surface.blit(text,(WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(5000)
      break
        
pygame.quit()