from manim import *
from queue import Queue

class GraphNode:
    def __init__(self, data, position=ORIGIN, radius=0.5, neighbors=[], scale=1):
        self.char = data
        self.data = Tex(str(data))
        self.data.scale(scale)
        self.neighbors = []
        self.center = position
        self.radius = radius
        self.circle = Circle(radius=radius)
        self.circle.move_to(position)
        self.data.move_to(position)
        self.drawn = False
        self.marked = False
        self.edges = []
        self.prev = None

    def connect(self,other):
        line_center = Line(self.center, other.center)
        unit_vector = line_center.get_unit_vector()
        start,end = line_center.get_start_and_end()
        new_start = start + unit_vector* self.radius
        new_end = end - unit_vector * self.radius
        line = Line(new_start,new_end)
        self.neighbors.append(other)
        other.neighbors.append(self)
        self.edges.append(line)
        other.edges.append(line)
        return line
    

class animation(Scene):
    
    def construct(self):
        self.show_bfs_animation()
    
    def show_bfs_animation(self):
        bfs_title = Tex("BFS animation")
        bfs_title.scale(1.2)
        bfs_title.move_to(UP*3.5)
        linija = Line(LEFT,RIGHT)
        linija.next_to(bfs_title,DOWN).scale(7)

        graph, edge_dict = self.create_bfs_graph()
        nodes,edges = self.make_graph_mobject(graph,edge_dict)

        entire_graph = VGroup(nodes, edges)

        self.play(
            Write(bfs_title),
            Create(linija)
        )
        
        self.wait()

        self.play(
            Write(entire_graph),
            run_time = 3
        )

        self.wait()

        # print(graph)
        bfs_full_order = bfs(graph,0)

        scale_factor = 1

        for element in bfs_full_order:
            if isinstance(element, int):
                surround_circle = self.highlight_node(graph, element, scale_factor= scale_factor, run_time=1)
            else:
                last_edge = self.sharpie_edge(edge_dict, element[0] , element[1], color= RED)    

    def highlight_node_red(self,graph, element,color= RED, scale_factor = 1):
        node = graph[element]
        surround_circle = Circle(radius= node.circle.radius)
        surround_circle.move_to(node.circle.get_center())
        surround_circle.set_color(color)
        surround_circle.set_stroke(width=8*scale_factor)
        surround_circle.set_fill(opacity=0)

        self.play(
            Create(surround_circle),
            run_time = 1
        )


        return surround_circle



    def sharpie_edge(self, edge_dict, u , v, color = BLUE, scale_factor =1, run_time = 1):
        
        edge = edge_dict[(u,v)]
        line = Line(edge.get_start(), edge.get_end())
        line.set_stroke(width=16 * scale_factor)
        line.set_color(color)

        self.play(
            Create(line),
            run_time =1 
        )

        return line

    def highlight_node(self, graph, index, color= GREEN,scale_factor =1, animate =  True, run_time =1 ):

        node = graph[index]
        surround_circle = Circle(radius = node.circle.radius)
        surround_circle.move_to(node.circle.get_center())
        surround_circle.set_stroke(width=8*scale_factor)
        surround_circle.set_color(color)
        surround_circle.set_fill(opacity=0)

        if animate:
            self.play(
                Create(surround_circle),
                run_time = run_time
            )
        return surround_circle
    def create_bfs_graph(self):
        graph = []
        edges = {}

        radius, scale = 0.4, 0.9

        node_0 = GraphNode('0', position= UP * 2.3, radius=radius, scale=scale)
        node_1 = GraphNode('1', position= UP  + LEFT * 3.0, radius=radius, scale=scale)
        node_2 = GraphNode('2',position= UP*0.7, radius=radius, scale=scale)
        node_3 = GraphNode('3', position= UP + RIGHT * 3.0, radius=radius, scale=scale)
        node_4 = GraphNode('4', position= LEFT * 5.0 + DOWN, radius=radius, scale=scale)
        node_5 = GraphNode('5', position= LEFT * 3 + DOWN, radius=radius, scale=scale)
        node_6 = GraphNode('6', position= RIGHT * 3 + DOWN, radius=radius, scale=scale)
        node_7 = GraphNode('7', position= RIGHT * 5.0 + DOWN, radius=radius, scale=scale)
        node_8 = GraphNode('8', position= LEFT * 6.0 + DOWN * 3.0, radius=radius, scale=scale)
        node_9 = GraphNode('9', position= LEFT * 3.5 + DOWN * 3.0, radius=radius, scale=scale)
        node_10 = GraphNode('10', position= RIGHT * 2.0 + DOWN * 3.0, radius=radius, scale=scale)
        node_11 = GraphNode('11', position= RIGHT * 4.0 + DOWN * 3.0, radius=radius, scale=scale)

        edges[(0,1)] = node_0.connect(node_1)
        edges[(0,2)] = node_0.connect(node_2)
        edges[(0,3)] = node_0.connect(node_3)
        edges[(1,4)] = node_1.connect(node_4)
        edges[(1,5)] = node_1.connect(node_5)
        edges[(3,6)] = node_3.connect(node_6)
        edges[(3,7)] = node_3.connect(node_7)
        edges[(4,8)] = node_4.connect(node_8)
        edges[(4,9)] = node_4.connect(node_9)
        edges[(6,10)] = node_6.connect(node_10)
        edges[(6,11)] = node_6.connect(node_11)

        graph.append(node_0)
        graph.append(node_1)
        graph.append(node_2)
        graph.append(node_3)
        graph.append(node_4)
        graph.append(node_5)
        graph.append(node_6)
        graph.append(node_7)
        graph.append(node_8)
        graph.append(node_9)
        graph.append(node_10)
        graph.append(node_11)

        return graph, edges
    

    def make_graph_mobject(self,graph, edge_dict, node_color = DARK_BLUE, stroke_color = BLUE, data_color = WHITE, edge_color = GRAY, scale_factor =1 , show_data = True):

        nodes = []
        edges=  []

        for node in graph:
            node.circle.set_fill(color = node_color, opacity = 0.5)
            node.circle.set_stroke(color = stroke_color)
            node.data.set_color(color = data_color)

            if show_data:
                nodes.append(VGroup(node.circle, node.data))
            else:
                nodes.append(VGroup(node.circle))
            
        
        for edge in edge_dict.values():
            edge.set_stroke(width = 7*scale_factor)
            edge.set_color(color = edge_color)
            edges.append(edge)

        return VGroup(*nodes), VGroup(*edges)
    

def bfs(graph,start):
    bfs_order = []
    marked = [False] * len(graph)
    edge_to  = [None] * len(graph)

    queue = Queue()

    queue.put(start)

    while not queue.empty():
        node = queue.get()
        marked[node]= True
        bfs_order.append(node)

        for sused in graph[node].neighbors:
            neighbour_node = int(sused.char)
            if not marked[neighbour_node]:
                edge_to[neighbour_node] = node
                queue.put(neighbour_node)
    
    print(bfs_order)

    bfs_full_order = []

    for i in range(len(bfs_order) - 1):
        prev,curr = bfs_order[i], bfs_order[i+1]
        bfs_full_order.append(prev)
        bfs_full_order.append((edge_to[curr], curr))
    
    bfs_full_order.append(curr)
    print(bfs_full_order)
    return bfs_full_order