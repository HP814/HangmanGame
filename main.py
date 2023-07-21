# import pygame, sys
# from pygame.locals import QUIT

# pygame.init()
# DISPLAYSURF = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Hello World!')
# while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:
#            pygame.quit()
#            sys.exit()
#    pygame.display.update()

import pygame
from pygame.locals import *
import math
import random

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HP's Hangman Game")

RADIUS = 20
GAP = 15
letters = []
A = 65
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont('Permanent Marker', 40)

WORD_FONT = pygame.font.SysFont('Permanent Marker', 60)

TITLE_FONT = pygame.font.SysFont('Permanent Marker', 70)

images = []
for i in range(7):
  images.append(pygame.image.load("images/hangman" + str(i) + ".png"))

hangman_status = 0
words = ["DEVELOPER", "DATA", "PYGAME", "PYTHON", "INNOVATOR", "ENGINEER"]
word = random.choice(words)
guessed = []

FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
  win.fill((135, 206, 235))

  text = TITLE_FONT.render("HP's HANGMAN", 1, (0, 0, 0))
  win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "

  text = WORD_FONT.render(display_word, 1, (0, 0, 0))
  win.blit(text, (400, 200))

  for letter in letters:
    x, y, l, visiblity = letter
    if visiblity:
      pygame.draw.circle(win, (0, 0, 0), (x, y), RADIUS, 3)
      text = LETTER_FONT.render(l, 1, (0, 0, 0))
      win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

  win.blit(images[hangman_status], (150, 100))
  pygame.display.update()


def display_message(message):
  pygame.time.delay(1000)
  win.fill((255, 255, 255))
  text = WORD_FONT.render(message, 1, (0, 0, 0))
  win.blit(
    text,
    (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
  pygame.display.update()
  pygame.time.delay(3000)


while run:
  clock.tick(FPS)

  draw()

  for event in pygame.event.get():
    if event.type == QUIT:
      run = False
    if event.type == MOUSEBUTTONDOWN:
      m_x, m_y = pygame.mouse.get_pos()
      for letter in letters:
        x, y, l, visiblity = letter
        if visiblity:
          dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
          if dis < RADIUS:
            letter[3] = False
            guessed.append(l)
            if l not in word:
              hangman_status += 1

  won = True
  for letter in word:
    if letter not in guessed:
      won = False
      break

  if won:
    display_message("You Won !!")
    break
  if hangman_status == 6:
    display_message("You Lost :(")
    break

pygame.quit()
