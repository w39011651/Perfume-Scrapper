# Perfume scrapper
## 動機
為了詢問AI香水推薦，於是我想要將所有調性複製並輸入給AI，但一個一個香水慢慢複製太花時間，於是決定製作這個爬蟲來完成這件事
## 功用
這是一個香水爬蟲，會將網站上香水的調性抓取並整理成一個CSV檔案，這個爬蟲採用了異步請求，能夠節省時間
## 香水品牌
目前我是以[FINCA](https://www.fincataiwan.com/categories/%E9%A6%99%E6%B0%B4?limit=72)香水作為目標網站
## 文件結構
```
|
|-.gitignore
|-README.md
|-LICENSE
|-notes_parser.py #主程式在此執行
|-perfume_parser.py #整理每個香水的頁面網址，並且獲取每個香水的調性
|-utils.py #logs等功能函數定義模組
|-save_csv.py #儲存至csv檔案模組
|-perfumes.csv #獲取結果
```
## 如何執行
在專案資料夾中執行 `notes_parser.py` 或者開啟終端執行 `python notes_parser.py`

## 待修復或新增功能
+ csv格式，有縮排、空格等問題
+ 可以直接使用API串聯LLM詢問問題，節省將csv檔案拖至LLM步驟

## requirements
+ bs4
+ asyncio
+ asynchttp
+ csv
+ requests
+ json