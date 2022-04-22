import sys
try:
    class Graph(object):
        def __init__(self, znak, opening):
            self.znak = znak
            self.graph = self.construct_graph(znak, opening)
        def construct_graph(self, znak, opening):
            graph = {}
            for znak in znak:
                graph[znak] = {}
            graph.update(opening)
            for znak, edges in graph.items():
                for adjacent_node, value in edges.items():
                    if graph[adjacent_node].get(znak, False) == False:
                        graph[adjacent_node][znak] = value
            return graph
        def get_nodes(self):
            return self.znak
        def get_outgoing_edges(self, znak):
            connections = []
            for out_node in self.znak:
                if self.graph[znak].get(out_node, False) != False:
                    connections.append(out_node)
            return connections
        def value(self, node1, node2):
            return self.graph[node1][node2]
    def issledovatel(graph, ot_kuda):
        unvisited_nodes = list(graph.get_nodes())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        for znak in unvisited_nodes:
            shortest_path[znak] = max_value
        shortest_path[ot_kuda] = 0
        while unvisited_nodes:
            current_min_node = None
            for znak in unvisited_nodes:
                if current_min_node == None:
                    current_min_node = znak
                elif shortest_path[znak] < shortest_path[current_min_node]:
                    current_min_node = znak
            neighbors = graph.get_outgoing_edges(current_min_node)
            for neighbor in neighbors:
                tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
                if tentative_value < shortest_path[neighbor]:
                    shortest_path[neighbor] = tentative_value
                    previous_nodes[neighbor] = current_min_node
            unvisited_nodes.remove(current_min_node)
        return previous_nodes, shortest_path
    def print_result(perevorot, korotky, ot_kuda, kuda):
        path = []
        znak = kuda
        if znak == ot_kuda:
            print("<----------------------------ALERT---------------------------->")
            print('Вы допустили ошибку при вводе данных')
        while znak != ot_kuda:
            path.append(znak)
            znak = perevorot[znak]
        path.append(ot_kuda)
        print("Самый короткий путь: {}".format(korotky[kuda]))
        print(" -> ".join(reversed(path)))
    znaks = ["A", "B", "C", "D", "E", "F", "G", "H"]
    opening = {}
    for znak in znaks:
        opening[znak] = {}

    matrix = input('ВВЕДИТЕ ПУТЬ К ФАЙЛУ: ')
    with open(matrix) as f:
        myList = [line.split() for line in f]

    opening["A"]["B"] = int(myList[1][2])
    opening["A"]["C"] = int(myList[1][3])
    opening["A"]["D"] = int(myList[1][4])
    opening["A"]["E"] = int(myList[1][5])
    opening["A"]["F"] = int(myList[1][6])
    opening["A"]["G"] = int(myList[1][7])
    opening["A"]["H"] = int(myList[1][8])
    opening["B"]["A"] = int(myList[2][2])
    opening["B"]["C"] = int(myList[2][3])
    opening["B"]["D"] = int(myList[2][4])
    opening["B"]["E"] = int(myList[2][5])
    opening["B"]["F"] = int(myList[2][6])
    opening["B"]["G"] = int(myList[2][7])
    opening["B"]["H"] = int(myList[2][8])
    opening["C"]["B"] = int(myList[3][2])
    opening["C"]["A"] = int(myList[3][3])
    opening["C"]["D"] = int(myList[3][4])
    opening["C"]["E"] = int(myList[3][5])
    opening["C"]["F"] = int(myList[3][6])
    opening["C"]["G"] = int(myList[3][7])
    opening["C"]["H"] = int(myList[3][8])
    opening["D"]["B"] = int(myList[4][2])
    opening["D"]["C"] = int(myList[4][3])
    opening["D"]["A"] = int(myList[4][4])
    opening["D"]["E"] = int(myList[4][5])
    opening["D"]["F"] = int(myList[4][6])
    opening["D"]["G"] = int(myList[4][7])
    opening["D"]["H"] = int(myList[4][8])
    opening["E"]["B"] = int(myList[5][2])
    opening["E"]["C"] = int(myList[5][3])
    opening["E"]["D"] = int(myList[5][4])
    opening["E"]["A"] = int(myList[5][5])
    opening["E"]["F"] = int(myList[5][6])
    opening["E"]["G"] = int(myList[5][7])
    opening["E"]["H"] = int(myList[5][8])
    opening["F"]["B"] = int(myList[6][2])
    opening["F"]["C"] = int(myList[6][3])
    opening["F"]["D"] = int(myList[6][4])
    opening["F"]["E"] = int(myList[6][5])
    opening["F"]["A"] = int(myList[6][6])
    opening["F"]["G"] = int(myList[6][7])
    opening["F"]["H"] = int(myList[6][8])
    opening["G"]["B"] = int(myList[7][2])
    opening["G"]["C"] = int(myList[7][3])
    opening["G"]["D"] = int(myList[7][4])
    opening["G"]["E"] = int(myList[7][5])
    opening["G"]["F"] = int(myList[7][6])
    opening["G"]["A"] = int(myList[7][7])
    opening["G"]["H"] = int(myList[7][8])
    opening["H"]["B"] = int(myList[8][2])
    opening["H"]["C"] = int(myList[8][3])
    opening["H"]["D"] = int(myList[8][4])
    opening["H"]["E"] = int(myList[8][5])
    opening["H"]["F"] = int(myList[8][6])
    opening["H"]["G"] = int(myList[8][7])
    opening["H"]["A"] = int(myList[8][8])

    graph = Graph(znaks, opening)
    ot_kuda=input('От куда держишь путь, странник? : ')
    kuda=input('Куда держишь путь, странник? : ')
    perevorot, korotky = issledovatel(graph=graph, ot_kuda=ot_kuda)

    print_result(perevorot, korotky, ot_kuda=ot_kuda, kuda=kuda)
except ValueError:
    print('Вводите пожалуйста числа')