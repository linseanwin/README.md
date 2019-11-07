def heapify(tree,n,i):
    if i >= n:
        return
    c1 = 2*i+1
    c2 = 2*i+2
    maximum = i
        
    if c1 < n and tree[c1] > tree[i]:
            maximum = c1
    if c2 < n and tree[c2] > tree[i]:
            maximum = c2
            
    if maximum != i: 
        tree[i],tree[maximum] = tree[maximum],tree[i]
            
        heapify(tree,n,maximum)

def build_heap(tree,n):
    last_node = n - 1
    parent = (last_node - 1)//2
    for i in range(parent):
        heapify(tree,n,i)
        
def heap_sort(tree,n):
    build_heap(tree,n)
    i = int
    for i in range(n-1,0,-1) :
        tree[0],tree[i] = tree[i],tree[0]
        heapify(tree,i,0)
        
       
tree = [ 10,4, 1, 2, 3,6] 
n = 6
heap_sort(tree,n)
i = int
for i in range(n):
    print (tree[i])    
        
    
