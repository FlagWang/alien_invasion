# _*_ coding:utf-8 _*_

import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	#设置游戏主界面背景色
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(screen)


	#游戏主循环
	while True:

		#监听键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#刷新背景色
		screen.fill(ai_settings.bg_color)
		
		ship.blitme()
		
		#刷新最近绘制的屏幕
		pygame.display.flip()

run_game()