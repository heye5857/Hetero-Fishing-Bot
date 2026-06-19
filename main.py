import time
import cv2
from vision import get_fishing_positions, check_image, grab_screen
from actions import press_left, press_right, stop_moving, interact, click_at
from states import BotState
from config import CENTER_THRESHOLD, LOOP_DELAY

def main():
    state = BotState.IDLE
    print("機器人已啟動。按下 Ctrl+C 可停止。")
    
    try:
        while True:
            # 只有在非 QTE 狀態下才擷取全螢幕
            if state != BotState.QTE:
                screen = grab_screen()
                
                # 偵測是否魚餌不足
                if state != BotState.OUT_OF_BAIT:
                    bait_empty, _ = check_image(screen, "images/out_of_bait.png", threshold=0.85)
                    if bait_empty:
                        print("\n警告：偵測到魚餌不足！切換至等待補充狀態。")
                        stop_moving()
                        state = BotState.OUT_OF_BAIT

            if state == BotState.IDLE:
                # 偵測並點擊「開始釣魚」
                start_detected, start_loc = check_image(screen, "images/start_fishing.png", threshold=0.7)
                if start_detected:
                    print("\n偵測到開始按鈕，正在點擊...")
                    interact() 
                    time.sleep(2) # 等待過場動畫
                    state = BotState.WAITING_FOR_BITE
                else:
                    print("狀態：閒置 - 等待開始按鈕...          ", end='\r')
                    time.sleep(0.5)

            elif state == BotState.WAITING_FOR_BITE:
                # 偵測魚兒上鉤圖示
                bite_detected, _ = check_image(screen, "images/fish_bite.png", threshold=0.8)
                if bite_detected:
                    print("\n偵測到魚兒上鉤！進入 QTE 階段。")
                    interact() 
                    time.sleep(0.6) # 等待 QTE 進度條出現
                    state = BotState.QTE
                else:
                    print("狀態：正在等魚上鉤...                ", end='\r')

            elif state == BotState.QTE:
                # 高效能擷取小區域
                green_x, cursor_x, mini_screen = get_fishing_positions()
                
                if green_x is not None and cursor_x is not None:
                    # QTE 控制邏輯
                    error = green_x - cursor_x
                    if error > CENTER_THRESHOLD:
                        press_right()
                    elif error < -CENTER_THRESHOLD:
                        press_left()
                    else:
                        stop_moving()
                else:
                    # 如果沒看到進度條，先停止移動，並確認是否真的結束
                    stop_moving()
                    full_screen = grab_screen()
                    
                    # 1. 檢查是否成功 (調低門檻至 0.7 增加相容性)
                    success_detected, success_loc = check_image(full_screen, "images/success.png", threshold=0.8)
                    if success_detected:
                        print("\n偵測到成功畫面！點擊關閉視窗。")
                        if success_loc:
                            time.sleep(0.5) # 等待畫面穩定
                            click_at(success_loc[0] + 50, success_loc[1] + 20)
                        time.sleep(1.5)
                        state = BotState.IDLE
                    else:
                        # 2. 檢查是否失敗重回開始畫面
                        start_detected, _ = check_image(full_screen, "images/start_fishing.png", threshold=0.7)
                        if start_detected:
                            print("\n偵測到開始按鈕 (失敗或跳過)，重置狀態。")
                            state = BotState.IDLE
                        else:
                            # 什麼都沒偵測到，可能還在動畫中，等待一下
                            print("狀態：QTE 結束，正在搜尋結算畫面...   ", end='\r')
                            time.sleep(0.2)
                
                time.sleep(LOOP_DELAY)
            
            elif state == BotState.OUT_OF_BAIT:
                bait_empty, _ = check_image(screen, "images/out_of_bait.png", threshold=0.85)
                if not bait_empty:
                    print("\n魚餌已補充，恢復運作...")
                    state = BotState.IDLE
                else:
                    print("狀態：魚餌不足 - 等待手動補充中...    ", end='\r')
                    time.sleep(2)
            
            if state != BotState.QTE:
                time.sleep(0.1)
                
    except KeyboardInterrupt:
        print("\n機器人已被使用者停止。")
        stop_moving()

if __name__ == "__main__":
    main()
