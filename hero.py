import pygame, datetime


class Hero():
    def __init__(self, bi_game):
        super().__init__()
        # 优化帧率
        self.clock = pygame.time.Clock()
        self.dt = 0

        self.screen = bi_game.screen
        self.screen_rect = bi_game.screen.get_rect()

        # 加载英雄图像并获取其外接矩形。
        self.stand_img = 'images/stand.png'
        self.jump_img = 'images/jump.png'
        self.move_left_img = 'images/move-left.png'
        self.move_right_img = 'images/move-right.png'
        self.image = pygame.image.load(self.stand_img)
        self.rect = self.image.get_rect()

        # 把英雄放在地面上
        self.rect.midleft = self.screen_rect.midleft
        self.rect.y = 435

        # 英雄移动的状态
        self.moving_top = False
        self.moving_left = False
        self.moving_right = False
        self.moving_right = False
        self.bi_game = bi_game
        self.direction_y = -1

        # 游戏设置参数
        self.setting = bi_game.Setting

        self.jump_time = datetime.datetime.now().second
        self.jump_st = 0  # 0上 1下

    def update(self):
        if self.moving_top:

            self.image = pygame.image.load(self.jump_img)
            t = abs(datetime.datetime.now().second - self.jump_time)
            if self.moving_left:
                if self.jump_st == 0:
                    x = self.rect.x
                    y = self.rect.y
                    x -= 80
                    y -= 80
                    x = max(x, 0)
                    self.rect.x = x
                    self.rect.y = y
                    self.bi_game._update_screen()
                    self.jump_st = 1
                elif self.jump_st == 1 and t >= 3.5:
                    x = self.rect.x
                    y = self.rect.y
                    x -= 80
                    y += 80
                    x = max(x, 0)
                    self.rect.x = x
                    self.rect.y = y
                    self.jump_st = 0
                    self.bi_game._update_screen()
                    self.image = pygame.image.load(self.move_left_img)
                    self.moving_top = False
                self.bi_game._update_screen()
            elif self.moving_right:
                if self.jump_st == 0:
                    x = self.rect.x
                    y = self.rect.y
                    x += 80
                    y -= 80
                    x = min(x, 788 - self.rect.width)
                    self.rect.x = x
                    self.rect.y = y
                    self.bi_game._update_screen()
                    self.jump_st = 1
                elif self.jump_st == 1 and t >= 3.5:
                    x = self.rect.x
                    y = self.rect.y
                    x += 80
                    y += 80
                    x = min(x, 788 - self.rect.width)
                    self.rect.x = x
                    self.rect.y = y
                    self.jump_st = 0
                    self.bi_game._update_screen()
                    self.image = pygame.image.load(self.move_right_img)
                    self.moving_top = False
                self.bi_game._update_screen()
            else:
                if self.jump_st == 0:
                    y = self.rect.y
                    y -= 80
                    self.rect.y = y
                    self.bi_game._update_screen()
                    self.jump_st = 1
                elif self.jump_st == 1 and t >= 3.5:
                    y = self.rect.y
                    y += 80
                    self.rect.y = y
                    self.jump_st = 0
                    self.bi_game._update_screen()
                    self.image = pygame.image.load(self.stand_img)
                    self.moving_top = False
                    self.bi_game._update_screen()
                    self.moving_top = False
        if self.moving_left and self.rect.left > 0:
            self.image = pygame.image.load(self.move_left_img)
            self.rect.x -= 2
        # if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
        #     self.y += self.setting.ship_speed
        if self.moving_right and self.rect.right < 788:
            self.image = pygame.image.load(self.move_right_img)
            self.rect.x += 2

    def blitme(self):
        # 在指定位置绘制飞船   图像     位置
        # self.rect = self.image.get_rect()
        self.screen.blit(self.image, self.rect)

    def hero_reset(self):
        self.jump_st = 0
        self.image = pygame.image.load(self.stand_img)
        self.rect.midleft = self.screen_rect.midleft
        self.rect.y = 435
