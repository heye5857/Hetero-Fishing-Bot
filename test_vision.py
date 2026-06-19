import cv2
import time
from vision import get_fishing_positions
from config import LOWER_GREEN, UPPER_GREEN, LOWER_CURSOR, UPPER_CURSOR

def test_vision():
    """
    測試視覺辨識。
    顯示擷取的畫面，並標註偵測到的綠色條與游標位置。
    按下 'q' 鍵可退出。
    """
    print("正在測試視覺辨識。按下 'q' 可退出。")
    
    while True:
        green_x, cursor_x, screen = get_fishing_positions()
        
        # 繪製除錯資訊
        if green_x:
            # 綠色線代表綠色區域中心
            cv2.line(screen, (green_x, 0), (green_x, screen.shape[0]), (0, 255, 0), 2)
        if cursor_x:
            # 紅色線代表游標位置
            cv2.line(screen, (cursor_x, 0), (cursor_x, screen.shape[0]), (0, 0, 255), 2)
            
        cv2.imshow("視覺測試 (Vision Test)", screen)
        
        print(f"綠色區域 X: {green_x}, 游標 X: {cursor_x}")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cv2.destroyAllWindows()

if __name__ == "__main__":
    test_vision()
