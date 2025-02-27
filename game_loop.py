import pygame
import random
import math

screen_width = 1000
screen_hight = 1000
BASE_COLOR = (130, 0, 130)

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_hight))
done = False

number_of_stars = 40
SPEED = 0.1
stars = []

def new_star() -> list:
    x = random.randint(-screen_width // 2, screen_width // 2)
    y = random.randint(-screen_hight // 2, screen_hight // 2)
    z = 256
    color = 0
    rotation_angle = random.uniform(0, 360)
    return [x, y, z, color, rotation_angle]

def apply_brightness(color, brightness):
    r = int(color[0] * (brightness / 200))
    g = int(color[1] * (brightness / 200))
    b = int(color[2] * (brightness / 200))
    return (r, g, b)

def move_and_check(star: list) -> list:
    screen_center_x = screen_width // 2
    screen_center_y = screen_hight // 2

    x = star[0] * 256 / star[2] + screen_center_x
    y = star[1] * 256 / star[2] + screen_center_y

    star[2] -= SPEED

    if (x < 0 or x > screen_width) or (y < 0 or y > screen_hight):
        star = new_star()

    if star[3] < 255:
        star[3] += 0.15

    if star[3] > 255:
        star[3] = 255


    star[4] += 0.2
    if star[4] >= 360:
        star[4] -= 360

    return star

def draw_star(star: list) -> None:
    screen_center_x = screen_width // 2
    screen_center_y = screen_hight // 2

    x = int(star[0] * 256 / star[2] + screen_center_x)
    y = int(star[1] * 256 / star[2] + screen_center_y)

    outer_radius = 6
    inner_radius = 3  

    rotation_angle = star[4]

    points = []
    for i in range(12):
        angle = math.radians(30 * i + rotation_angle)
        if i % 2 == 0:

            px = x + outer_radius * math.cos(angle)
            py = y - outer_radius * math.sin(angle)
        else:

            px = x + inner_radius * math.cos(angle)
            py = y - inner_radius * math.sin(angle)
        points.append((px, py))
        color = apply_brightness(BASE_COLOR, star[3])

    pygame.draw.polygon(screen, color, points)

for i in range(0, number_of_stars):
    stars.append(new_star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))

    for i in range(0, number_of_stars):
        s = stars[i]

        s = move_and_check(s)
        stars[i] = s

        draw_star(s)

    pygame.display.flip()

pygame.quit()