####################################################################
### Hyunsung KO, student of Sorbonne University in Paris, France ###
####################################################################

import os
import pygame

#######################################################################################
# Initiation
pygame.init()

# Display size setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Game title setting
pygame.display.set_caption("The Balloon Game")

# FPS
clock = pygame.time.Clock()
#######################################################################################

# 1. Initiation of user game (Background, game images, coordinates, speed, font, etc.)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

# Background
background = pygame.image.load(os.path.join(image_path, "background.png"))

# Stage
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # To put the character on the height of the stage

# Character
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height - stage_height

running = True
while running:
    dt = clock.tick(60)

    # 2. Event processing (Keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Definition of the game character's the position

    # 4. Collision processing

    # 5. Drawing on the screen
    screen.blit(background, (0, 0))
    screen.blit(stage, (0, screen_height -stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()

pygame.quit()