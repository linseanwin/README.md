## insert 新增:

將一個新的值插入樹中 可能會有幾種情況

若是此樹為空值則直接插入當成root

若是此樹有值和root比較後，小於者往左，大於者往右

直到最後一個數字出現無法往下比後新增至最後該位置

## search 搜尋:

丟一個值進入此樹查詢

一樣合此樹的root比較大小，若等於root則直接回傳此數

大於root則往右找，反之小於則往左找

當有找到時回傳此數，若比較到最後1數仍然沒有此數則回傳none

## modify 修改:

先找到此數要修改的值，在藉由比較大小往下往下插入新的值

找到該數值後insert即將修改的值，再將原本的值刪除

若是修改該數字會破壞此樹的結構，那麼得先往下新增

新增後再藉由平衡修改後再將原本的數值刪除

## delete 刪除:

刪除的複雜難度取決於有無子節點

越多子節點需要更多程式碼將此數刪除

### 參考資料:

http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html

http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html
