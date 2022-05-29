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

# Character moving direction
character_to_x = 0

# Character moving speed
character_speed = 5

# Weapon
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = character_size[0]

weapons = []

# Weapon speed
weapon_speed = 10

# Ball creation
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# Ball speed
ball_speed_y = [-15, -12, -9, -6]

# Balls
balls = []

balls.append({
    "pos_x" : 50,
    "pos_y" : 50,
    "img_idx" : 0,
    "to_x" : 3, # if it's -3, then to the left, and if it's 3, then to the right
    "to_y" : -5,
    "init_spd_y" : ball_speed_y[0]})

running = True
while running:
    dt = clock.tick(30)

    # 2. Event processing (Keyboard, mouse, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: # the character to left
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # the character to right
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # the character using weapon
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                charactere_to_x = 0

    # 3. Definition of the game character's the position
    character_x_pos += character_to_x
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # Weapon position
    weapons = [[w[0], w[1] - weapon_speed] for w in weapons]

    # Weapon disappearing when it touches the edge
    weapons = [[w[0], w[1]] for w in weapons if w[1] > 0]

    # Definition of the position of balls
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx =ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.45

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]

    # 4. Collision processing

    # 5. Drawing on the screen
    screen.blit(background, (0, 0))

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))

    screen.blit(stage, (0, screen_height -stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))



    pygame.display.update()

pygame.quit()