"""
doc
"""

def get_graph_from_file(file_name):
    """
    (str) -> (list)
    Read graph from file and return a list of edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    file = open(file_name, 'r', encoding='utf8')
    file = [i for i in file]
    file = [j.strip('\n') for j in file]
    file = [list(map(int, el.split(','))) for el in file]
    return file

def to_edge_dict(edge_list) :
    """
    This function will sort the elements of the graph by keys
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5]])
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    result = {}
    for i in edge_list :
        if i[0] in result :
            result[i[0]].append(i[1])
        else :
            result[i[0]] = [i[1]]
        if i[1] in result :
            result[i[1]].append(i[0])
        else :
            result[i[1]] = [i[0]]
    return result

def is_edge_in_graph(graph, edge):
    """
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    try :
        if edge[1] not in graph[edge[0]] or edge[0] not in graph[edge[1]] :
            return False
        else :
            return True
    except KeyError :
        return False

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict
    Add a new edge to the graph and return new graph.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] in graph :
        graph[edge[0]].append(edge[1])
    else :
        graph[edge[0]] = [edge[1]]
    if edge[1] in graph :
        graph[edge[1]].append(edge[0])
    else :
        graph[edge[1]] = [edge[0]]
    return graph

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in graph and edge[1] in graph[edge[0]] :
        graph[edge[0]].remove(edge[1])
    if edge[1] in graph and edge[0] in graph[edge[1]] :
        graph[edge[1]].remove(edge[0])
    return graph

def add_node(graph, node):
    """
    (dict, int) -> (dict)
    Add a new node to the graph and return a new graph.
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph :
        graph[node] = []
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)
    Delete a node and all incident edges from the graph.
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node in graph :
        graph.pop(node)
    for i in graph :
        if node in graph[i] :
            graph[i].remove(node)
    return graph

def convert_to_dot(graph):
    """
    (dict) -> (None)
    Save the graph to a file in a DOT format.
    """
    file = open('result.dot', 'w', encoding='utf8')
    file.write(graph)
    file.close()
    return None

if __name__=="__main__" :
    import doctest
    print(doctest.testmod())
