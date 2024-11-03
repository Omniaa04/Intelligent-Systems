def path_cost(path):
    final_cost=0
    for (node,cost) in path:
        final_cost+=cost
    return final_cost , path[-1][0]



Graph={
    'S':[('A',2), ('B',3), ('D',5)],
    'A':[('C',4)],
    'B':[('D',4)],
    'C':[('D',1),('G',2)],
    'D':[('G',5)],
}

def UCS(graph, start, goal):
    visitted=[]
    queue=[[(start,0)]]
    while  queue:
        queue.sort(key = path_cost)
        path=queue.pop(0)
        node=path[-1][0]
        if node in visitted:
            continue
        visitted.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node,[])
            for(node2 , cost) in adjacent_nodes :
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

solution = UCS(Graph, 'S', 'G')
print("Solution is" , solution)
print("Cost of Solution is " , path_cost(solution)[0])
