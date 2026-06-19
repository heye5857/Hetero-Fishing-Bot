import numpy as np

# 螢幕擷取設定
# 您可能需要根據遊戲解析度和視窗位置調整這些參數
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

# 按鍵綁定
MOVE_LEFT = 'a'      # 向左移動
MOVE_RIGHT = 'd'     # 向右移動
PULL_FISH = 'f'  # 拉魚/互動按鍵 (例如：空白鍵)
