import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")
clock = pygame.time.Clock()

run = True
while run:

  clock.tick(FPS)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
pygame.quit()
