from collections import defaultdict 

import math

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    def Dijkstra(self, s): 
        a = [False] * self.V 
        b = [True] * self.V
        c = [float('inf')] * self.V
        
        
        c[s] = 0
        
        while a != b:
            for i in range(self.V):
                if g.graph[i][s] != 0 and c[s] + g.graph[i][s] < c[i]:
                    c[i] = c[s] + g.graph[i][s]
                           
            d = float('inf')
            e = 0
            for e in range(self.V):
                if a[e] == False and c[e] < d :
                    d = c[e]
                    s = e         
            a[s] = True
            
            f = {} 
            if a == b:
                for i in range(self.V):
                    f[str(i)] = c[i]
                return f
        return 
    

    def Kruskal(self):
        a = [column for column in range(self.V)]
        b = {}
        c = sorted(self.dict)
       
        for i in c:
            j = 0
            s = 0
            for j , s in self.dict[i]:
                if a[j] !=a [s]:
                    a = [a[j] if q == a[s] else q for q in a]
                    b[str(j)+'-'+str(s)]=i
                else:
                    pass
        
        return b   
       
    
#http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html

#https://medium.com/cantors-paradise/dijkstras-shortest-path-algorithm-in-python-d955744c7064
