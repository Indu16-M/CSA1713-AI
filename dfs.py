def dfs(graph, start_node, visited=None):
    # If visited set is not provided, initialize it as an empty set
    if visited is None:
        visited = set()

    # Mark the node as visited and print it
    visited.add(start_node)
    print(start_node, end=" ")

    # Recursively visit all unvisited neighbors
    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def take_graph_input():
    graph = {}
    
    # Input the number of edges
    edges_count = int(input("Enter the number of edges in the graph: "))
    
    print("Enter each edge in the format 'node1 node2' (separated by a space):")
    for _ in range(edges_count):
        edge = input().split()
        node1, node2 = edge[0].upper(), edge[1].upper()  # Ensure uppercase
        
        # Add nodes to the graph if not already present
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        
        # Add the edge in both directions (undirected graph)
        graph[node1].append(node2)
        graph[node2].append(node1)
    
    return graph

def main():
    # Take graph input from the user
    graph = take_graph_input()
    
    # Take the starting node for DFS
    start_node = input("Enter the starting node for DFS: ").upper()  # Ensure uppercase input
    
    # Call DFS and show the result
    print(f"DFS Traversal starting from node {start_node}: ", end="")
    dfs(graph, start_node)

if __name__ == "__main__":
    main()
