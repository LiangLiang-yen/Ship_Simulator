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
resistance = Decimal('0.05')


class Ship_topView(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, *groups):
        super().__init__(*groups)
        self.raw_image = pygame.image.load("ship_topView.jpg").convert_alpha()
        # 縮小圖片
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        # 回傳位置
        self.rect = self.image.get_rect()
        # 定位
        self.rect.topleft = (x, y)


class Ship(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, *groups):
        super().__init__(*groups)
        self.raw_image = pygame.image.load("ship_img.png").convert_alpha()
        # 縮小圖片
        self.image = pygame.transform.scale(self.raw_image, (width, height))
        # 回傳位置
        self.rect = self.image.get_rect()
        # 定位
        self.rect.topleft = (x, y)


def main():
    pygame.init()  # Initialization
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Create window surface
    pygame.display.set_caption('Ship')  # Set window title

    ocean1 = pygame.Rect(Screen[1]['x'], Screen[1]['y'] + Screen[1]['height'] * .75,
                         Screen[1]['width'], Screen[1]['height'] * .25)  # Ocean1 Create
    ocean2 = pygame.Rect(Screen[2]['x'], Screen[2]['y'],
                         Screen[2]['width'], Screen[2]['height'])  # Ocean1 Create

    shipPosition = {'x': Screen[1]['x'] + Screen[1]['width'] - shipSize['width'],
                    'y': Screen[1]['height'] * .75 - shipSize['height']}  # Ship Create
    ship_topView_Position = {'x': Screen[2]['x'] + Screen[2]['width'] - shipSize['width'],
                             'y': Screen[2]['height'] * .5}  # Ship Create

    # Accelerate Initialization
    accel_x = Decimal('0')
    decrease = False

    main_clock = pygame.time.Clock()
    while True:  # 死迴圈確保視窗一直顯示
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            accel_x = Decimal('-3.0')
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            accel_x = Decimal('3.0')
        for event in pygame.event.get():  # 遍歷所有事件
            if event.type == pygame.QUIT:  # 如果單擊關閉視窗，則退出
                sys.exit()
            elif event.type == pygame.KEYUP:
                decrease = True

        # Accelerate
        if decrease is True and abs(accel_x) > 0:
            if accel_x > 0:
                accel_x -= resistance
            else:
                accel_x += resistance
        else:
            decrease = False

        # print(accel_x)
        change_x = accel_x
        # if change_x + shipPosition['x'] >= WINDOW_WIDTH - shipSize['width']:
        #     change_x = 0
        # elif change_x + shipPosition['x'] <= 0:
        #     change_x = 0
        shipPosition['x'] += change_x
        # Clear Surface
        window_surface.fill(WHITE)
        # Draw Ocean
        pygame.draw.rect(window_surface, BLUE, ocean1)
        pygame.draw.rect(window_surface, BLUE, ocean2)
        # Draw Ship
        ship = Ship(shipSize['width'], shipSize['height'], shipPosition['x'], shipPosition['y'])
        ship_topView = Ship_topView(shipSize['width'], shipSize['height'], ship_topView_Position['x'], ship_topView_Position['y'])
        window_surface.blit(ship.image, ship.rect)
        window_surface.blit(ship_topView.image, ship_topView.rect)
        # 更新全部顯示
        pygame.display.flip()


if __name__ == '__main__':
    main()
