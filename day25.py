import networkx as nx 
import matplotlib.pyplot as plt 

connections = []
with open('day25_input.txt') as f:
    for row in f.read().split('\n'):
        main, conn = row.split(': ')
        for c in conn.split(' '):
            connections.append([main, c])
    
# save the graph to file to find the connetions to remove
G = nx.Graph() 
G.add_edges_from(connections) 
plt.figure(1, figsize=(200, 80), dpi=60)
nx.draw_networkx(G) 
plt.savefig("day25_graph.png")

# remove connections:  qmr - ptj, xvh - dhn, lxt - lsv
new_connections = [[a,b] for a,b in connections if not (min(a, b) in ('ptj','dhn','lsv') and max(a,b) in ('qmr','xvh','lxt'))]
N = nx.Graph() 
N.add_edges_from(new_connections) 
subgraphs = [N.subgraph(c) for c in nx.connected_components(N)]
for i in range(len(subgraphs)):
    print(f"Subgraph: {i} consists of {len(subgraphs[i].nodes())} nodes")
print('Answer is:', len(subgraphs[0].nodes()) * len(subgraphs[1].nodes()))