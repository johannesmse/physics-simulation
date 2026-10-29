import pygame
import config as cfg
from ui import UI
from world import World

pygame.init()
pygame.display.set_caption("Physics simulation")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((cfg.WINDOW_WIDTH, cfg.WINDOW_HEIGHT))
world = World()
game_ui = UI(screen, world)
running = True

world_update_timer = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if world_update_timer == 2:
        world.update_world()
        world_update_timer = 0
    else:
        world_update_timer += 1

    game_ui.draw()
    pygame.display.flip()
    clock.tick(400)

pygame.quit()