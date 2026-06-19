# 釣魚機器人 Android 版本

這是一個適用於Android設備的釣魚機器人自動化程式。該程式可以自動控制遊戲中的釣魚過程，包括開始釣魚、檢測魚兒上鉤以及進行QTE快速反應事件。

## 功能特性

- 自動檢測並點擊"開始釣魚"按鈕
- 檢測魚兒上鉤信號
- QTE快速反應事件自動控制
- 魚餌不足檢測和提示
- 支援多種遊戲狀態識別

## 環境要求

1. **Python 3.6+**
2. **Android設備** (需要開啟USB調試模式)
3. **ADB工具** (Android Debug Bridge)
4. **已安裝的Python庫**:
   - opencv-python
   - numpy
   - pydirectinput (用於Windows，Android版本會自動適配)

## 安裝步驟

### 1. 克隆或下載項目文件
```bash
git clone [項目地址]
cd HeteroFishingBot
```

### 2. 安裝Python依賴
```bash
pip install -r requirements.txt
```

### 3. 配置Android設備
- 在Android設備上開啟開發者選項和USB調試
- 使用USB線連接電腦和Android設備
- 確保ADB工具可以識別設備

## 運行方法

### 方法一：使用Python運行
```bash
python android_main.py
```

### 方法二：直接運行（如果已設定可執行權限）
```bash
chmod +x android_main.py
./android_main.py
```

## 使用說明

1. 啟動遊戲並進入釣魚介面
2. 運行機器人程式
3. 程式會自動檢測遊戲狀態並進行操作
4. 按 `Ctrl+C` 停止程式

## 設定檔說明

### android_config.py
- 調整了適合Android設備的螢幕截圖區域
- 修改了顏色識別閾值以適應不同遊戲環境
- 降低了循環延遲以提高回應速度

### 圖片模板
程式需要以下圖片模板文件在 `images/` 目錄中：
- `start_fishing.png` - 開始釣魚按鈕
- `fish_bite.png` - 魚兒上鉤提示
- `out_of_bait.png` - 魚餌不足提示
- `success.png` - 成功提示

## 注意事項

1. 確保Android設備的USB調試已開啟
2. 確保ADB工具在系統PATH中可用
3. 根據遊戲實際介面調整圖片模板和顏色識別參數
4. 部分遊戲可能需要特定權限設定

## 故障排除

### 常見問題
1. **"Android截圖錯誤"** - 檢查ADB是否正確連接設備
2. **無法檢測到圖片** - 調整圖片模板或閾值參數
3. **控制不靈敏** - 調整LOOP_DELAY參數

## 技術細節

### 螢幕截圖
使用ADB命令 `screencap` 截取Android螢幕並傳輸到電腦進行處理。

### 輸入控制
使用ADB命令模擬按鍵操作：
- `input keyevent 21` - 左鍵
- `input keyevent 22` - 右鍵  
- `input keyevent 66` - 確認/互動鍵
- `input tap x y` - 點擊指定座標

## 版本資訊

- 當前版本: 1.0 (Android適配版)
- 支援平台: Android 5.0+
- Python版本: 3.6+

## 許可證

[在此處添加許可證資訊]
