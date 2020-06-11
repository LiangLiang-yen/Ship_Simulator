import sys

import pygame
from pygame.locals import QUIT

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
    # 初始化
    pygame.init()
    # 建立 window 視窗畫布，大小為 800x600
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    # 設置視窗標題為 Ship
    pygame.display.set_caption('Ship')
    # 清除畫面並填滿背景色
    window_surface.fill(WHITE)
    ocean = pygame.Rect(0, WINDOW_HEIGHT * 0.75, WINDOW_WIDTH, WINDOW_HEIGHT * 0.25)

    shipPosition = {'x': WINDOW_WIDTH * .5, 'y': WINDOW_HEIGHT * .75 - shipSize['height']}
    ship = Ship(shipSize['width'], shipSize['height'], shipPosition['x'], shipPosition['y'])

    main_clock = pygame.time.Clock()
    while True:  # 死迴圈確保視窗一直顯示
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if shipPosition['x'] - 5 > 0:
                shipPosition['x'] = shipPosition['x'] - 5
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            shipPosition['x'] = shipPosition['x'] + 5
        for event in pygame.event.get():  # 遍歷所有事件
            if event.type == pygame.QUIT:  # 如果單擊關閉視窗，則退出
                sys.exit()

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
