import pydirectinput
import time
import subprocess
from config import MOVE_LEFT, MOVE_RIGHT, PULL_FISH

# 設定預設按鍵間隔，防止遊戲跳過太快的輸入
pydirectinput.PAUSE = 0.005

def press_left():
    """按下左鍵並放開右鍵 (Windows版本)"""
    # 某些遊戲需要先確保另一個鍵已放開
    pydirectinput.keyUp(MOVE_RIGHT)
    pydirectinput.keyDown(MOVE_LEFT)

def press_right():
    """按下右鍵並放開左鍵 (Windows版本)"""
    pydirectinput.keyUp(MOVE_LEFT)
    pydirectinput.keyDown(MOVE_RIGHT)

def stop_moving():
    """停止所有移動按鍵 (Windows版本)"""
    pydirectinput.keyUp(MOVE_LEFT)
    pydirectinput.keyUp(MOVE_RIGHT)

def interact():
    """按下互動/拉魚按鍵 (增加按下時間以確保觸發) (Windows版本)"""
    pydirectinput.keyDown(PULL_FISH)
    time.sleep(0.1)
    pydirectinput.keyUp(PULL_FISH)

def click_at(x, y):
    """在指定座標點擊滑鼠左鍵 (Windows版本)"""
    # 先移動再點擊，有時直接點擊會失效
    pydirectinput.moveTo(x, y)
    time.sleep(0.05)
    pydirectinput.click()

def press_left_android():
    """在Android設備上按下左鍵"""
    try:
        subprocess.run(['adb', 'shell', 'input', 'keyevent', '21'], check=True, capture_output=True)
    except Exception as e:
        print(f"Android左鍵按壓錯誤: {e}")

def press_right_android():
    """在Android設備上按下右鍵"""
    try:
        subprocess.run(['adb', 'shell', 'input', 'keyevent', '22'], check=True, capture_output=True)
    except Exception as e:
        print(f"Android右鍵按壓錯誤: {e}")

def stop_moving_android():
    """在Android設備上停止移動"""
    # Android上通常不需要特別停止移動，因為是即時反應
    pass

def interact_android():
    """在Android設備上按下互動按鍵"""
    try:
        subprocess.run(['adb', 'shell', 'input', 'keyevent', '66'], check=True, capture_output=True)
    except Exception as e:
        print(f"Android互動按壓錯誤: {e}")

def click_at_android(x, y):
    """在Android設備上指定座標點擊"""
    try:
        subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)], check=True, capture_output=True)
    except Exception as e:
        print(f"Android點擊錯誤: {e}")
