random.seed(2)
# Reducing the size of the network

df_edges = pd.read_csv("com-Amazon.csv", delimiter = " ")
OG = nx.from_pandas_edgelist(df_edges, source="From", target="To", create_using= nx.DiGraph) #the original co-purchasing network
nodes = random.sample(list(OG.nodes()), int(OG.number_of_nodes() * 0.23)) # will use only 26% of the graph
G=OG.subgraph(nodes)
largest_cc = max(nx.weakly_connected_components(G), key=len) #find the largest weakly component
G1=G.subgraph(largest_cc) # the final graph with the largest weakly connected component
#G1= G1.to_undirected()
G2_node_list= [] # add node that have the degree > 2
for node,degree in G1.degree():
    if degree > 2:
        G2_node_list.append(node)
G2= G1.subgraph(G2_node_list) #creating the graph base on the degree > 2
G2= G2.to_undirected()
removed_edges = random.sample(list(G2.edges()), int(G2.number_of_edges() * 0.30)) #we will removed 20% of the edges
G_train = G2.copy()
G_train.remove_edges_from(removed_edges)
G_test = G2.copy()
#G_test.add_edges_from(removed_edges)
print(OG)
print(G)
print(G1)
print(G2)
print(G_train)

