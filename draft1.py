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
        self.force = 0
        # define starting angle, and this angle will help to make sure of angular speed
        self.theta = 0
    def draw(self):
        self.circle = pygame.draw.circle(screen, self.color, (self.x_pos, self.y_pos), self.radius)


    def Force(self):
        dx = self.x_pos - p1.x_pos
        dy = self.y_pos - p1.y_pos
        distance = math.sqrt(dx*dx + dy*dy)
        self.force = (Gravitation*p1.mass*self.mass)/distance*distance
        return self
    
    def revolve(self):
        dx = self.x_pos - p1.x_pos
        dy = self.y_pos - p1.y_pos
        radius = math.sqrt(dx*dx + dy*dy)

        self.x_pos = p1.x_pos + radius * math.cos(self.theta)
        self.y_pos = p1.y_pos + radius * math.sin(self.theta)
        self.theta += angular_speed  

class Orbits:
    def __init__(self, color, x_pos, y_pos, id,):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = color
        self.width = 3
        self.id = id
    def draw(self, x_pos, y_pos):
        dx = self.x_pos - p1.x_pos
        dy = self.y_pos - p1.y_pos
        radius = math.sqrt(dx*dx + dy*dy)
        self.circle = pygame.draw.circle(screen, self.color, (p1.x_pos, p1.y_pos), int(radius), self.width)

    

# intilizing instances 
p1 = Planet(518,332, 0,0, 1000, 'red', 60, 1)
p2 = Planet(139, 453, 0,0, 400,'blue',30,2)
p3 = Planet(308,438,0,0, 500, 'green', 20, 3)
p2.theta = 0

o1 = Orbits('white', p1.x_pos,p1.y_pos,9 )
o2 = Orbits('white', p1.x_pos, p1.y_pos,10)

# variables 
angular_speed = 0.02


force2 = p2.Force()
force3 = p3.Force()
print(f"F2 = ", force2, "F3 = ", force3)



# Game loop 
running = True 
while running:
    timer.tick(fps)
    screen.fill('black')

    p1.draw()
    p2.draw()
    p2.revolve()
    p3.draw()
    p3.revolve()
    o1.draw(p1.x_pos, p1.y_pos)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
pygame.quit()
