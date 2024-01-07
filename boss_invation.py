import pygame, sys
from setting import Setting
from hero import Hero
from boss import Boss
from apple import Apple1
from fireBall import fireBall
import datetime
from health import Health
from stats import stats
from button import Button
from show_level import show_level


class BossInvation:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        # 运行控制
        self.running = True
        # 游戏设置参数
        self.Setting = Setting()
        self.screen = pygame.display.set_mode((self.Setting.screen_width, self.Setting.screen_height))
        self.clock = pygame.time.Clock()
        # 设置标题
        pygame.display.set_caption("Boss Invasion")
        # 游戏数据
        self.stats = stats(self)
        # 英雄人物
        self.hero = Hero(self)
        # boss
        self.boss = Boss(self)
        # 苹果
        self.apple = pygame.sprite.Group()
        self.if_fire_bullets = False
        # 火球
        self.fire_balls = pygame.sprite.Group()
        # 血条
        self.boss_health = Health(self)
        # 运行状态
        self.active = False
        # 按钮
        self.button = Button(self, "Start")
        # show_level
        self.level = show_level(self)

    def _check_apple_fireBall_collisions(self):
        collisions = pygame.sprite.groupcollide(  # 这个函数就是用作检测碰撞，然后删除的，True:删除，False就不删除
            self.apple, self.fire_balls, True, True)

    def _check_apple_boss_collisions(self):
        # collisions = pygame.sprite.groupcollide(  # 这个函数就是用作检测碰撞，然后删除的，True:删除，False就不删除
        #     self.apple, self.boss.image, True, True)
        for i in self.apple:
            # print(i)
            if i.rect.top <= self.boss.rect.bottom and (
                    i.rect.midtop[0] >= self.boss.rect.left and (i.rect.midtop[0] <= self.boss.rect.right) or (
                    i.rect.midtop[1] >= self.boss.rect.left and i.rect.midtop[1] <= self.boss.rect.right)):
                # print("碰到了1111111111111111111111111")
                self.boss_health.width = (96.0 * (self.boss_health.now_health / self.boss_health.health))

                self.apple.remove(i)
                self.boss_health.now_health -= 1
                self.stats.now_health -= 1  # 碰到后掉血

                self.boss_health.update()
                self.boss_health.update()
                print(self.boss_health.width, self.boss_health.now_health, self.boss_health.health)
                self.boss_health.show()
                self._update_screen()
                if (self.boss_health.now_health <= 0):
                    self.stats.next_round()
                    self.active = False
                    self.button._prep_msg("next round")  # 下一关
                    self._update_screen()
                    # self.stats.

    def _check_fireBall_hero_collisions(self):
        for i in self.fire_balls:
            b = self.hero.rect.top
            t = i.rect.bottom
            l = self.hero.rect.left

            if (((self.hero.rect.top <= i.rect.top and i.rect.top <= self.hero.rect.bottom) or (
                    self.hero.rect.top <= i.rect.bottom and i.rect.bottom <= self.hero.rect.bottom))
                    and
                    ((self.hero.rect.left <= i.rect.left and i.rect.left <= self.hero.rect.right) or (
                            self.hero.rect.left <= i.rect.right and i.rect.right <= self.hero.rect.right))):
                print("碰到了")
                self.fire_balls.remove(i)
                self.active = False
                self.button._prep_msg("Restart")
                self.stats.reset()

    # 单击按钮时开始游戏
    def _check_play_button(self, mouse_pos):
        if self.button.rect.collidepoint(
                mouse_pos) and self.active == False:  # 判断按钮元素是否碰到了指定坐标 同时要游戏处于关闭状态时才能有用
            print("点击按钮")
            self.active = True

    def _fire_bullet(self):
        # 判断持续开火  和   已经出现的子弹数量小于 储存子弹数量
        if self.if_fire_bullets and len(self.apple) < self.Setting.bullets_allowed:
            try:
                new_apple = Apple1(self)
                a = self.apple.sprites()[-1]
                for bullet in self.apple.sprites():
                    a = bullet
                # print(new_bullet.x, a.x, new_bullet.y, a.y)
                if abs(new_apple.rect.x - a.rect.x) + abs(new_apple.rect.y - a.rect.y) > self.Setting.fireBall_distance:
                    self.apple.add(new_apple)
                    new_apple.draw_bullet()
                # print(1)
            except IndexError:
                #  创建一颗子弹并加入编组
                new_bullet = Apple1(self)
                self.apple.add(new_bullet)
                new_apple.draw_bullet()

    def _fire_fireball(self):
        # 判断持续开火  和   已经出现的子弹数量小于 储存子弹数量
        try:
            new_ball = fireBall(self)
            f = self.fire_balls.sprites()[-1]
            # print(new_bullet.x, a.x, new_bullet.y, a.y)
            if abs(datetime.datetime.now().second - f.time) > self.Setting.fire_time:
                self.fire_balls.add(new_ball)
            # print(1)
        except IndexError:
            #  创建一颗子弹并加入编组
            new_bullet = fireBall(self)
            self.fire_balls.add(new_bullet)

    def _update_fireball(self):
        self.fire_balls.update()  # 更新所有在组中的子弹的位置  
        # 删除消失的子弹。
        for bullet in self.fire_balls.copy():  # 因为遍历的列表要保持不变，所以遍历副本，然后在主列表中进行删除
            if bullet.rect.bottom > 788:
                self.fire_balls.remove(bullet)  # 在列表中移除指定元素

    def _update_bullets(self):
        self.apple.update()  # 更新所有在组中的子弹的位置
        self._fire_bullet()  # 持续开火
        # 删除消失的子弹。
        for bullet in self.apple.copy():  # 因为遍历的列表要保持不变，所以遍历副本，然后在主列表中进行删除
            if bullet.rect.bottom <= 0 or bullet.rect.right > 790 or bullet.rect.left < 0 or bullet.rect.top > 661:
                self.apple.remove(bullet)  # 在列表中移除指定元素
                # print(len(self.bullets))
        # 检测外星人与子弹相撞，然后就删除
        # self._check_bullet_alien_collisions()
        # 同时进行

    # 检测事件
    def _check_events(self):
        self._check_apple_boss_collisions()
        self._check_apple_fireBall_collisions()
        self._check_fireBall_hero_collisions()
        for event in pygame.event.get():

            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:  # 点击X
                self.running = False  # 退出循环
            # 监视键盘按下事件
            elif event.type == pygame.KEYDOWN:  # 识别键盘事件

                self._check_keydown_events(event, self.hero.rect.y)
                # print(self.hero.rect)
            # 监视键盘松开事件
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标单击事件
                mouse_pos = pygame.mouse.get_pos()  # 点击坐标
                self._check_play_button(mouse_pos)  # 检测是否点击在按钮上面

    # 按下键盘事件
    def _check_keydown_events(self, event, y):
        # 移动图片---------------------------------------------（待优化帧率） 已优化

        if event.key == pygame.K_w:
            if self.hero.moving_top == True:  # w 跳跃
                pass
            else:
                self.hero.moving_top = True  # 开始持续移动

        elif event.key == pygame.K_a:  # a 向左移动
            self.hero.moving_left = True  # 开始持续移动
        elif event.key == pygame.K_s:  # s 下蹲
            self.hero.moving_bottom = True  # 开始持续移动
        elif event.key == pygame.K_d:  # d 向右移动
            if self.hero.moving_top == False:
                self.hero.image = pygame.image.load(self.hero.move_right_img)
            self.hero.moving_right = True  # 开始持续移动
        elif event.key == pygame.K_q:  # 按Q退出
            self.running = False
        elif event.key == pygame.K_SPACE:  # 按空格开火
            self.if_fire_bullets = True
            # self._fire_bullet()

    # 松开键盘事件
    def _check_keyup_events(self, event):
        # if event.key == pygame.K_w:  # w
        #     self.hero.moving_top = False  # 关闭持续移动
        if event.key == pygame.K_a:
            if self.hero.moving_right != True and self.hero.moving_top == False:
                self.hero.image = pygame.image.load(self.hero.stand_img)
            self.hero.moving_left = False  # 关闭持续移动
        elif event.key == pygame.K_s and self.hero.moving_top != True:
            self.hero.moving_bottom = False  # 关闭持续移动
        elif event.key == pygame.K_d:  # d
            if self.hero.moving_left != True and self.hero.moving_top == False:
                self.hero.image = pygame.image.load(self.hero.stand_img)
            self.hero.moving_right = False  # 关闭持续移动
        elif event.key == pygame.K_SPACE:  # 按空格开火
            self.if_fire_bullets = False

    # 更新屏幕
    def _update_screen(self):
        # 背景颜色
        self.screen.fill(self.Setting.bg_color)
        # 显示背景图片
        self.bg_img = pygame.image.load(self.Setting.bg_img)
        self.bg_img_rect = self.bg_img.get_rect()
        self.bg_img_rect.midbottom = self.screen.get_rect().midbottom
        self.screen.blit(self.bg_img, self.bg_img_rect)

        # 显示英雄
        self.hero.blitme()

        # 显示boss
        self.boss.blitme()
        self.boss_health.update()
        # 帧率
        self.clock.tick(60)  # limits FPS to 60
        # 绘制苹果
        for a in self.apple.sprites():
            a.draw_bullet()
        # 绘制火球
        for a in self.fire_balls.sprites():
            a.draw_bullet()
        # 显示血条
        self.boss_health.show()
        if self.active == False:
            self.button.draw_button()

        # 绘制当前关卡
        self.level.show()
        pygame.display.flip()

    def run_game(self):
        """开始游戏的主循环"""
        while self.running:

            self._check_events()  # 检测事件
            self._update_screen()  # 更新屏幕
            if self.active:
                self._update_bullets()  # 更新苹果
                self.hero.update()
                self.boss.update()
                self._fire_fireball()
                self._update_fireball()

    def quit_game(self):
        pygame.quit()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    bi = BossInvation()
    bi.run_game()
    bi.quit_game()
