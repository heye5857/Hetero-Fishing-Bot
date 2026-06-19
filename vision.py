import cv2
import numpy as np
import mss
import subprocess
import os
from config import LOWER_GREEN, UPPER_GREEN, LOWER_CURSOR, UPPER_CURSOR, FISHING_REGION

def grab_screen(region=None):
    """
    擷取螢幕畫面 (Windows版本)
    :param region: 擷取區域 (dict)，格式如 {"top": y, "left": x, "width": w, "height": h}
    :return: BGR 格式的 numpy 陣列影像
    """
    with mss.mss() as sct:
        if region:
            monitor = region
        else:
            monitor = sct.monitors[1]
        
        screenshot = sct.grab(monitor)
        # 轉換為 numpy 陣列，然後從 BGRA 轉為 BGR
        img = np.array(screenshot)
        return cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

def grab_screen_android():
    """
    擷取Android螢幕畫面 (使用ADB)
    :return: BGR 格式的 numpy 陣列影像
    """
    try:
        # 使用ADB截圖並推送至電腦
        subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screen.png'], check=True, capture_output=True)
        subprocess.run(['adb', 'pull', '/sdcard/screen.png', './temp_screen.png'], check=True, capture_output=True)
        
        # 讀取圖片
        screen = cv2.imread('./temp_screen.png')
        
        # 刪除臨時文件
        if os.path.exists('./temp_screen.png'):
            os.remove('./temp_screen.png')
            
        return screen
    except Exception as e:
        print(f"Android截圖錯誤: {e}")
        return None

def find_center_x(image, lower, upper):
    """
    在影像中尋找指定顏色範圍的中心點 X 座標
    :param image: 來源影像
    :param lower: HSV 顏色下限
    :param upper: HSV 顏色上限
    :return: 中心點 X 座標，若未找到則返回 None
    """
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    
    # 尋找輪廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    if not contours:
        return None
    
    # 取得最大的輪廓 (假設它是目標)
    largest_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(largest_contour)
    
    if M["m00"] == 0:
        return None
        
    center_x = int(M["m10"] / M["m00"])
    return center_x

def get_fishing_positions():
    """
    獲取釣魚相關的 X 座標位置 (綠色條與游標)
    :return: (綠色條 X 座標, 游標 X 座標, 擷取的畫面影像)
    """
    screen = grab_screen(FISHING_REGION)
    
    green_x = find_center_x(screen, LOWER_GREEN, UPPER_GREEN)
    cursor_x = find_center_x(screen, LOWER_CURSOR, UPPER_CURSOR)
    
    return green_x, cursor_x, screen

def check_image(screen, template_path, threshold=0.8):
    """
    在畫面中檢查是否存在範本圖片 (使用灰階比對以減少背景顏色干擾)
    :param screen: 來源畫面
    :param template_path: 範本圖片路徑
    :param threshold: 匹配閾值 (0.0 到 1.0)
    :return: (是否找到, 找到的位置)
    """
    template = cv2.imread(template_path)
    if template is None:
        return False, None
    
    # 轉換為灰階
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    
    res = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    if max_val >= threshold:
        # print(f"DEBUG: 圖片 {template_path} 匹配度: {max_val:.4f}")
        return True, max_loc
    return False, None
