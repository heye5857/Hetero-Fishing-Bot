import numpy as np

# 螢幕擷取設定
# Android版本可能需要調整這些參數以適應不同解析度
FISHING_REGION = {"top": 50, "left": 600, "width": 725, "height": 40}

# HSV 顏色範圍設定
# 綠色條 (目標區域)
LOWER_GREEN = np.array([40, 50, 50])
UPPER_GREEN = np.array([90, 255, 255])

# 黃色游標 (已針對您的需求調整為黃色偵測)
LOWER_CURSOR = np.array([20, 100, 100])
UPPER_CURSOR = np.array([35, 255, 255])

# 控制設定
CENTER_THRESHOLD = 15  # 稍微調小一點增加靈敏度
LOOP_DELAY = 0.001     # 大幅降低延遲，讓控制更即時

# 按鍵綁定 (Android版本)
MOVE_LEFT_ANDROID = 'left'      # 向左移動 (Android keyevent)
MOVE_RIGHT_ANDROID = 'right'    # 向右移動 (Android keyevent)
PULL_FISH_ANDROID = 'enter'  # 拉魚/互動按鍵 (Android keyevent)

# Android設備設定
ADB_PATH = "adb"  # ADB可執行文件路徑，通常系統已設定