# 02_informed_search/solutions/a_star.py
import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue format: (f_score, current_node, path, g_score)
    pq = [(heuristics[start], start, [start], 0)]
    visited = set()
    
    while pq:
        # Extract the state with the lowest f(n)
        f_score, current, path, g_score = heapq.heappop(pq)
        
        # Goal check
        if current == goal:
            return path, g_score
            
        if current in visited:
            continue
            
        visited.add(current)
        
        # Explore neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor not in visited:
                new_g = g_score + weight
                new_f = new_g + heuristics.get(neighbor, 0)
                heapq.heappush(pq, (new_f, neighbor, path + [neighbor], new_g))
                
    return None, float('inf')

if __name__ == "__main__":
    graph_map = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 5), ('E', 2)],
        'C': [('F', 3)],
        'D': [],
        'E': [('G', 2)],
        'F': [('G', 1)],
        'G': []
    }
    
    heuristic_values = {
        'A': 6, 'B': 4, 'C': 4, 'D': 6, 'E': 2, 'F': 1, 'G': 0
    }
    
    start_node = 'A'
    goal_node = 'G'
    
    path, cost = a_star_search(graph_map, heuristic_values, start_node, goal_node)
    if path:
        print(f"Optimal Path found: {' -> '.join(path)}")
        print(f"Total Path Cost: {cost}")
