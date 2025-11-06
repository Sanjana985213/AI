graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1),('E',5)],
    'D': [('E', 8)],
    'E': [('J', 5),('I',5)],
    'F': [('G', 1),('H',7)],
    'G': [('I',3)],
    'H': [('I',2)],
    'I': [('J',3)],
    'J':[]
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
    
}
def a_star(graph, heuristic, start, goal):
    open_nodes = {start}
    cost_from_start = {start: 0}  # g(n)
    total_estimated_cost = {start: heuristic[start]}  # f(n) = g(n) + h(n)
    parent = {}

    while open_nodes:
        current = min(open_nodes, key=lambda x: total_estimated_cost[x])

        
        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], cost_from_start[goal]  

        open_nodes.remove(current)

        
        for neighbor, cost in graph[current]:
            new_cost = cost_from_start[current] + cost
            if new_cost < cost_from_start.get(neighbor, float('inf')):
                parent[neighbor] = current
                cost_from_start[neighbor] = new_cost
                total_estimated_cost[neighbor] = new_cost + heuristic[neighbor]
                open_nodes.add(neighbor)

    return None, None  



path = a_star(graph, heuristics, 'A', 'J')
print("Shortest path:", path)
