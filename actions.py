import pydirectinput
import time
from config import MOVE_LEFT, MOVE_RIGHT, PULL_FISH

# 設定預設按鍵間隔，防止遊戲跳過太快的輸入
pydirectinput.PAUSE = 0.005

def press_left():
    """按下左鍵並放開右鍵"""
    # 某些遊戲需要先確保另一個鍵已放開
    pydirectinput.keyUp(MOVE_RIGHT)
    pydirectinput.keyDown(MOVE_LEFT)

def press_right():
    """按下右鍵並放開左鍵"""
    pydirectinput.keyUp(MOVE_LEFT)
    pydirectinput.keyDown(MOVE_RIGHT)

def stop_moving():
    """停止所有移動按鍵"""
    pydirectinput.keyUp(MOVE_LEFT)
    pydirectinput.keyUp(MOVE_RIGHT)

def interact():
    """按下互動/拉魚按鍵 (增加按下時間以確保觸發)"""
    pydirectinput.keyDown(PULL_FISH)
    time.sleep(0.1)
    pydirectinput.keyUp(PULL_FISH)

def click_at(x, y):
    """在指定座標點擊滑鼠左鍵"""
    # 先移動再點擊，有時直接點擊會失效
    pydirectinput.moveTo(x, y)
    time.sleep(0.05)
    pydirectinput.click()
