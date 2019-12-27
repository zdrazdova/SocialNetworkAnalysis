import networkx as nx
import matplotlib.pyplot as plt
import copy as cp
import numpy as np

def intro(G):
    file.write("% Analysis of USAir97 network \n")
    file.write("% Zuzana Drázdová & Zuzana Šimečková \n")
    file.write("% January 7 2020 \n")
    file.write("# General information \n")
    file.write("US Air 97 Network has **{0}** nodes and **{1}** edges.\n\n".format(len(G.nodes),len(G.edges)))
    file.write("Data are from company US Airways, from year 1997.\n\n")
    file.write("Nodes represent Airports in the United States and edges represent routes between these airtports.\n\n")
    file.write("Each edge has weights with indicated how many flights were on given route.\n\n")
    file.write("Each node has *x* and *y* coordinates that can be mapped to the geographical location of the airport.\n\n")


def top_reach(G):
    sorted_d = sorted([(value, key) for (key,value) in G.degree], reverse=True)
    file.write("\n")
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
    
    nx.draw_networkx(Gselection, pos=positions, with_labels=False, node_size=100, edge_color="#ff000000")
    
    for (u, v, d) in Gselection.edges(data=True):
        w =  d['weight']
        edge = [(u,v,d)]
        nx.draw_networkx_edges(Gselection, pos=positions, edgelist=edge, equidistant=True, alpha=0.5, width=w*20)
    plt.savefig('most_other_airports.svg')
    
    file.write("\n")
    file.write("# Top US airports \n")
    file.write("![Airports with flights to/from most other airports - map](top_reach.png)")


def top_flights(G):
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
        
    Gpower = cp.deepcopy(G)    
        
    for node in G.nodes:
        if node not in top:
            Gpower.remove_node(node)
    plt.figure(figsize=(8,3.4))

    positions = {}
    for node in Gpower.nodes:
        data = Gpower.nodes[node]
        posi = (data['x'],-data['y'])
        positions.setdefault(node, posi)
    
    nx.draw_networkx(Gpower, pos=positions, with_labels=False, node_size=100, edge_color="#ff000000")
    
    for (u, v, d) in Gpower.edges(data=True):
        w =  d['weight']
        edge = [(u,v,d)]
        nx.draw_networkx_edges(Gpower, pos=positions, edgelist=edge, equidistant=True, alpha=0.5, width=w*20)
    
    plt.savefig('most_flights.svg')
    file.write("\n\n")
    file.write("# Top US airports \n")
    file.write("![Airports with most flights - map](top_flights.png)\n\n")
    return top

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
            
def compute_betweenness(G):
    file.write("\n")
    file.write("# Centralities \n\n")
    file.write("### Edge betweenness: \n") 
    betweenness = nx.edge_betweenness_centrality(G)
    sorted_top_b = sorted(betweenness.values(),reverse=True)[:10]
    for edge in G.edges:
        u,v,x = edge
        if betweenness[(u,v)] in sorted_top_b:
            if betweenness[(u,v)] == sorted_top_b[0]:
                file.write("* " + str(u) + " -- " + str(v) + ": **" + str(betweenness[(u,v)]) + "**\n\n")
            else:
                file.write("* " + str(u) + " -- " + str(v) + ": " + str(betweenness[(u,v)]) + "\n\n")


def random_graph(nodes,edges):
    G = nx.Graph()
    for n in range(nodes):
        G.add_node(n)
    e = 0
    while e < edges:
        u = np.random.randint(0,nodes)
        v = np.random.randint(0,nodes)
        if u != v and (u,v) not in G.edges and (v,u) not in G.edges:
            G.add_edge(u,v)  
            e = e+1 
    return G

def diameter(G):
    file.write("\n")
    file.write("# Graph diameter \n")
    file.write("Social networks have small diameter \n\n")
    R = random_graph(len(G.nodes), len(G.edges))
    
    file.write("Random network with the same amount of nodes and edges has diameter **{0}** \n\n".format(nx.diameter(R)))
    diameter = nx.diameter(G)
    counter = 0
    for u in G.nodes:
        for v in G.nodes:
            if len(nx.shortest_path(G,u,v)) > diameter:
                counter += 1
    file.write("Our network has diameter **{0}**\n\n".format(diameter))
    file.write(" * Number of routes with max shortest length: **{0}** \n".format(int(counter/2)))
    file.write(" * All of them start: *West Tinian* - *Saipan* - *Guam* - *Honolulu*\n")
    file.write(" * Most of them end: *Anchorage* - *Bethel* - *SAT*\n")
    file.write(" * Where SAT stands for Small Alaskan Town = {Tuluksak, Akiachak, Akiak, Kwethluk, Napaskiak, Napakiak, Tuntutuliak, Eek, Kongiganak, Kwigillingok, Quinhagak}\n\n")
    
    Gal = cp.deepcopy(G)
    
    Alaska = {"Anchorage Intl", "Bethel", "Tuluksak", "Akiachak", "Akiak", "Kwethluk", "Napaskiak", "Napakiak", "Tuntutuliak", "Eek", "Kongiganak", "Kwigillingok", "Quinhagak"}
    
    Gguam = cp.deepcopy(G)
    
    Guam = {"Saipan Intl", "Rota Intl", "Guam Intll", "Babelthuap/Koror", "West Tinian"}

    
    for node in G.nodes:
        if node not in Alaska:
            Gal.remove_node(node)
        if node not in Guam:
            Gguam.remove_node(node)
      
    plt.figure(figsize=(8,3.4))

    positions = {}
    for node in Gguam.nodes:
        data = Gguam.nodes[node]
        posi = (data['x'],-data['y'])
        positions.setdefault(node, posi)
    
    nx.draw_networkx(Gguam, pos=positions, with_labels=True, node_size=40, edge_color="#ff000000")
    
    for (u, v, d) in Gguam.edges(data=True):
        w =  d['weight']
        edge = [(u,v,d)]
        nx.draw_networkx_edges(Gguam, pos=positions, edgelist=edge, equidistant=True, alpha=0.7, width=w*40)
    
    plt.savefig('guam.svg')
    file.write("\n\n")
    file.write("\n# Islands in Pacific Ocean\n")
    file.write("![Airports around Guam territory - map](guam.png)\n\n")  
    
    plt.figure(figsize=(8,3.4))

    positions = {}
    for node in Gal.nodes:
        data = Gal.nodes[node]
        posi = (data['x'],-data['y'])
        positions.setdefault(node, posi)
    
    nx.draw_networkx(Gal, pos=positions, with_labels=True, node_size=40, edge_color="#ff000000")
    
    for (u, v, d) in Gal.edges(data=True):
        w =  d['weight']
        edge = [(u,v,d)]
        nx.draw_networkx_edges(Gal, pos=positions, edgelist=edge, equidistant=True, alpha=0.7, width=w*40)
    
    plt.savefig('alaska.svg')
    file.write("\n\n")
    file.write("\n# Small Alaskan Towns\n")
    file.write("![Airports in southern Alaska - map](alaska.png)\n\n")
 



