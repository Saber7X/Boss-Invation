class Setting:
    def __init__(self):
        """初始化游戏的设置。"""
        # 屏幕设置
        self.screen_width = 788  # 屏幕宽度
        self.screen_height = 661  # 屏幕高度
        self.bg_color = (240, 167, 50)  # 背景颜色
        self.bg_img = 'images/ground.png'  # 背景图片

        # 记分
        self.level_scale = 1.5  # 随关卡，难度提高速度。

        # 英雄设置
        self.hero_speed = 1.1  # 速度

        # 弹药设置
        self.fireBall_distance = 50.0  # 火球间隔距离,越大越疏,小小越密
        self.fireBall_speed = 1.5  # 火球的移动速度
        self.bullets_allowed = 30  # 存储苹果的数量

        # boss设置
        self.boss_speed = 1.0
        self.boss_direction = 1  # 方向：1 表示向右移，为-1 表示向左移。
        self.boss_health = 1  # boss血量
        self.fire_time = 3  # 发射火球的秒数间隔
        self.boss_health_img_width = 96  # boss血条的长度

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1  # 玩家每升一级后提升的难度
        self.initialize_dynamic_settings()  # 初始化游戏设置

    # 初始化
    def initialize_dynamic_settings(self):
        # 弹药设置
        self.fireBall_distance = 50.0  # 火球间隔距离,越大越疏,小小越密
        self.fireBall_speed = 1.5  # 火球的移动速度
        self.bullets_allowed = 30  # 存储苹果的数量

        # boss设置
        self.boss_speed = 1.0
        self.boss_direction = 1  # 方向：1 表示向右移，为-1 表示向左移。
        self.boss_health = 10  # boss血量
        self.fire_time = 10  # 发射火球的秒数间隔
        self.boss_health_img_width = 96  # boss血条的长度

    # 增加难度（下一轮）
    def increase_speed(self):
        self.boss_speed *= self.level_scale  # 增加boss移动速度
        self.fireBall_speed *= self.level_scale  # 增加火球飞行速度
        self.boss_health *= self.level_scale  # 增加Boss血量
        self.fire_time /= self.level_scale  # 减小火球发射间隔时间
