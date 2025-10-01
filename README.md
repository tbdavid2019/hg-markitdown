---
title: "Hg Markitdown"
emoji: 📝
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.25.0
app_file: app.py
pinned: false
--- Markitdown
emoji: �
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 5.25.0
app_file: app.py
pinned: false
---

# MarkItDown 檔案轉 Markdown 工具

這個專案提供一個基於 Gradio 的網頁介面，支援拖放或選取檔案（PDF、Word、Excel、PowerPoint、圖片、音訊等）並自動轉換為 Markdown 內容，方便快速複製使用。

## 功能特色

- 支援拖曳或選擇檔案即時轉換
- 轉換結果以 Markdown 元件呈現，支援語法高亮
- 內建複製按鈕，可一鍵複製轉換後內容
- 可手動按「開始轉換」重新觸發、更新結果

## 執行方式

```bash
pip install -r requirements.txt
python app.py
```

執行後於終端機顯示的網址（預設 http://127.0.0.1:7860/）即可打開網頁並進行檔案上傳轉換。

## 注意事項

- 請確認已安裝 `markitdown[all]` 所需的系統依賴與 NLP 模型。
- 若遇到特定檔案格式無法解析，請檢查檔案是否完整、未加密，或參考 MarkItDown 官方文件取得額外支援。
