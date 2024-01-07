import random

import pygame
from pygame.sprite import Sprite  # 可以同时操作很多元素
import datetime


# 继承Sprite
class fireBall(Sprite):
    # 管理苹果
    def __init__(self, bi_game):
        super().__init__()  # 我想继承它的作用应该就是为了方便存储在他的group里面
        # 在英雄的位置创建一个子弹对象
        self.time = datetime.datetime.now().second
        self.direction = 1
        self.screen = bi_game.screen
        self.setting = bi_game.Setting

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置。
        # 感觉是直接创建了一个rect对象,由于是自建,所以无需get
        self.images = pygame.image.load('images/fireball.png')
        self.rect = self.images.get_rect()
        self.rect.midtop = bi_game.boss.rect.midbottom  # 与飞机顶部中间对齐

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.goal_x = bi_game.hero.rect.x
        self.goal_y = bi_game.hero.rect.y

        self.z = False
        if float(bi_game.boss.rect.x - self.goal_x) == 0:
            self.z = True
        if self.z == False:
            self.direction = float(bi_game.boss.rect.y - self.goal_y) / float(bi_game.boss.rect.x - self.goal_x)

        self.f = 1
        if bi_game.boss.rect.x >= bi_game.hero.rect.x:
            self.f = -1

    def update(self):
        s = 1
        # if abs(self.direction) >= 10:
        #     s = 0.1
        self.x += float(1 * self.f * s)
        self.y += abs(self.direction * s)
        self.rect.x = self.x
        self.rect.y = self.y

    def draw_bullet(self):
        # 绘制子弹
        self.screen.blit(self.images, self.rect)
