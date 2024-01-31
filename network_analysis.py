# %% [markdown]
# calculation of the "betweenness", "closeness" and "PageRank" on all of the nodes for Facebook-Ego dataset

# %%
import networkx as nx

# Function that Load the Facebook-Ego dataset 
def load_network(edges_file):
   G= nx.Graph()
   with open(edges_file) as f:
      for line in f:
         a, b = line.split()  
         G.add_edge(a, b)
   return G

# Load dataset   
G_facebook = load_network("686.edges") 

# Calculate node metrics
betweenness = nx.betweenness_centrality(G_facebook)
closeness = nx.closeness_centrality(G_facebook) 
pagerank = nx.pagerank(G_facebook)

# Print node metrics
for node in G_facebook.nodes():
   print(f"Node: {node}")
   print(f"Betweenness: {betweenness[node]}") 
   print(f"Closeness: {closeness[node]}")
   print(f"PageRank: {pagerank[node]}")
   print("-"*30)


