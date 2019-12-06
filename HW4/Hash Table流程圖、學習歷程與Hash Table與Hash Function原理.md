# 學習歷程:

![](https://www.leeholmes.com/blog/wp-content/uploads/2019/07/image.png)

聽到老師說，這次的hash table比上次的bst容易多了，可能是上次我沒有想出delete和modify的緣故。

是後來參考同學的程式碼以及詳細的解釋才讓我較為明白，平白想出程式碼真的不容易。

而光install 資料都研究了不少時間，原來cmd開了就成功了啊。

remove的部分想不太出來，只好先pass了，之後再對照高手的程式碼參考。

即便無法想出原創，但盡可能了解原理跟程式碼在做什麼事情。



# Hash Table原理：

hash table中文稱雜湊表，是根據key存在儲存位置的資料結構，將文件經由hash function加密後可以依照清楚的排序更容易找到儲存後的資料。如輸入字元後運用capacity的餘數，若該資料餘數為2則會在linked list編號2那條找到，若該編號同時有許多筆資料則繼續從該編號後尋找即可，可節省不少時間。

# Hash Function原理：

hash function中文稱雜湊函式，是將數字或字串輸入後輸出雜湊值，很有可能只是一個字母或些許符號改變，輸出的值就有非常大的不同，如演算法圖鑑舉例就像是以個果汁機打碎後，打碎的果汁同理無法回到原有的樣子，也就是不可逆的。而本次作業適用MD5加密，轉進位制。

# 流程圖：

![](https://github.com/linseanwin/learning-note/blob/master/images/S__59498511.jpg)

# 參考資料：

https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash

https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8

http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html

