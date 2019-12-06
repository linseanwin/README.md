from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):   
        x = MD5.new()
        x.update(key.encode("utf-8"))
        val = int(x.hexdigest(),16)
        y = val % self.capacity
    
        
        if self.data[y] == None:
            self.data[y] = ListNode(val)
        else:
            
            a = False
            if self.data[y].val != val:
                a = True
            if a:              
                b = self.data[y]
                while b.next != None and b.next.val != val:
                    b = b.next
                if b.next == None:
                    b.next = ListNode(val)
        
    def remove(self, key):
        pass
      
        
    def contains(self, key):
        a = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        b = a % self.capacity
        c = self.data[b]
        
        if c == None:
            return False
        
        else:
            while c:
                if c.val == a:
                    return True
                
                elif c.val != a:
                    c = c.next
            
                    if c == None:
                        return False

#參考資料:

#https://www.youtube.com/watch?v=2BldESGZKB8

#https://github.com/samuel871211/My-python-code/tree/master/HW4

#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html

#https://github.com/C-WeiYu/WeiYu/blob/master/HW4/Hash%20Table%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87Hash%20Table%E8%88%87Hash%20function%E5%8E%9F%E7%90%86.ipynb
