from collections import defaultdict 

class Graph:
    
    def __init__(self):    
        self.graph = defaultdict(list) 
            
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  

    def BFS(self, s): 
        a = [] 
        b = [s]   
        a.append(s) 
        while len(b) != 0:
            
            u = b.pop(0) 
            
            n = 0
            
            for n in self.graph[u]: 
                if n not in a: 
                    a.append(n) 
                    b.append(n)    
        return a
    
    def DFS(self, s):
        a = [] 
        b = [s]  
        while len(b) != 0: 
            u = b.pop(-1) 
            if u not in a: 
                a.append(u)
                
            c = 0    
            
            for c in self.graph[u]: 
                if c not in a: 
                    if c not in b:
                        b.append(c)
                    
        return a
    
#參考資料:

#https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html

#https://github.com/C-WeiYu/WeiYu/blob/master/HW5/BFS%E8%88%87DFS%E6%B5%81%E7%A8%8B%E5%9C%96%E3%80%81%E7%A8%8B%E5%BC%8F%E7%A2%BC%E5%AD%B8%E7%BF%92%E6%AD%B7%E7%A8%8B%E8%88%87BFS%E8%88%87DFS%E5%8E%9F%E7%90%86%E8%88%87%E6%AF%94%E8%BC%83.ipynb

#https://en.wikipedia.org/wiki/Breadth-first_search
    
  
