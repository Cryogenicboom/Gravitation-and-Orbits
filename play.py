import pygame 
import math 

pygame.init()

# Configurations 
WIDTH = 1100
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH,HEIGHT])

fps = 60
timer = pygame.time.Clock()

Gravitation = 0.5


class Planet:
    def __init__(self, x_pos, y_pos, x_speed, y_speed, mass, color, radius, id):
        self.x_pos = x_pos 
        self.y_pos = y_pos
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.mass = mass
        self.color = color
        self.radius = radius
        self.id = id
        # define starting angle, and this angle will help to make sure of angular speed
        self.theta = 0
    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)


class Orbits:
    def __init__(self, radius, color, x_pos, y_pos, id,):
        self.radius = radius
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = 3
        self.id = id
    def draw(self, x_pos, y_pos):
        dx = p2.x_pos - p1.x_pos
        dy = p2.y_pos - p1.y_pos
        radius = math.sqrt(dx*dx + dy*dy)
        self.circle = pygame.draw.circle(screen, self.color, (p1.x_pos, p1.y_pos), int(radius), self.width)


# intilizing instances 
p1 = Planet(518,332, 0,0, 1000, 'red', 60, 1)
p2 = Planet(289, 304, 0,0, 400,'blue',30,2)
p2.theta = 0
o1 = Orbits(110, (0,0,0), p1.x_pos,p1.y_pos,9 )

# variables 
angular_speed = 0.02
Force = (Gravitation*p1.mass*p2.mass)/o1.radius*2
print(f"Force = ",Force)


# Game loop 
running = True 
while running:
    timer.tick(fps)
    screen.fill('black')

    p1.draw()

    dx = p2.x_pos - p1.x_pos
    dy = p2.y_pos - p1.y_pos
    radius = math.sqrt(dx*dx + dy*dy)

    p2.x_pos = p1.x_pos + radius * math.cos(p2.theta)
    p2.y_pos = p1.y_pos + radius * math.sin(p2.theta)
    p2.theta += angular_speed  # move along the orbit

    p2.draw()
    o1.draw(p1.x_pos, p1.y_pos)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
pygame.quit()