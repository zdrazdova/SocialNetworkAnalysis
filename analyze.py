import networkx as nx
import matplotlib.pyplot as plt


G=nx.read_pajek("USAir97.net")

G1=nx.Graph(G)

print("US Air 97 Network has {0} nodes and {1} edges.".format(len(G.nodes),len(G.edges)))



sorted_d = sorted([(value, key) for (key,value) in G1.degree], reverse=True)

print("Top ten airports with most flights: ",sorted_d[:10])
print(G.nodes['San Francisco Intl'])
print(G.edges['Minot Intl', 'Stapleton Intl',0])

Gselection = G

remove = sorted_d[10:]
nodes_to_remove = []
for r in range(len(remove)):
    node = remove[r][1]
    nodes_to_remove.append(node)
    Gselection.remove_node(node)

pos = nx.circular_layout(Gselection)

nx.draw_networkx(Gselection, pos, with_labels=True, node_size=100, edge_color="#ff000000")

for (u, v, d) in Gselection.edges(data=True):
    w =  d['weight']
    edge = [(u,v,d)]
    nx.draw_networkx_edges(Gselection, pos, edgelist=edge, equidistant=True, alpha=0.5, width=w*10)





plt.show()
