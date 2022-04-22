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
    # print("<-----Добавьте пути сами!----->")
    opening["A"]["B"] = int('1')
    opening["A"]["C"] = int('6')
    opening["A"]["D"] = int('13')
    opening["A"]["E"] = int('11')
    opening["A"]["F"] = int('99')
    opening["A"]["G"] = int('67')
    opening["B"]["A"] = int('5')
    opening["B"]["C"] = int('8')
    opening["B"]["D"] = int('7')
    opening["B"]["E"] = int('89')
    opening["B"]["F"] = int('1')
    opening["B"]["G"] = int('1')
    opening["C"]["B"] = int('14')
    opening["C"]["A"] = int('95')
    opening["C"]["D"] = int('134')
    opening["C"]["E"] = int('666')
    opening["C"]["F"] = int('888')
    opening["C"]["G"] = int('365')
    opening["D"]["B"] = int('904')
    opening["D"]["C"] = int('532')
    opening["D"]["A"] = int('78')
    opening["D"]["E"] = int('34')
    opening["D"]["F"] = int('644')
    opening["D"]["G"] = int('177')
    opening["E"]["B"] = int('47')
    opening["E"]["C"] = int('90')
    opening["E"]["D"] = int('72')
    opening["E"]["A"] = int('19')
    opening["E"]["F"] = int('85')
    opening["E"]["G"] = int('34')
    opening["F"]["B"] = int('567')
    opening["F"]["C"] = int('33')
    opening["F"]["D"] = int('36')
    opening["F"]["E"] = int('76')
    opening["F"]["A"] = int('99')
    opening["F"]["G"] = int('19')
    opening["G"]["B"] = int('1')
    opening["G"]["C"] = int('1')
    opening["G"]["D"] = int('56')
    opening["G"]["E"] = int('234')
    opening["G"]["F"] = int('456')
    opening["G"]["A"] = int('890')

    graph = Graph(znaks, opening)
    ot_kuda=input('От куда держишь путь, странник? : ')
    kuda=input('Куда держишь путь, странник? : ')
    perevorot, korotky = issledovatel(graph=graph, ot_kuda=ot_kuda)

    print_result(perevorot, korotky, ot_kuda=ot_kuda, kuda=kuda)
except ValueError:
    print('Вводите пожалуйста числа')