def other_properties(G, top):
    file.write("\n# Other properties \n")
    
    file.write("Radius of the graph: **{0}** \n\n\n".format(nx.radius(G)))
    
    max_edges = len(G.nodes)*(len(G.nodes)-1)/2
    file.write("Density of the graph: **{0}** \n\n\n".format(len(G.edges)/max_edges))
    to_remove = []
    Gtop = cp.deepcopy(G)
    for node in G.nodes:
        if node not in top:
            Gtop.remove_node(node)
    max_edges = len(Gtop.nodes)*(len(Gtop.nodes)-1)/2
    file.write("Density of the graph of top airports: **{0}** \n\n".format(len(Gtop.edges)/max_edges))

    Gbrid = cp.deepcopy(G)
    counter = 0
    top_weight = 0
    top_edge = 0
    for (u, v, d) in G.edges(data=True):
        w =  d['weight']
        Gbrid.remove_edge(u,v)
        if not nx.is_connected(Gbrid):
            counter += 1
            if w > top_weight:
                top_weight = w
                top_edge = (u,v)
        Gbrid.add_edge(u,v)
    file.write("US Air 97 is **connected** network. \n\n".format(counter))
    file.write("It has **{0}** bridges. \n\n".format(counter))
    file.write("Most important bridge is **{0}** to **{1}**. \n\n".format(top_edge[0],top_edge[1]))

def max_clique(G):
    Gcls = nx.find_cliques(G)
    top_clique = None
    top_clique_size = 0
    for i in Gcls:
        if len(i)>top_clique_size:
            top_clique_size = len(i)
            top_clique = i
    file.write("\n")
    file.write("\n# Max clique \n")
    file.write("Size of max clique: **{0}**\n".format(top_clique_size))
    Gclique = cp.deepcopy(G)
    for node in G.nodes:
        if node not in top_clique:
            Gclique.remove_node(node)
    plt.figure(figsize=(8,3.4))

    positions = {}
    for node in Gclique.nodes:
        data = Gclique.nodes[node]
        posi = (data['x'],-data['y'])
        positions.setdefault(node, posi)
    
    nx.draw_networkx(Gclique, pos=positions, with_labels=True, node_size=100, edge_color="#ff000000")
      
    plt.savefig('max_clique.svg')
    file.write("![Airports - max clique - map](max_clique.png)\n\n")

    


def power_law(G):
    degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
    max_degree = max(degree_sequence)
    
    degree_array = np.zeros((max_degree+1))
    for i in degree_sequence:
        degree_array[i] += 1
    non_zero = 0
    for i in range(max_degree+1):
        if degree_array[i] != 0:
            non_zero += 1
    plot_degree = np.zeros((non_zero,2))
    index = 0
    for i in range(max_degree):
        if degree_array[i+1] != 0:
            plot_degree[index][0] = i+1
            plot_degree[index][1] = degree_array[i+1]
            index += 1

    x, y = plot_degree.T
    plt.clf()
    plt.figure(figsize=(8,5))
    plt.scatter(x,y)
    plt.ylabel("Number of nodes")
    plt.xlabel("Degree")
    
    plt.savefig('power_law.png')
    
    
    file.write("\n")
    file.write("# Power-law degree \n")
    
    file.write("![Power-law degree distribution](power_law.png)")

G=nx.read_pajek("USAir97.net")
G = G.to_undirected(reciprocal=False, as_view=False)

with open("slides.md", "w") as file:

    
    
    intro(G)

    top_reach(G)

    top = top_flights(G)
    
    compute_centrality("Degree", nx.degree_centrality(G), top)
    
    compute_centrality("Closeness", nx.closeness_centrality(G), top)
    
    compute_betweenness(G)  
    
    diameter(G) 
    
    other_properties(G, top)
    
    max_clique(G)
    
    power_law(G)
    
    
    
    
