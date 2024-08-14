# системные
# глобальные
import pyautogui
# локальные


__all__ = ['make']
w = 370
h = 500


def make(name=None):
	return pyautogui.screenshot(name, region=(1920-w, 1080-h, w, h-40))