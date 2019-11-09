def heapify(tree,n,i):#寫一顆樹 n代表節點 i代表對該值做heapify
    if i >= n:
        return
    c1 = 2*i+1 #第一個子節點
    c2 = 2*i+2 #第二個子節點
    maximum = i
        
    if c1 < n and tree[c1] > tree[i]: #c1 c2不可出界 故2,3行補return
            maximum = c1
    if c2 < n and tree[c2] > tree[i]:
            maximum = c2
            
    if maximum != i: #如果i為最大值就不必交換
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
