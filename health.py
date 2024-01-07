import pygame.font
from pygame.sprite import Group


# from ship import Ship


# 记分牌
class Health:
    """显示得分信息的类。"""

    def __init__(self, bi_game):
        """初始化显示得分涉及的属性。"""

        self.bi_game = bi_game

        self.screen = bi_game.screen  # 窗口
        self.screen_rect = self.screen.get_rect()  # 窗口参数
        self.settings = bi_game.Setting  # 设置参数
        self.stats = bi_game.stats  # 游戏数据
        # 显示得分信息时使用的字体设置。
        self.text_color = (43, 43, 43)  # 字体颜色
        self.font = pygame.font.SysFont(None, 19)  # 字体大小

        self.health = self.settings.boss_health
        self.now_health = self.stats.now_health
        self.width = 96
        self.height = 16
        self.prep_bgRec()
        self.prep_healthRec()
        self.prep_healthNumber()
        self.show()

    def prep_bgRec(self):
        """将得分转换为一幅渲染的图像。"""
        # 获取更新的分数
        self.bgRec = pygame.image.load('images/health_bg.png')
        self.bgRec_rect = self.bgRec.get_rect()
        self.bgRec_rect.midbottom = self.bi_game.boss.rect.midtop

    def prep_healthRec(self):
        """将得分转换prep_healthRec为一幅渲染的图像。"""
        # 获取更新的分数
        # self.healthRec = pygame.set_mode([self.width, self.height])
        # self.healthRec.fill([255, 0, 0])
        # self.healthRec =
        self.healthRec_rect = pygame.Rect(0, 0, self.width, self.height)
        self.healthRec_rect.midtop = self.bgRec_rect.midtop
        self.healthRec_rect.y += 2
        self.healthRec_rect.left = self.bgRec_rect.left + 2

    def prep_healthNumber(self):
        """将得分转换为一幅渲染的图像。"""
        now_health = round(self.now_health, 0)  # 保留到小数点后-1为，即十位
        now_health_str = "{:,}".format(now_health)  # 固定格式，数字转字符串时加入逗号
        health = round(self.health, 0)  # 保留到小数点后-1为，即十位
        health_str = "{:,}".format(health)  # 固定格式，数字转字符串时加入逗号

        self.healthNumber_image = self.font.render(f"{now_health_str} / {health_str}", True,
                                                   self.text_color)  # 创建文字图片
        # 在屏幕右上角显示得分。
        self.healthNumber_rect = self.healthNumber_image.get_rect()  # 获取上图的参数
        self.healthNumber_rect.center = self.bgRec_rect.center  # 指定位置，距离右边20
        # self.healthNumber_rect.y += 1 # 距离上面20

    def show(self):
        """在屏幕上显示得分。"""
        self.update()
        self.screen.blit(self.bgRec, self.bgRec_rect)  # 画图片
        # self.prep_healthRec()
        pygame.draw.rect(self.screen, [255, 0, 0], self.healthRec_rect, 0)
        # self.prep_healthNumber()
        self.screen.blit(self.healthNumber_image, self.healthNumber_rect)  # 画图片

    def update(self):
        self.health = self.bi_game.Setting.boss_health
        self.bgRec_rect.midbottom = self.bi_game.boss.rect.midtop
        self.healthRec_rect.midtop = self.bgRec_rect.midtop
        self.healthRec_rect.y += 2
        self.healthRec_rect.left = self.bgRec_rect.left + 2

        # print(self.width)

        self.now_health = self.bi_game.stats.now_health
        self.healthNumber_rect.midtop = self.bgRec_rect.midtop  # 指定位置，距离右边20
        self.healthNumber_rect.y += 3  # 距离上面20

        self.prep_healthRec()
        self.prep_healthNumber()
