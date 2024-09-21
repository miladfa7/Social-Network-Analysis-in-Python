# Social-Network-Analysis-in-Python (facebook)

Social Network Analysis in Python
Networks today are part of our everyday life. Let's learn how to visualize and understand a social network in Python using Networks <br>

## Dataset information
The dataset you are referring to is the Facebook Social Circles Dataset, which is part of a collection of social network datasets. This dataset was collected by analyzing ego networks on Facebook, where an ego network is defined as a focal node (the ego) and all the nodes (friends) connected to it, along with the links (friendships) between these friends. The key aspects of this dataset include:

     - Node Features: Information about individual users, although anonymized.
     - Circles: Groups of friends, similar to how Facebook allows users to organize friends into different lists.
     - Ego Networks: Networks centered around a specific user (the ego), including that user's friends and the connections between them.
<b>Key Statistics<b>:

    Nodes: 4039 (representing users)
    Edges: 88234 (representing friendships)
    Clustering Coefficient: 0.6055 (indicating a relatively high level of clustering)
    Triangles: 1.61 million (showing the number of friend groups that are fully connected)
    Diameter: 8 (the longest shortest path between any two nodes)
    Effective Diameter: 4.7 (90th percentile of the shortest path lengths between nodes)
    

https://snap.stanford.edu/data/ego-Facebook.html <br>
![betweenness_centrality](https://user-images.githubusercontent.com/25765644/141525940-b0f12e32-cff6-4d30-bd0f-45fba8d5091d.png)


## 

1- Betweenness Centrality <br>
Betweenness centrality is defined as a measure of how often a node lies on the shortest path between all pairs of nodes in a network
```
python scripts/betweenness_centrality.py
```
2- Degree Centrality <br>
3- Closeness Centrality <br>
4- Eeigenvector Centrality <br>
5- Find shortest path <br>
6- Find all neighbors the nodes <br>
7- Degree Grapg <br>
8- K-clique <br>
9- K-core <br>
10- pagerank <br>
