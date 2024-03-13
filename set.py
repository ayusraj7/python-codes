a={1,2,4,6,4,6,2}
print(a)
# print(a[0])

for element in a:
    print(element*2)


l=[]
l.append(5)
l.append('AAA')
l.append([2,3])
print(l)

import random 
print('random number ',random.randrange(1,6))

d={x:x*2 for x in range (1,10)}
print(d);


import networkx
G=networkx.Graph()
G.add_edges_from([(2,1),(2,3),(4,2),(2,5)])
G.remove_node(2)
print(len(G.edges()))