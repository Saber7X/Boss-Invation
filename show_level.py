import pygame.font
from pygame.sprite import Group


# from ship import Ship


# 记分牌
class show_level:
    """显示得分信息的类。"""

    def __init__(self, bi_game):
        """初始化显示得分涉及的属性。"""

        self.bi_game = bi_game

        self.screen = bi_game.screen  # 窗口
        self.screen_rect = self.screen.get_rect()  # 窗口参数
        self.settings = bi_game.Setting  # 设置参数
        self.stats = bi_game.stats  # 游戏数据
        # 显示得分信息时使用的字体设置。
        self.text_color = (201, 221, 227)  # 字体颜色
        self.font = pygame.font.SysFont(None, 25)  # 字体大小

    def prep_bg(self):
        """将得分转换为一幅渲染的图像。"""
        # 获取更新的分数
        self.bg = pygame.image.load('images/board.png')
        self.bg_rect = self.bg.get_rect()
        self.bg_rect.midtop = self.screen_rect.midtop

    def prep_level_image(self):
        """将得分转换prep_healthRec为一幅渲染的图像。"""
        self.level = self.bi_game.stats.level
        self.level_str = "{:,}".format(self.level)
        self.level_img = self.font.render(f"NOW LEVEL: {self.level_str}", True,
                                          self.text_color)
        self.level_img_rect = self.level_img.get_rect()
        self.level_img_rect.midtop = self.bg_rect.midtop
        # self.level_img_rect.x += 50
        self.level_img_rect.y += 20

    def prep_highest_level_image(self):
        """将得分转换prep_healthRec为一幅渲染的图像。"""
        self.highest_level = self.bi_game.stats.highest_level
        self.highest_level_str = "{:,}".format(self.highest_level)
        self.highest_level_img = self.font.render(f"HIGHEST LEVEL: {self.highest_level_str}", True,
                                                  self.text_color)
        self.highest_level_img_rect = self.highest_level_img.get_rect()
        self.highest_level_img_rect.midtop = self.level_img_rect.midbottom
        self.highest_level_img_rect.y += 3.5

    def show(self):
        self.prep_bg()
        self.prep_level_image()
        self.prep_highest_level_image()
        self.screen.blit(self.bg, self.bg_rect)  # 画图片
        self.screen.blit(self.level_img, self.level_img_rect)  # 画图片
        self.screen.blit(self.highest_level_img, self.highest_level_img_rect)  # 画图片

    # def update(self):
    #     self.health = self.bi_game.Setting.boss_health
    #     self.bgRec_rect.midbottom = self.bi_game.boss.rect.midtop
    #     self.healthRec_rect.midtop = self.bgRec_rect.midtop
    #     self.healthRec_rect.y += 2
    #     self.healthRec_rect.left = self.bgRec_rect.left + 2
    #
    #     # print(self.width)
    #
    #     self.now_health = self.bi_game.stats.now_health
    #     self.healthNumber_rect.midtop = self.bgRec_rect.midtop  # 指定位置，距离右边20
    #     self.healthNumber_rect.y += 3  # 距离上面20
    #
    #     self.prep_healthRec()
    #     self.prep_healthNumber()
