import networkx as nx
import matplotlib.pyplot as plt



class GraphCentrality:
    def __init__(self, edge_list_file):
        self.edge_list_file = edge_list_file
        self.graph = None
        self.betweenness_centrality = None
        self.load_graph()

    def load_graph(self):
        """Loads the graph from the edge list file into a NetworkX Graph object."""
        try:
            self.graph = nx.read_edgelist(self.edge_list_file, create_using=nx.Graph(), nodetype=int)
            print(f"Graph loaded successfully with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges.")
        except Exception as e:
            print(f"Error loading graph: {e}")

    def compute_betweenness_centrality(self) -> None:
        """Computes the betweenness centrality for each node in the graph."""

        print("Start Computing...")
        self.betweenness_centrality = nx.betweenness_centrality(self.graph)
        print("Computation completed.")
    
    def display_top_central_nodes(self, top_n: int=10) -> None:
        """
        Displays the top N nodes with the highest betweenness centrality.
    
        """

        sorted_centrality = sorted(self.betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
        print(f"Top {top_n} nodes by Betweenness Centrality:")
        for i in range(min(top_n, len(sorted_centrality))):
            print(f"Node {sorted_centrality[i][0]}: {sorted_centrality[i][1]}")
    
    def visualize_graph(self):
        """Visualizes the graph with nodes for betweenness centrality."""
  
        plt.figure(figsize=(20, 20))

        # centrality values for the node sizes
        node_color = [20000.0 * self.graph.degree(v) for v in self.graph]
        node_size = [v * 10000 for v in self.betweenness_centrality.values()]
        pos = nx.spring_layout(self.graph)

        # Draw the graph
        nx.draw_networkx(
            self.graph, pos=pos, with_labels=False,
            node_color=node_color, node_size=node_size, cmap=plt.cm.viridis
        )
        
        plt.axis('off')
        
        # sm = plt.cm.ScalarMappable(cmap=plt.cm.viridis, norm=plt.Normalize(vmin=min(node_color), vmax=max(node_color)))        
        # sm.set_array([])
        # plt.colorbar(sm)

        # Show the graph
        plt.title("Betweenness Centrality in Facebook Social Network")
        graph_output = f"../images/betweenness_centrality_2.jpg"
        plt.savefig(graph_output)
        print(f"Graph is successfully saved in this path: {graph_output}")
        plt.show()


# Usage:
if __name__ == "__main__":
    graph_centrality = GraphCentrality("../dataset/facebook_combined.txt")

    graph_centrality.compute_betweenness_centrality()

    graph_centrality.display_top_central_nodes(top_n=10)

    graph_centrality.visualize_graph()

