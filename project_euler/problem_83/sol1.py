# https://projecteuler.net/problem=83
from collections import defaultdict
class graph:
    def __init__(self):
        self.nodes=set()
        self.edges=defaultdict(list)

    def add_node(self,value):
        self.nodes.add(value)

    def add_edge(self,from_node, to_node ):
        self.edges[from_node].append(to_node)



def dijkstra(initial,graph):
    visited=[]
    valid=[initial]
    i=0
    path={initial:initial}
    while len(valid)>0:
        i+=1
        current = min(valid,key=lambda x: path[x])
        visited.append(current)
        valid.remove(current)
        for node in graph.edges[current]:
            if node not in valid and node not in visited:
                valid.append(node)
            else:
                pass
            if node not in path:
                path[node]=path[current]+node
            else:
                if path[node]>(path[current]+node):
                    path[node]=path[current]+node
    return path




matrix=[]
fi=open('input.txt','r')
for line in fi:
    line=line.split(',')                          #Matrix1 is used to calculate
    line=list(map(int, line))                     #d{} which counts repeated node's frequency
    matrix.append(line)
fi.close()

d={}
for _ in range(80):
    for node in range(80):
        jup=0
        for k in matrix:
            l=k.count(matrix[_][node])
            jup+=l
        if jup > 1:
            d[matrix[_][node]]=jup

matrix2=[]
f2=open('input.txt','r')
for lin in f2:
    lin=lin.split(',')
    lin=list(map(int,lin))                        #Matrix2 gets rid of repeated nodes
    for p in range(len(lin)):
        if lin[p] in d:
            d[lin[p]]-=1
            lin[p]=lin[p]+ ((d[lin[p]]+1)/10000)
    matrix2.append(lin)

G=graph()


#. Adding edges of of non boundry nodes os matrix2
for _ in range(1,len(matrix2)-1):
    for node in range(1,len(matrix2[_])-1):
        G.add_node(matrix2[_][node])
        G.add_edge(matrix2[_][node],matrix2[_][node+1])
        G.add_edge(matrix2[_][node],matrix2[_][node-1])
        G.add_edge(matrix2[_][node],matrix2[_+1][node])
        G.add_edge(matrix2[_][node],matrix2[_-1][node])

for node in range(1,len(matrix2)-1):
    G.add_node(matrix2[0][node])
    G.add_edge(matrix2[0][node],matrix2[0][node-1])
    G.add_edge(matrix2[0][node],matrix2[0][node+1]) #Adding edges to first row 
    G.add_edge(matrix2[0][node],matrix2[1][node])

for node in range(1,len(matrix2)-1):
    G.add_node(matrix2[node][0])
    G.add_edge(matrix2[node][0],matrix2[node-1][0])
    G.add_edge(matrix2[node][0],matrix2[node+1][0]) #Adding edges to first column
    G.add_edge(matrix2[node][0],matrix2[node][1])

for node in range(1,len(matrix2)-1):
    G.add_node(matrix2[79][node])
    G.add_edge(matrix2[79][node],matrix2[79][node-1])
    G.add_edge(matrix2[79][node],matrix2[79][node+1]) #Adding edges to last row
    G.add_edge(matrix2[79][node],matrix2[78][node])

for node in range(1,len(matrix2)-1):
    G.add_node(matrix2[node][79])
    G.add_edge(matrix2[node][79],matrix2[node-1][79])
    G.add_edge(matrix2[node][79],matrix2[node+1][79]) #Adding edges to last column
    G.add_edge(matrix2[node][79],matrix2[node][78])

#Adding edges to corner nodes
G.add_node(matrix2[0][0])
G.add_edge(matrix2[0][0],matrix2[0][1])
G.add_edge(matrix2[0][0],matrix2[1][0])

G.add_node(matrix2[79][0])
G.add_edge(matrix2[79][0],matrix2[79][1])
G.add_edge(matrix2[79][0],matrix2[78][0])

G.add_node(matrix2[79][79])
G.add_edge(matrix2[79][79],matrix2[79][78])
G.add_edge(matrix2[79][79],matrix2[78][79])

G.add_node(matrix2[0][79])
G.add_edge(matrix2[0][79],matrix2[0][78])
G.add_edge(matrix2[0][79],matrix2[1][79])


a=dijkstra(matrix2[0][0],G)
print(int(a[matrix2[-1][-1]]))

