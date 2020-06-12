import sys

import pygame
import numpy as np

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (29, 162, 216)
FPS = 60
shipSize = {"width": 160, "height": 100}


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
    window_surface.fill(WHITE)  # Clear surface and fill background color
    ocean = pygame.Rect(0, WINDOW_HEIGHT * 0.75, WINDOW_WIDTH, WINDOW_HEIGHT * 0.25)  # Ocean Create
    shipPosition = {'x': WINDOW_WIDTH * .5, 'y': WINDOW_HEIGHT * .75 - shipSize['height']}  # Ship Create
    # Accelerate Initialization
    accel_x = 0
    change_x = 0

    main_clock = pygame.time.Clock()
    while True:  # 死迴圈確保視窗一直顯示
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            accel_x = -.2
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            accel_x = .2
        for event in pygame.event.get():  # 遍歷所有事件
            if event.type == pygame.QUIT:  # 如果單擊關閉視窗，則退出
                sys.exit()
            elif event.type == pygame.KEYUP:
                accel_x = 0

        # Accelerate
        change_x += accel_x
        if change_x + shipPosition['x'] >= WINDOW_WIDTH - shipSize['width']:
            change_x = 0
        elif change_x + shipPosition['x'] <= 0:
            change_x = 0
        shipPosition['x'] += change_x
        # Clear Surface
        window_surface.fill(WHITE)
        # Draw Ocean
        pygame.draw.rect(window_surface, BLUE, ocean)
        # Draw Ship
        ship = Ship(shipSize['width'], shipSize['height'], shipPosition['x'], shipPosition['y'])
        window_surface.blit(ship.image, ship.rect)
        # 更新全部顯示
        pygame.display.flip()


if __name__ == '__main__':
    main()
