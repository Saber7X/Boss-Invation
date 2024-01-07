import random

import pygame
from pygame.sprite import Sprite  # 可以同时操作很多元素


# 继承Sprite
class Apple1(Sprite):
    # 管理苹果

    def __init__(self, bi_game):
        super().__init__()  # 我想继承它的作用应该就是为了方便存储在他的group里面
        # 在飞船的位置创建一个子弹对象
        self.screen = bi_game.screen
        self.setting = bi_game.Setting
        self.direction = 1

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置。
        # 感觉是直接创建了一个rect对象,由于是自建,所以无需get
        self.images = pygame.image.load('images/bullet.png')
        self.rect = self.images.get_rect()

        self.rect.midbottom = bi_game.hero.rect.midtop  # 与飞机顶部中间对齐
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.goal_x = bi_game.mouse_x
        self.goal_y = bi_game.mouse_y

        self.z = False
        if float(self.rect.x - self.goal_x) == 0:
            self.z = True
        if self.z == False:
            self.direction = float(self.rect.y - self.goal_y) / float(self.rect.x - self.goal_x)

        self.f = 1
        if self.goal_x < self.x:
            self.f = -1

    def update(self):
        s = 1
        # if 10 < abs(self.direction):
        #     s = 0.5
        # 向上移动子弹
        # 更新子弹坐标
        # self.x = float(self.images.get_rect().x)
        # self.y = float(self.images.get_rect().y)
        self.x += float(1 * self.f * s)
        self.y += float(self.direction * self.f * s)
        print(float(1 * self.f * s), float(self.direction * self.f * s))
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        print(self.rect)
        self.screen.blit(self.images, self.rect)
