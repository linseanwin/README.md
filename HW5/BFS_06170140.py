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
