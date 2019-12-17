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
    

#nx.draw_circular(Gselection,pos=nx.spring_layout(Gselection))
weights_array = []
for edge in Gselection.edges:
    weight = Gselection.edges[edge]
    weights_array.append(weight['weight']*100)

print(weights_array)
print(type(Gselection))
print(type(G))
print(type(G1))

print(Gselection.edges)

e2 = [(u, v, d) for (u, v, d) in Gselection.edges(data=True) if d['weight'] > 0.1 and d['weight'] < 0.2]
e3 = [(u, v, d) for (u, v, d) in Gselection.edges(data=True) if d['weight'] <= 0.1 and d['weight'] > 0.05]
e1 = [(u, v, d) for (u, v, d) in Gselection.edges(data=True) if d['weight'] > 0.2]
e4 = [(u, v, d) for (u, v, d) in Gselection.edges(data=True) if d['weight'] <= 0.05]

pos = nx.circular_layout(Gselection)

nx.draw_networkx_nodes(Gselection, pos, node_size=100, with_labels=True)


nx.draw_networkx_edges(Gselection, pos, edgelist=e1, equidistant=True, alpha=0.5, width=3.6)
nx.draw_networkx_edges(Gselection, pos, edgelist=e2, equidistant=True, alpha=0.5, width=3)
nx.draw_networkx_edges(Gselection, pos, edgelist=e3, equidistant=True, alpha=0.5, width=2.4)
nx.draw_networkx_edges(Gselection, pos, edgelist=e4, equidistant=True, alpha=0.5, width=1.8)

print(e1)



plt.show()
