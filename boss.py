import pygame


class Boss():
    def __init__(self, bi_game):
        super().__init__()
        # 优化帧率
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.screen = bi_game.screen
        self.screen_rect = bi_game.screen.get_rect()

        # 加载英雄图像并获取其外接矩形。
        self.image = pygame.image.load('images/boss.png')
        self.rect = self.image.get_rect()

        # 把英雄放在地面上
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = 100
        # # 英雄移动的状态
        # self.moving_top = False
        # self.moving_left = False
        # self.moving_right = False
        # self.moving_right = False
        self.bi_game = bi_game

        # 游戏设置参数
        self.setting = bi_game.Setting

    def update(self):
        # 更新坐标
        # while self.setting.boss_health > 0:
        self.rect.x += self.setting.boss_speed * self.setting.boss_direction
        if self.rect.x <= 0 or self.rect.right >= self.screen.get_rect().right:  # 在速度不为1时><更好处理-1的情况
            self.setting.boss_direction *= -1

    def blitme(self):
        # 在指定位置绘制飞船   图像     位置
        # self.rect = self.image.get_rect()
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.midtop = self.screen_rect.midtop
        self.rect.y = 100
