# About Universe663's Python Module

## DatabaseTools

目前僅開發python對MSSQL的相關套件，使用的基礎套件為pyodbc，需要安裝pyodbc才可使用。
相關程式細節如下，版本穩定後應改寫為程式內的註解。

### Mssql

目前僅有簡單的read和exec，更複雜的read data from store procedure這種我還沒解。

以下是指令用法 :

1. config: settings.json的路徑，開發當時因為常常使用排程呼叫Python檔案處理資料，所以使用絕對路徑是相對穩定的方式，不過應該可以再進一步改善。
2. domain: DB連線資訊，預設為'Default'
3. exec: SQL query，尚未完成可以回傳資料的exec方式
4. read: SQL query，回傳 : [{"Key Name": "Key Value"}]

使用範例

```python
from DatabaseTools import Mssql
dbo = Mssql(domain="Default", config=r"settings.json")
dbo.read("select 1")
dbo.exec("insert into table(column) values('value')")
```

## DocParser

DocParser目前使用openpyxl套件處理read/export的作業，Library的未來開發方向將參考我自己的[C#的Library](https://github.com/Alien663/Lib_C-)，若要看使用方法，可以參考Test.py中的Test_DocParser()

1. 使用檔案的副檔名判斷Excel或是CSV檔案，因此要注意檔案的附檔名是否命名正確。
2. Excel為了支援多Sheet的read、write，因此資料格式較CSV的深度多一層。
3. 目前僅處理二維表資料，不考慮合併儲存格的狀況。
4. MyExcel的參數定義如下 :

    >filename: 檔案的路徑，建議輸入絕對路徑以避免錯誤

    >header: 設定欄位，資料從header的下一列開始，預設為第一列

5. 格式差異

> Excel

```json
{
    "Sheet Name" : [
        {"Key 1" : "value 1", "Key 2": "value 2" }
    ]
}
```

> CSV

```json
[
    {"Key 1" : "value 1", "Key 2": "value 2" }
]
```

## PDFExtrator

主要使用PDFMiner處理，一個PDF物件，代表一個PDF檔案
PDFMiner的安裝請參考這裡[here](https://gitlab.wke.csie.ncnu.edu.tw/Alien663/pdfminerinstall)
(PSFMiner目前網址無法使用，等待更新)

## I3SFile

基於研究所實驗室的論文[I3S-用於建構領域相關知識入口之智慧型資訊系統](https://hdl.handle.net/11296/47g5e9)所提出的架構，設計python套件的相關檔案處理，是我將爬蟲結果匯入資料庫以及建立檔案的Library。

### Archive

1. hex2DIR : 將輸入的16進位編碼轉為資料夾路徑

    >root : 為檔案儲存位置的最上層位置

    >hex_str : 16進位整數

    >file_depth : 檔案的深度，目前I3S規則中8個bytes控制(16^8)，此參數保留修改空間，以便應付不同狀況，但限制必須為偶數

    >mkdir : 決定是否要建立檔案，若為True，遇到不存在的路徑時將自動建立資料夾，預設為False以避免手誤建立多於資料夾

2. dir2DEC : 將16進位的檔案路徑轉為10進位的整數

    >file_path : 檔案路徑

    >file_depth : 用法請參照上述hex2DIR中的說明