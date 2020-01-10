# hash table

![](http://www.algolist.net/img/hash-table-chaining.png)

雜湊表（Hash table），是根據鍵（Key）而直接查詢在內存存儲位置的資料結構。也就是說，它通過計算一個關於鍵值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄，這加快了查找速度，映射函數稱做雜湊函數，存放記錄的數組稱做雜湊表。

# Hash Table原理：

hash table中文稱雜湊表，是根據key存在儲存位置的資料結構，將文件經由hash function加密後可以依照清楚的排序更容易找到儲存後的資料。如輸入字元後運用capacity的餘數，若該資料餘數為2則會在linked list編號2那條找到，若該編號同時有許多筆資料則繼續從該編號後尋找即可，可節省不少時間。

# Hash Function原理：

hash function中文稱雜湊函式，是將數字或字串輸入後輸出雜湊值，很有可能只是一個字母或些許符號改變，輸出的值就有非常大的不同，如演算法圖鑑舉例就像是以個果汁機打碎後，打碎的果汁同理無法回到原有的樣子，也就是不可逆的。而本次作業適用MD5加密，轉進位制。

# 參考資料

http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
