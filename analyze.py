import networkx as nx
import matplotlib.pyplot as plt


G=nx.read_pajek("USAir97.net")

G1=nx.Graph(G)

with open("slides.md", "w") as file:
    file.write("% Analysis of USAir97 network \n")
    file.write("% Zuzana Drázdová & Zuzana Šimečková \n")
    file.write("% January 7 2020 \n")
    file.write("# General information \n")
    file.write("US Air 97 Network has **{0}** nodes and **{1}** edges.\n".format(len(G.nodes),len(G.edges)))
    file.write("Nodes represent Airports in the United States and edges represent routes between these airtports. Each edge has weights with indicated how many flights are on given route")



    sorted_d = sorted([(value, key) for (key,value) in G1.degree], reverse=True)

    file.write("\n")
    file.write("# Top US airports \n")
    
    file.write("**Top ten airports with most flights:** \n\n")
    for i in range(10):
        file.write("* " + str(sorted_d[i][1]) + "\n\n")
        #file.write(sorted_d[:10])
    Gselection = G
    
    #print(G.nodes['San Francisco Intl'])

    remove = sorted_d[10:]
    nodes_to_remove = []
    for r in range(len(remove)):
        node = remove[r][1]
        nodes_to_remove.append(node)
        Gselection.remove_node(node)

    pos = nx.circular_layout(Gselection)



    #print(Gselection.nodes['San Francisco Intl'])
    
    positions = {}
    for node in Gselection.nodes:
        print(Gselection.nodes[node])
        data = Gselection.nodes[node]
        posi = (data['x'],-data['y'])
        positions.setdefault(node, posi)
    
    print(positions)
    
    nx.draw_networkx(Gselection, pos=positions, with_labels=True, node_size=100, edge_color="#ff000000")
    
    for (u, v, d) in Gselection.edges(data=True):
        w =  d['weight']
        edge = [(u,v,d)]
        nx.draw_networkx_edges(Gselection, pos=positions, edgelist=edge, equidistant=True, alpha=0.5, width=w*10)
    
    plt.savefig('most_flights.svg')
    file.write("\n")
    file.write("# Top US airports \n")
    file.write("![](most_flights.png)")
    
    
    
    

#print(G.edges['Minot Intl', 'Stapleton Intl',0])


