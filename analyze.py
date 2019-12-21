import networkx as nx
import matplotlib.pyplot as plt
import copy as cp
import numpy as np


def compute_centrality(name, computed, top):
    file.write("\n")
    file.write("# Centralities \n")  
    file.write("\n")
    file.write("### " + name + " centrality: \n") 
    
    centrality = np.empty((10))
    for i in range(10):
        centrality[i] = computed[top[i]]
    top_index = np.argmax(centrality)
    for i in range(10):
        if i != top_index:
            file.write("* " + str(top[i]) + ": " + str(centrality[i]) + "\n\n")
        else:
            file.write("* **" + str(top[i]) + ": " + str(centrality[i]) + "**\n\n")

G=nx.read_pajek("USAir97.net")

G1=nx.Graph(G)

with open("slides.md", "w") as file:
    file.write("% Analysis of USAir97 network \n")
    file.write("% Zuzana Drázdová & Zuzana Šimečková \n")
    file.write("% January 7 2020 \n")
    file.write("# General information \n")
    file.write("US Air 97 Network has **{0}** nodes and **{1}** edges.\n\n".format(len(G.nodes),len(G.edges)))
    file.write("Nodes represent Airports in the United States and edges represent routes between these airtports.\n\n")
    file.write("Each edge has weights with indicated how many flights are on given route.\n\n")



    sorted_d = sorted([(value, key) for (key,value) in G1.degree], reverse=True)

    file.write("\n\n")
    file.write("# Top US airports \n")
    
    file.write("**Top ten airports with flights to/from most other airports:** \n\n")
    for i in range(10):
        file.write("* " + str(sorted_d[i][1]) + "\n\n")
    Gselection = cp.deepcopy(G)
    


    remove = sorted_d[10:]
    nodes_to_remove = []
    for r in range(len(remove)):
        node = remove[r][1]
        nodes_to_remove.append(node)
        Gselection.remove_node(node)


    plt.figure(figsize=(8,3.4))
    
    positions = {}
    for node in Gselection.nodes:
        data = Gselection.nodes[node]
        posi = (data['x'],-data['y'])
        positions.setdefault(node, posi)
    
    nx.draw_networkx(Gselection, pos=positions, with_labels=True, node_size=100, edge_color="#ff000000")
    
    for (u, v, d) in Gselection.edges(data=True):
        w =  d['weight']
        edge = [(u,v,d)]
        nx.draw_networkx_edges(Gselection, pos=positions, edgelist=edge, equidistant=True, alpha=0.5, width=w*10)
    
    plt.savefig('most_other_airports.svg')
    file.write("\n")
    file.write("# Top US airports \n")
    file.write("![Airports with flights to/from most other airports - map](top.png)")
    
    
    power_dict = {}

    for node in G.nodes:
        value = 0
        for edge in G.edges(data=True):
            (u,v,d) = edge
            w = d['weight']
            if node == edge[0] or node == edge[1]:
                value += w
        power_dict.setdefault(value, node)
        
    sorted_p = sorted(power_dict)[-10:]   
    sorted_p = reversed(sorted_p)

    file.write("\n\n")
    file.write("# Top US airports \n")
    file.write("**Top ten airports with most flights:** \n\n")
    
    top = []
    for i in sorted_p:
        file.write("* " + str(power_dict[i]) + "\n\n")
        top.append(power_dict[i])

    G_und = G.to_undirected(reciprocal=False, as_view=False)
    
   
    compute_centrality("In degree", nx.in_degree_centrality(G) ,top)  
    compute_centrality("Out degree", nx.out_degree_centrality(G) ,top)        
    compute_centrality("Degree", nx.degree_centrality(G_und) ,top)
    compute_centrality("Closeness", nx.closeness_centrality(G_und) ,top)
    
