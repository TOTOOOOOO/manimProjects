from manim import*


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
        self.show_dfs_intuition()
    
    def show_dfs_intuition(self):
        
        dfs_title = Tex("DFS animation")
        dfs_title.scale(1.2)
        dfs_title.move_to(UP*3.5)
        linija = Line(LEFT,RIGHT)
        linija.next_to(dfs_title,DOWN).scale(7)


        graph, edge_dict = self.create_dfs_graph()
        nodes,edges = self.make_graph_mobject(graph, edge_dict)

        print(edge_dict)

        entire_graph = VGroup(nodes, edges)
        
        self.play(
            Write(dfs_title),
            Create(linija)
        )

        self.wait() 
        
        self.play(
            Write(entire_graph),
            run_time = 3
        )

        self.wait(1)

        dfs_full_order = dfs(graph,0)
        
        preorder = Tex(*r"Preorder:   0   1   2   3   5   6   7   8   9   4".split('  '))
        postorder = Tex(*r"Postorder:   2   6   9   8   7   5   3   4   1   0".split('  '))
        
        preorder.shift(DOWN*0.5)
        preorder.next_to(entire_graph, DOWN)
        postorder.next_to(preorder,DOWN)
        # postorder.shift(LEFT*0.75)

        self.play(
            Write(preorder[:1]),
            Write(postorder[:1])
        )

        order_index = 1
        post_order_index = 1

        scale_factor = 1
        
        last_node = -1

        for element in dfs_full_order:
            if isinstance(element,int):
                surround_circle = self.highlight_node(graph,element, scale_factor = scale_factor,run_time = 1)
                self.play(
                    TransformFromCopy(graph[element].data, preorder[order_index])
                )
                       
                last_node = element
                order_index += 1


                if element == 4:
                    lista = [4,1,0]
                    for i in lista:
                        surround_circle = self.highlight_node_red(graph,i)
                        self.wait()
                        self.play(
                            TransformFromCopy(graph[i].data, postorder[post_order_index])
                        )

                        post_order_index += 1
                        
                
                if element == 9:
                    pom = [9,8,7,5,3]
                    
                    for i in pom:
                        surround_circle = self.highlight_node_red(graph,i)
                        self.wait()
                        self.play(
                            TransformFromCopy(graph[i].data, postorder[post_order_index])
                        )

                        post_order_index += 1
                
            else:
                e = element[0]
                if e != last_node and last_node != 9:
                    surround_circle = self.highlight_node_red(graph,last_node)
                    self.wait()
                    self.play(
                        TransformFromCopy(graph[last_node].data, postorder[post_order_index])
                    )

                    post_order_index += 1

                last_edge = self.sharpie_edge(edge_dict, element[0], element[1], scale_factor = scale_factor, run_time = 1)


        self.wait(3)

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
        line.set_color(GREEN)

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

    def create_dfs_graph(self):
        graph = []
        edges = {}

        radius,scale = 0.4, 0.9

        SHIFT = RIGHT * 2.5

        node_0 = GraphNode('0', position=LEFT * 5, radius=radius, scale=scale)
        node_1 = GraphNode('1', position=LEFT * 3 + UP * 2, radius=radius, scale=scale)
        node_2 = GraphNode('2', position=LEFT * 3 + DOWN * 2, radius=radius, scale=scale)
        node_3 = GraphNode('3', position=LEFT * 1, radius=radius, scale=scale)
        node_4 = GraphNode('4', position=LEFT * 1 + UP * 2, radius=radius, scale=scale)
        node_5 = GraphNode('5', position=RIGHT * 1, radius=radius, scale=scale)
        node_6 = GraphNode('6', position=LEFT * 1 + DOWN * 2, radius=radius, scale=scale)
        node_7 = GraphNode('7', position=RIGHT * 3 + DOWN * 2, radius=radius, scale=scale)
        node_8 = GraphNode('8', position=RIGHT * 3 + UP * 2, radius=radius, scale=scale)
        node_9 = GraphNode('9', position=RIGHT * 5 + UP * 2, radius=radius, scale=scale)
    

        edges[(0,2)] = node_0.connect(node_2)
        edges[(0,1)] =  node_0.connect(node_1)
        edges[(1, 4)] = node_1.connect(node_4)
        edges[(1, 3)] = node_1.connect(node_3)
        edges[(1, 2)] = node_1.connect(node_2)
        edges[(3, 5)] = node_3.connect(node_5)
        edges[(5, 8)] = node_5.connect(node_8)
        edges[(5, 7)] = node_5.connect(node_7)
        edges[(5, 6)] = node_5.connect(node_6)
        edges[(7, 8)] = node_7.connect(node_8)
        edges[(8, 9)] = node_8.connect(node_9)

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

        return graph,edges

    
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



def dfs(graph,start):
    # vraca listu preorder listu cvorova i grana
    dfs_order = []
    marked = [False] * len(graph)
    edge_to = [None] * len(graph)

    stack = [start]

    while len(stack) > 0:
        node = stack.pop()
        if not marked[node]:
            marked[node] = True
            dfs_order.append(node)
        
        for neighbour in graph[node].neighbors:
            neighbour_node = int(neighbour.char)
            if not marked[neighbour_node]:
                edge_to[neighbour_node] = node
                stack.append(neighbour_node)
    
    print(dfs_order)

    dfs_full_order = []

    for i in range(len(dfs_order)  - 1):
        prev,curr = dfs_order[i], dfs_order[i+1]
        dfs_full_order.append(prev)
        dfs_full_order.append((edge_to[curr], curr))
    
    dfs_full_order.append(curr)
    print(dfs_full_order)
    return dfs_full_order