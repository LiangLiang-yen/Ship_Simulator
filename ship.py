from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import sys
import pygame
from decimal import Decimal

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 600
Screen = {1: {'width': 800, 'height': 600, 'x': 0, 'y': 0}, 2: {'width': 800, 'height': 600, 'x': 800, 'y': 0}}
WHITE = (255, 255, 255)
BLUE = (29, 162, 216)
FPS = 60
shipSize = {"width": 160, "height": 100}
resistance = Decimal('0.005')
speed = Decimal('1.0')

pygame.init()  # Initialization
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Create window surface
pygame.display.set_caption('Ship')  # Set window title
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)  # Show text
clock.tick(FPS)


class Ship:
    def __init__(self, width, height, x, y):
        self.x = Decimal(str(x))
        self.y = Decimal(str(y))
        self.raw_image = pygame.image.load("ship_img.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))  # scale image
        self.ACC_X = 0

    def move(self, position_x):
        self.ACC_X = position_x
        self.x += self.ACC_X

    def stop(self):  # 慣性
        if abs(self.ACC_X) > 0:
            if self.ACC_X > 0:
                self.ACC_X -= resistance
            else:
                self.ACC_X += resistance
            self.x += self.ACC_X

    def draw(self):
        global font
        text = font.render("ACC_X: {}".format(self.ACC_X), True, (0, 0, 0))
        rect = self.image.get_rect(topleft=(self.x, self.y))
        window_surface.blit(text, text.get_rect(topleft=(0, 0)))
        window_surface.blit(self.image, rect)


class Ship_topView(Ship):
    def __init__(self, width, height, x, y):
        super().__init__(width, height, x, y)
        self.raw_image = pygame.image.load("ship_topView_img.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (width, height))  # scale image
        self.ACC_Y = 0

    def move_vertical(self, position_y):
        self.ACC_Y = position_y
        self.y += self.ACC_Y

    def stop(self):
        super().stop()
        if abs(self.ACC_Y) > 0:
            if self.ACC_Y > 0:
                self.ACC_Y -= resistance
            else:
                self.ACC_Y += resistance
            self.y += self.ACC_Y

    def draw(self):
        super().draw()
        global font
        text = font.render("ACC_Y: {}".format(self.ACC_Y), True, (0, 0, 0))
        window_surface.blit(text, text.get_rect(topleft=(0, 40)))


def draw_win(ship1, ship2):
    ocean1 = pygame.Rect(Screen[1]['x'], Screen[1]['y'] + Screen[1]['height'] * .75,
                         Screen[1]['width'], Screen[1]['height'] * .25)  # Ocean1 Create
    ocean2 = pygame.Rect(Screen[2]['x'], Screen[2]['y'],
                         Screen[2]['width'], Screen[2]['height'])  # Ocean1 Create
    window_surface.fill(WHITE)  # Clear Surface
    # Draw Ocean
    pygame.draw.rect(window_surface, BLUE, ocean1)
    pygame.draw.rect(window_surface, BLUE, ocean2)
    # Draw Ship
    ship1.draw()
    ship2.draw()
    pygame.display.update()


def main():
    shipPosition = {'x': Screen[1]['x'] + Screen[1]['width'] - shipSize['width'],
                    'y': Screen[1]['height'] * .75 - shipSize['height']}  # Ship Create
    ship_topView_Position = {'x': Screen[2]['x'] + Screen[2]['width'] - shipSize['width'],
                             'y': Screen[2]['height'] * .5 - shipSize['height'] * .5}  # Ship Create

    ship = Ship(shipSize['width'], shipSize['height'], shipPosition['x'], shipPosition['y'])
    ship_topView = Ship_topView(shipSize['width'], shipSize['height'], ship_topView_Position['x'],
                                ship_topView_Position['y'])
    while True:  # 死迴圈確保視窗一直顯示
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            ship.move(-speed)
            ship_topView.move(-speed)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            ship.move(speed)
            ship_topView.move(speed)
        if pygame.key.get_pressed()[pygame.K_UP]:
            ship_topView.move_vertical(-speed)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            ship_topView.move_vertical(speed)
        if not pygame.key.get_pressed()[pygame.K_LEFT] and \
                not pygame.key.get_pressed()[pygame.K_RIGHT] and \
                not pygame.key.get_pressed()[pygame.K_UP] and \
                not pygame.key.get_pressed()[pygame.K_DOWN]:
            ship.stop()
            ship_topView.stop()
        for event in pygame.event.get():  # 遍歷所有事件
            if event.type == pygame.QUIT:  # 如果單擊關閉視窗，則退出
                sys.exit()
        draw_win(ship, ship_topView)


main()
