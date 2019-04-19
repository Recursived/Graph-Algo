import pprint
import sys

class Tas:
  
    def __init__(self): 
        self.arr = [] 
        self.size = 0
        self.pos = [] 
  
    def newNode(self, v, poids): 
        minHeapNode = [v, poids] 
        return minHeapNode 
  
    def swapNode(self,a, b): 
        t = self.arr[a] 
        self.arr[a] = self.arr[b] 
        self.arr[b] = t 
  
    def minHeapify(self, val): 
        smallest = val 
        left = 2*val + 1
        right = 2*val + 2
  
        if left < self.size and self.arr[left][1] < self.arr[smallest][1]:
            smallest = left 
  
        if right < self.size and self.arr[right][1] < self.arr[smallest][1]:
            smallest = right 
  
        if smallest != val: 
  
            self.pos[ self.arr[smallest][0] ] = val 
            self.pos[ self.arr[val][0] ] = smallest 
  
            self.swapNode(smallest, val) 
  
            self.minHeapify(smallest) 
  
    def extractMin(self): 
  
        if self.isEmpty() == True: 
            return

        root = self.arr[0] 

        last = self.arr[self.size - 1] 
        self.arr[0] = last 

        self.pos[last[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, poids): 
  
        i = self.pos[v] 
  
        self.arr[i][1] = poids 

        while i > 0 and self.arr[i][1] < self.arr[(i - 1) // 2][1]:
   
            self.pos[ self.arr[i][0] ] = (i-1)//2
            self.pos[ self.arr[(i-1)//2][0] ] = i 
            self.swapNode(i, (i - 1)//2 ) 
  
 
            i = (i - 1) // 2; 
  
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  


def create_graph(sommets, arcs):
    graphe = dict((s, list()) for s in sommets)
    for pred, succ, etiq in arcs:
        graphe[pred].append((succ, etiq))

    print("Affichage du graphe : ")
    pprint.pprint(graphe)
    return graphe

def dijkstra(graphe, source):
    sommets = set(graphe.keys())
    poids = []

    tas = Tas()

    for v in sommets:
        poids.append(sys.maxsize)
        tas.arr.append( tas.newNode(v, poids[v]) )
        tas.pos.append(v)

    tas.pos[source] = source
    poids[source] = 0
    tas.decreaseKey(source, poids[source])

    tas.size = len(sommets)

    while tas.isEmpty() == False:

        nhn = tas.extractMin()
        u = nhn[0]

        for somval in graphe[u]:

            v = somval[0]

            if tas.isInMinHeap(v) and poids[u] != sys.maxsize and  somval[1] + poids[u] < poids[v]:
                    poids[v] = somval[1] + poids[u]

                    # update poidsance value
                    # in min heap also
                    tas.decreaseKey(v, poids[v])
    return poids, tas

if __name__ == "__main__":
    sommets = list(range(6))
    arcs = [
        (0, 4, 4),
        (1, 0, 4),
        (2, 1, 2),
        (2, 5, 3),
        (3, 2, 9),
        (3, 4, 2),
        (3, 5, 6),
        (4, 1, 9),
        (4, 3, 2),
        (4, 5, 3),
        (5, 1, 6),
        (5, 2, 3),
        (5, 3, 6)
        ]

    graphe = create_graph(sommets, arcs)
    d, heap = dijkstra(graphe, 3)
    print("Liste des poids: ", d)
    print("Liste des prédécesseur: ", heap.arr, heap.pos)
