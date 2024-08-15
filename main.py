# системные
from time import sleep, time
from threading import Thread

# глобальные
import pyautogui
import pygame
from pygame import display
from pygame.locals import *

# локальные
from local import tesseract, screenshot, minecraft


pygame.init()
win = display.set_mode((800, 450), RESIZABLE)
clock = pygame.time.Clock()
clock2 = pygame.time.Clock()
font = pygame.font.SysFont('Consolas', 16)
running = True
lines = {}

def draw():
	global lines
	while running:
		image = screenshot.make()
		# 0.05390453338623047 s

		text = tesseract.proc(image)
		try:
			ll = text.split('\n')
		except:
			ll = [text]
		# 0.15065479278564453 s

		# print(lines)
		lines = minecraft.proc(ll)

		win.fill((30,30,30))
		image = font.render(str(int(clock2.get_fps())), True, (0, 255, 0))
		win.blit(image, (5, 5))
		for i, line in enumerate(lines):
			image = font.render(line, True, (255, 0, 0))
			win.blit(image, (5, 5+16*(i+1)))
		display.flip()

		clock2.tick(30)

def check():
	global lines
	fishing = None

	while running:
		if (minecraft.sounds[1] in lines) and (lines[minecraft.sounds[1]] >= 0.75):
			if fishing == True:
				pyautogui.rightClick()
				fishing = False
			else:
				sleep(0.5)
				pyautogui.rightClick()
				fishing = True
				sleep(3)

		elif (minecraft.sounds[3] in lines) and (lines[minecraft.sounds[3]] >= 0.75):
			fishing = False
		sleep(0.15)

Thread(target=draw, daemon=True).start()
Thread(target=check, daemon=True).start()

while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

	clock.tick(15)