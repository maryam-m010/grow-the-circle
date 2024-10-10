import pygame, sys
pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("grow the circle")
screen.fill("pink")
pygame.display.update()

class Circle:
    def __init__(self, color, pos, radius, width):
        self.c_color = color
        self.c_pos = pos
        self.c_radius = radius
        self.c_width = width
        self.c_surface = screen
    def draw(self):
        pygame.draw.circle(self.c_surface, self.c_color, self.c_pos, self.c_radius, self.c_width)
    
    def grow(self, r):
        self.c_radius += r 
        pygame.draw.circle(self.c_surface, self.c_color, self.c_pos, self.c_radius, self.c_width)

circle1 = Circle("blue", (300,300), 20, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("pink")
            circle1.draw()
            pygame.display.update()
        
        elif event.type == pygame.MOUSEBUTTONUP:
            screen.fill("pink")
            circle1.grow(50)
            pygame.display.update()

