<div align="left">

[![GitHub views](https://views.whatilearened.today/views/github/Junwu0615/How-To-Use-Clone-Shields.svg)](https://github.com/Junwu0615/How-To-Use-Clone-Shields)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/aae1fe99b8a54ec42c617f4d973016ba/raw/How-To-Use-Clone-Shields_clone.json&logo=github)](https://github.com/Junwu0615/How-To-Use-Clone-Shields)

</div>
    
## How To Use Clone Shields.io
想在頁面呈現有 Clone 的圖標，是無法單純的像是使用 views ，這種只須改個使用者變數的動態圖標。 <a href='https://github.com/Junwu0615/How-To-Use-Clone-Shields'><img alt='GitHub Views' src='https://views.whatilearened.today/views/github/Junwu0615/How-To-Use-Clone-Shields.svg'> </a> </br>
那麼怎麼實現呢 ? 首先需要用 Git Actions 此功能來操作，運行過程會用到 [Git Gist](https://gist.github.com/) 來做存儲，而產生出來的 json 格式，就可以透過 [Shields.io](https://shields.io/) 來呼叫。本次分享主要是參考 [MShawon](https://github.com/MShawon) 大神的文章，以中文的方式再分享一次。
具體操作請參考下列步驟。

## 更新 CLONE 紀錄方法
原先在 `clone.py` 中有大神寫的紀錄方式，但我做了些微調，由於 GitHub 只會紀錄最鄰近 2 周的紀錄，其餘的都會被洗掉。
因此我將 json 檔只保留 2 周內容，其餘數據要被清洗掉前，先做計數器的累加計算，如此一來可以省下 json 儲存空間。
具體分別在字典中擴充了下列 Key 值 :
- `count_past_to_last_2_weeks_ago` : 過去至近 2 周前的所有累算加總 - 不限於獨特用戶之克隆。
- `uniques_past_to_last_2_weeks_ago` : 過去至近 2 周前的所有累算加總 - 獨特用戶之克隆。
- `count_total` : 過去至今日所有不限於獨特用戶之克隆加總，其也視作為 Clone 圖標的取值來源。
- `uniques_total` : 過去至今日所有獨特用戶之克隆加總。

## STEP.1　需要創立2個檔案
參考本專案放置檔案之路徑，以及內容 (複製程式碼)，依此建立。
- `/clone.py`
- `/.github/workflows/clone.yml`

## STEP.2　修改2個檔案內容
程式碼大神已都寫好，只需變更 `使用者名稱 / 專案名稱 / 分支名稱` !

### I.　clone.py
**搜尋並取代關鍵字** [ `xxx` 為你的專案名稱 ]
- How-To-Use-Clone-Shields_clone.json -> `xxx`_clone.json
- How-To-Use-Clone-Shields_clone_before.json -> `xxx`_clone_before.json
- How-To-Use-Clone-Shields_clone.json -> `xxx`_clone.json
```python
import json

with open('How-To-Use-Clone-Shields_clone.json', 'r') as fh:
    now = json.load(fh)

with open('How-To-Use-Clone-Shields_clone_before.json', 'r') as fh:
    before = json.load(fh)

with open('How-To-Use-Clone-Shields_clone.json', 'w', encoding='utf-8') as fh:
    json.dump(latest, fh, ensure_ascii=False, indent=4)
```
### II.　clone.yml
修改為你專案主要的分支，main -> 將內容替換成你的 [ `分支名稱` ]
```python
  # run on every push on the master branch
  push:
    branches:
    - main
```
**搜尋並取代關鍵字** [ 將內容替換成你的 `使用者名稱 / 專案名稱 / 分支名稱` ] </br>
- How-To-Use-Clone-Shields_clone.json -> `xxx`_clone.json [ `xxx` 為你的專案名稱 ] </br>
- How-To-Use-Clone-Shields_clone_before.json -> `xxx`_clone_before.json [ `xxx` 為你的專案名稱 ] </br>
- https://raw.githubusercontent.com/Junwu0615/How-To-Use-Clone-Shields/main/clone.py (選出重點部分即可) </br> 
-> Junwu0615/How-To-Use-Clone-Shields/main -> 將內容替換成你的 [ `使用者名稱 / 專案名稱 / 分支名稱` ]

## STEP.3　取得 Clone 權限之 Token 以及開啟工作流之讀寫權限

### I.　取得 Clone 權限之 Token
- 權限路徑 : 右上角 (upper right corner) -> 設定 (settings) -> 開發者設定 (Developer Settings) -> 個人訪問令牌（經典）(Personal access tokens (classic)) -> 建立 (create) 。
- 名稱設置為 `SECRET_TOKEN` 。
- 天數可以設置不限天數 。
- 權限設置依照下方二圖所設定 。 </br>
  - <img width='550' height='500' src="https://github.com/Junwu0615/How-To-Use-Clone-Shields/blob/main/sample_img/token_00.jpg"/> 
  - <img width='550' height='100' src="https://github.com/Junwu0615/How-To-Use-Clone-Shields/blob/main/sample_img/token_01.jpg"/>
- 完成後即儲存，會得到一個 `Token 密鑰` 將之複製起來，至你的專案設定頁面貼上去。
    - 專案設定頁面路徑 : 選擇你的專案中的設定 -> 秘密和變數 (Secrets and variables)
    - 密鑰名稱設置為 `SECRET_TOKEN` 。
    - 將方才取得的 Token 貼上去。
    - <img width='750' height='450' src="https://github.com/Junwu0615/How-To-Use-Clone-Shields/blob/main/sample_img/token_02.jpg"/> 
    - 完成後即儲存。
    
### II.　開啟工作流之讀寫權限
- 設定路徑如下二圖所示。
  - <img width='750' height='400' src="https://github.com/Junwu0615/How-To-Use-Clone-Shields/blob/main/sample_img/token_03.jpg"/> 
  - <img width='500' height='200' src="https://github.com/Junwu0615/How-To-Use-Clone-Shields/blob/main/sample_img/token_04.jpg"/> 
- 選擇完即儲存。

## STEP.4　README.md 設置圖標
如此一來前置作業都已完成 (STEP.1-3)。接下來先讓專案在後台進行運作，等待幾秒鐘後，即可在專案目錄生成一個 CLONE.md 的檔案 。 檔案裏頭有已建好的圖標路徑，就可在 README.md 中直接使用。如下所示。[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count_total&url=https://gist.githubusercontent.com/Junwu0615/aae1fe99b8a54ec42c617f4d973016ba/raw/How-To-Use-Clone-Shields_clone.json&logo=github)](https://github.com/Junwu0615/How-To-Use-Clone-Shields) </br>
#### 另外要確認是否已在 [Git Gist](https://gist.github.com/) 生成 json 檔 (取得 clone 數據)，可以進去 [ https://gist.github.com/使用者名稱/ ] 查看。

## 參考來源
- [MShawon | github-clone-count-badge](https://github.com/MShawon/github-clone-count-badge)
