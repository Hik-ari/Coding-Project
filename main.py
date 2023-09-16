import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
pygame.quit()
