import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain  # For Louvain clustering

# Load transaction data
data = pd.read_csv('data/transactions.csv')

# Create a transaction network graph
G = nx.from_pandas_edgelist(data, source='Sender', target='Receiver', edge_attr='Amount')

# Compute centrality metrics
pagerank = nx.pagerank(G, alpha=0.85)
degree_centrality = nx.degree_centrality(G)

# Detect communities using Louvain method
partition = community_louvain.best_partition(G)

# Plot the transaction network
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, seed=42)  # Layout for visualization
nx.draw(G, pos, with_labels=True, node_size=[v * 5000 for v in degree_centrality.values()], node_color=list(partition.values()), cmap=plt.cm.Set3, edge_color='gray')
plt.title("Transaction Network Analysis")
plt.show()

# Print key entities based on PageRank
print("Top 5 Key Entities by PageRank:")
for node, score in sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"{node}: {score:.4f}")

# Save processed network data
data['PageRank'] = data['Sender'].map(pagerank)
data.to_csv('data/processed_transactions.csv', index=False)
