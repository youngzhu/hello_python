import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("外星人入侵v1")

        self.ship = Ship(self)
        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self._create_fleet()

        # 不能直接省略
        # 对象的属性必须都在init方法中初始化
        self.game_active = False

        self.play_button = Button(self, 'Play')

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_alien()

            # Redraw the screen during each pass through the loop.
            self._update_screen()
            
            # tick() ⽅法接受⼀个参数：游戏的帧率。
            # 这⾥使⽤的值为 60， Pygame 将尽可能确保这个循环每秒恰好运⾏ 60 次
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.settings.initialize_dynamic_settings()
            # Reset the game statistics.
            self.stats.reset_stats()
            self.scoreboard.prep_score()
            self.scoreboard.prep_level()
            self.scoreboard.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        # 在使⽤ for 循环遍历列表（或 Pygame 编组）时，Python 要求该列表的⻓度在整个循环中保持不变。
        # 这意味着不能从 for 循环遍历的列表或编组中删除元素，因此必须遍历编组的副本。
        # 使⽤⽅法 copy() 来作为 for 循环的遍历对象，让我们能够在循环中修改原始编组 bullets。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Respond to bullet-alien collisions."""
        # Remove any bullets and aliens that have collided.
        # 两个值为 True 的实参告诉 Pygame 在发⽣碰撞时删除对应的⼦弹和外星⼈
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)

        # 更新得分
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()

        # 外星舰队全部被消灭 
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提升等级
            self.stats.level += 1
            self.scoreboard.prep_level()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # 将这个循环放在绘制⻜船的代码⾏前⾯，以防⼦弹出现在⻜船上
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        self.scoreboard.show_score()

        # 如果游戏处于非活动状态，则展示Play按钮
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        # 为了获取外星人的宽度而创建
        alien = Alien(self)
        # 属性 rect.size 是⼀个元组，包含外星⼈的宽度和⾼度
        alien_width, alien_height = alien.rect.size

        current_x = alien_width
        current_y = alien_height

        while current_y < self.settings.screen_height - 3*alien_height:
            while current_x < self.settings.screen_width - 2 * alien_width:
                self._create_alien(current_x, current_y)
                # 递增 current_x 的值
                # 将其值加上外星⼈宽度的两倍，从⽽越过刚添加的外星⼈，并在外星⼈之间留下⼀些空间
                current_x += 2 * alien_width

            # 添加完一行外星人后，重置x，递增y
            current_x = alien_width
            current_y += 2 * alien_height


    def _create_alien(self, position_x, position_y):
        alien = Alien(self)
        alien.x = position_x
        alien.rect.x = position_x
        alien.rect.y = position_y
        self.aliens.add(alien)

    def _update_alien(self):
        """更新舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            self.scoreboard.prep_ships()

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            # 我们根本没有创建多艘⻜船。在整个游戏运⾏期间，只创建了⼀个⻜船实例，并在该⻜船被撞到时将其居中。
            # 统计信息 ships_left 指出玩家是否⽤完了所有的⻜船
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()