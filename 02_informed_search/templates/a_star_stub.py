# 02_informed_search/templates/a_star_stub.py
import heapq

def a_star_search(graph, heuristics, start, goal):
    """
    Finds the shortest path from start to goal using A* Search.
    graph: dict representing adjacency list with edge weights {node: [(neighbor, weight), ...]}
    heuristics: dict containing h(n) values for each node {node: h_value}
    """
    # Priority queue stores tuples of: (f_score, current_node, path_taken, actual_g_cost)
    # Priority queue automatically keeps the lowest f_score at the top
    pq = [(heuristics[start], start, [start], 0)]
    
    # Track visited nodes to prevent cycles
    visited = set()
    
    while pq:
        # TODO: Pop the node with the lowest f_score from the priority queue (heapq.heappop)
        
        # TODO: If the current node is the goal, return the path and total actual cost (g)
        
        # TODO: If the node is already visited, skip it
        
        # TODO: Mark the node as visited
        
        # TODO: Loop through all neighbors of the current node
        # Calculate its g_score (current_g + edge_weight)
        # Calculate its f_score (g_score + heuristics[neighbor])
        # If neighbor not visited, push to priority queue (heapq.heappush)
        pass

    return None, float('inf')

if __name__ == "__main__":
    # Example Graph Map representation from the lab manual
    graph_map = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 5), ('E', 2)],
        'C': [('F', 3)],
        'D': [],
        'E': [('G', 2)],
        'F': [('G', 1)],
        'G': []
    }
    
    # Straight line distance heuristic values h(n)
    heuristic_values = {
        'A': 6, 'B': 4, 'C': 4, 'D': 6, 'E': 2, 'F': 1, 'G': 0
    }
    
    start_node = 'A'
    goal_node = 'G'
    
    print(f"Running A* Search from {start_node} to {goal_node}...")
    path, cost = a_star_search(graph_map, heuristic_values, start_node, goal_node)
    
    if path:
        print(f"Optimal Path found: {' -> '.join(path)}")
        print(f"Total Path Cost: {cost}")
    else:
        print("Goal is unreachable.")
