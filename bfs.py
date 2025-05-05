from collections import deque

def bfs(graph, start_node):
    # Create a set for visited nodes
    visited = set()
    # Create a queue to explore nodes
    queue = deque([start_node])

    # Start BFS traversal
    visited.add(start_node)
    print(f"BFS Traversal starting from node {start_node}: ", end="")
    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Visit the node
        
        # Add unvisited neighbors to the queue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    print()  # New line after the traversal

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
    
    # Take the starting node for BFS
    start_node = input("Enter the starting node for BFS: ").upper()  # Ensure uppercase input
    
    # Call BFS and show the result
    bfs(graph, start_node)

if __name__ == "__main__":
    main()
