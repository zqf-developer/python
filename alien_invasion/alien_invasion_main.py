"""
alien_invasion这个包名不能与程序名同名，否则import的时候无法生效
"""
import pygame

from alien_invasion.settings import Settings

from alien_invasion.ship import Ship

import alien_invasion.game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色
    # bg_color = (230, 230, 230)

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)


run_game()
