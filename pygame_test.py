import pygame
from pkg_resources import resource_filename
import geo2wall.extract as g2w


def quit_game():
    global run
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


def get_walls():
    # extract walls
    file = resource_filename("geo2wall", "shp/1og.shp")
    walls_h, walls_v = g2w.get_walls_from_geometry_file(
        file_path=file,
        kml_folder="Waende",
        rotation_angle=-99)
    return walls_h, walls_v


# a few values
walls_h, walls_v = get_walls()
vel = 1
wall_thickness = 4
wall_scale = 20
screen_size = (1920, 1080)
robot_size = (50, 50)
robot_start_pos = (50, 250)

run = True

# initialize screen and robot
pygame.init()

screen = pygame.display.set_mode(screen_size)

robot = pygame.image.load("robot_3Dblue.png")
robot = pygame.transform.scale(robot, robot_size)
robot_rect = robot.get_rect()
robot_rect.center = robot_start_pos

# create wall obstacles
vertical_obstacles = list()
horizontal_obstacles = list()
for wall in walls_v:
    wall *= wall_scale
    y_1, y_2 = screen_size[1] - wall[1], screen_size[1] - wall[3]
    if y_1 < y_2:
        top = y_1
    else:
        top = y_2
    if wall[0] < wall[2]:
        left = wall[0]
    else:
        left = wall[2]
    vertical_obstacles.append(pygame.Rect(left, top, wall_thickness, abs(y_2 - y_1)))
for wall in walls_h:
    wall *= wall_scale
    y_1, y_2 = screen_size[1] - wall[1], screen_size[1] - wall[3]
    if y_1 < y_2:
        top = y_1
    else:
        top = y_2
    if wall[0] < wall[2]:
        left = wall[0]
    else:
        left = wall[2]
    horizontal_obstacles.append(pygame.Rect(left, top, abs(wall[0] - wall[2]), wall_thickness))

# simulation loop
while run:
    # check if game is closed
    quit_game()
    # white background
    screen.fill((255, 255, 255))
    # fill in walls
    for wall in vertical_obstacles:
        pygame.draw.rect(screen, (0, 0, 0), wall, 1)
    for wall in horizontal_obstacles:
        pygame.draw.rect(screen, (0, 0, 0), wall, 1)
    # check for collisions
    move_restriction = [0, 0, 0, 0]
    collision_horizontal_list = robot_rect.collidelistall(horizontal_obstacles)
    for index in collision_horizontal_list:
        if horizontal_obstacles[index].centery < robot_rect.centery:
            move_restriction[2] = 1
        else:
            move_restriction[3] = 1
    collision_vertical_list = robot_rect.collidelistall(vertical_obstacles)
    for index in collision_vertical_list:
        if vertical_obstacles[index].centerx < robot_rect.centery:
            move_restriction[0] = 1
        else:
            move_restriction[1] = 1

    # move robot
    userInput = pygame.key.get_pressed()
    if userInput[pygame.K_LEFT] and move_restriction[0] == 0:
        robot_rect.x -= vel
    if userInput[pygame.K_RIGHT] and move_restriction[1] == 0:
        robot_rect.x += vel
    if userInput[pygame.K_UP] and move_restriction[2] == 0:
        robot_rect.y -= vel
    if userInput[pygame.K_DOWN] and move_restriction[3] == 0:
        robot_rect.y += vel

    # draw robot
    screen.blit(robot, (robot_rect.x, robot_rect.y))
    pygame.time.delay(10)
    pygame.display.update()
