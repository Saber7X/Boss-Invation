class stats():
    def __init__(self, bi_game):
        self.bi_game = bi_game
        self.screen = bi_game.screen  # 窗口
        self.screen_rect = self.screen.get_rect()  # 窗口参数
        self.settings = bi_game.Setting  # 设置参数
        self.now_health = self.settings.boss_health  # 游戏数据
        self.level = 1
        self.highest_level = 1

    def update(self):  # 更新最大值
        self.highest_level = max(self.level, self.highest_level)

    def next_round(self):
        self.level += 1
        self.bi_game.Setting.increase_speed()
        self.now_health = self.bi_game.Setting.boss_health
        self.update()

    # 初始化
    def reset(self):
        self.level = 1
        self.bi_game.Setting.initialize_dynamic_settings()
        self.now_health = self.bi_game.Setting.boss_health
        self.bi_game.hero.hero_reset()
        for i in self.bi_game.apple:
            self.bi_game.apple.remove(i)
        for i in self.bi_game.fire_balls:
            self.bi_game.fire_balls.remove(i)
        self.bi_game.boss_health.width = 96
        self.bi_game.boss.reset()
