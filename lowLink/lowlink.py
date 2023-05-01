from manim import *

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

    def connectTilted(self,other, ugao):
        line_center = Line(self.center, other.center)
        unit_vector = line_center.get_unit_vector()
        start,end = line_center.get_start_and_end()
        new_start = start + unit_vector* self.radius 
        new_end = end - unit_vector * self.radius
        line = Line(new_start,new_end, path_arc= ugao)
        self.neighbors.append(other)
        other.neighbors.append(self)
        self.edges.append(line)
        other.edges.append(line)
        return line


    def connectTilted1(self,other, ugao):
        line_center = Line(self.center, other.center)
        unit_vector = line_center.get_unit_vector()
        start,end = line_center.get_start_and_end()
        new_start = start + unit_vector* self.radius  + LEFT*0.25 + UP * 0.5
        new_end = end - unit_vector * self.radius + LEFT * 0.5 + DOWN *0.2
        line = Line(new_start,new_end, path_arc= ugao)
        self.neighbors.append(other)
        other.neighbors.append(self)
        self.edges.append(line)
        other.edges.append(line)
        return line

    def connectTilted2(self,other, ugao):
        line_center = Line(self.center, other.center)
        unit_vector = line_center.get_unit_vector()
        start,end = line_center.get_start_and_end()
        new_start = start + unit_vector* self.radius + RIGHT * 0.21 + UP* 0.5
        new_end = end - unit_vector * self.radius + RIGHT * 0.475 + DOWN * 0.1
        line = Line(new_start,new_end, path_arc= ugao)
        self.neighbors.append(other)
        other.neighbors.append(self)
        self.edges.append(line)
        other.edges.append(line)
        return line

class animation(Scene):
    
    def construct(self):
        self.show_animation()

    
    def show_animation(self):

        title = Tex("Low link animation")
        title.scale(1.2)
        title.move_to(UP*3.5)
        linija = Line(LEFT,RIGHT)
        linija.next_to(title,DOWN).scale(7)


        graph, edge_dict = self.create_graph()
        nodes, edges = self.make_graph_mobject(graph,edge_dict)


        print(graph)
        print(edge_dict)

        entire_graph = VGroup(nodes,edges)

        self.play(
            Write(title),
            Create(linija, run_time =2)
        )

        self.play(
            Write(entire_graph),
            run_time = 3
        )

        node = graph[0]
        surround_circle_a = Circle(radius = node.circle.radius)
        surround_circle_a.move_to(node.circle.get_center())
        surround_circle_a.set_stroke(width=8)
        surround_circle_a.set_color(GREEN)
        surround_circle_a.set_fill(opacity=0)
        tekst_a = Tex("1/1")
        tekst_a.scale(0.75)
        tekst_a.next_to(surround_circle_a, LEFT)

        self.play(
            Create(surround_circle_a),
            run_time = 1,
        )

        self.play(
            Write(tekst_a)
        )

        edge = edge_dict[('a', 'b')]
        line1 = Line(edge.get_start(), edge.get_end())
        line1.set_stroke(width=16)
        line1.set_color(GREEN)

        self.play(
                Create(line1),
                run_time = 1
            )
        
        node = graph[1]
        surround_circle_b= Circle(radius = node.circle.radius)
        surround_circle_b.move_to(node.circle.get_center())
        surround_circle_b.set_stroke(width=8)
        surround_circle_b.set_color(GREEN)
        surround_circle_b.set_fill(opacity=0)
        self.play(
            Create(surround_circle_b)
        )


        tekst_b = Tex("2", "/", "2")
        tekst_b.scale(0.75)
        tekst_b.next_to(surround_circle_b, UL * 0.5)

        self.play(
            Write(tekst_b)
        )
        
        edge = edge_dict[('b', 'c')]
        line2 = Line(edge.get_start(), edge.get_end())
        line2.set_stroke(width=16)
        line2.set_color(GREEN)

        self.play(
            Create(line2)
        )

        node = graph[3]
        surround_circle_c= Circle(radius = node.circle.radius)
        surround_circle_c.move_to(node.circle.get_center())
        surround_circle_c.set_stroke(width=8)
        surround_circle_c.set_color(GREEN)
        surround_circle_c.set_fill(opacity=0)
        

        self.play(
            Create(surround_circle_c)
        )

        tekst_c = Tex(r"3",r"/",r"3")
        tekst_c.scale(0.75)
        tekst_c.next_to(surround_circle_c, LEFT *0.5)

        self.play(
            Write(tekst_c)
        )

        edge = edge_dict[('c', 'e')]
        line3 = Line(edge.get_start(), edge.get_end())
        line3.set_stroke(width=16)
        line3.set_color(GREEN)

        self.play(
            Create(line3)
        )

        node = graph[4]
        surround_circle_e= Circle(radius = node.circle.radius)
        surround_circle_e.move_to(node.circle.get_center())
        surround_circle_e.set_stroke(width=8)
        surround_circle_e.set_color(GREEN)
        surround_circle_e.set_fill(opacity=0)
        

        self.play(
            Create(surround_circle_e)
        )

        tekst_e = Tex(r"4",r"/",r"4")
        tekst_e.scale(0.75)
        tekst_e.next_to(surround_circle_e, LEFT)

        self.play(
            Write(tekst_e)
        )

        edge = edge_dict[('b', 'e')]
        line4 = Line(edge.get_end(),edge.get_start(), path_arc= -PI/1.1)
        line4.set_stroke(width=16)
        line4.set_color(GREEN)

        self.play(
            Create(line4)
        )
        
        self.highlight_node_red(graph,4)

        new_tekst_e = Tex("2").move_to(tekst_e[2].get_right(), RIGHT)
        new_tekst_e.scale(0.75)


        self.play(
            ReplacementTransform(tekst_e[2], new_tekst_e),
            run_time =1 
        )

        self.highlight_node_red(graph,3)
        
        new_tekst_c = Tex("2").move_to(tekst_c[2].get_right(), RIGHT)
        new_tekst_c.scale(0.75)
        self.play(
            ReplacementTransform(tekst_c[2], new_tekst_c)
        )


        # self.highlight_node_red(graph,1)

        edge = edge_dict[('b', 'd')]
        line5 = Line(edge.get_start(),edge.get_end())
        line5.set_stroke(width=16)
        line5.set_color(GREEN)

        self.play(
            Create(line5)
        )

        node = graph[5]
        surround_circle_d= Circle(radius = node.circle.radius)
        surround_circle_d.move_to(node.circle.get_center())
        surround_circle_d.set_stroke(width=8)
        surround_circle_d.set_color(GREEN)
        surround_circle_d.set_fill(opacity=0)

        self.play(
            Create(surround_circle_d)
        )


        tekst_d = Tex(r"5",r"/",r"5")
        tekst_d.next_to(surround_circle_d, DOWN)
        tekst_d.scale(0.75)

        self.play(
            Write(tekst_d)
        )

        edge = edge_dict[('a', 'd')]
        line6 = Line(edge.get_end(),edge.get_start(), path_arc= PI/4)
        line6.set_stroke(width=16)
        line6.set_color(GREEN)

        self.play(
            Create(line6)
        )

        self.highlight_node_red(graph,5)

        new_tekst_d = Tex("1").move_to(tekst_d[2].get_right(), RIGHT)
        new_tekst_d.scale(0.75)
        self.play(
            ReplacementTransform(tekst_d[2], new_tekst_d)
        )


        self.highlight_node_red(graph,1)

        new_tekst_b = Tex("1").move_to(tekst_b[2].get_right(), RIGHT)
        new_tekst_b.scale(0.75)
        self.play(
            ReplacementTransform(tekst_b[2], new_tekst_b)
        )

        edge = edge_dict[('a', 'f')]
        line7 = Line(edge.get_start(),edge.get_end())
        line7.set_stroke(width=16)
        line7.set_color(GREEN)

        self.play(
            Create(line7)
        )

        surround_circle = self.highlight_node(graph,2)

        tekst_f = Tex("6", "/", "6")
        tekst_f.scale(0.75)
        tekst_f.next_to(surround_circle,UP)

        self.play(
            Write(tekst_f)
        )

        edge = edge_dict[('f', 'g')]
        line8 = Line(edge.get_start(),edge.get_end())
        line8.set_stroke(width=16)
        line8.set_color(GREEN)


        self.play(
            Create(line8)
        )
        
        surround_circle = self.highlight_node(graph,6)
        
        tekst_f = Tex("7", "/", "7")
        tekst_f.scale(0.75)
        tekst_f.next_to(surround_circle, DOWN)
        
        self.play(
            Write(tekst_f)
        )
        self.highlight_node_red(graph, 6)

        edge = edge_dict[('f', 'h')]
        line9 = Line(edge.get_start(),edge.get_end())
        line9.set_stroke(width=16)
        line9.set_color(GREEN)


        self.play(
            Create(line9)
        )

        surround_circle = self.highlight_node(graph,7)

        tekst_h = Tex("8", "/", "8")
        tekst_h.scale(0.75)
        tekst_h.next_to(surround_circle, RIGHT)
        self.play(
            Write(tekst_h)
        )



        edge = edge_dict[('h', 'i')]
        line9 = Line(edge.get_start(),edge.get_end())
        line9.set_stroke(width=16)
        line9.set_color(GREEN)


        self.play(
            Create(line9)
        )

        surround_circle= self.highlight_node(graph, 8)

        tekst_i = Tex("9","/", "9")
        tekst_i.scale(0.75)
        tekst_i.next_to(surround_circle, LEFT)
        self.play(
            Write(tekst_i)
        )


        edge = edge_dict[('f', 'i')]
        line10 = Line(edge.get_end(),edge.get_start(), path_arc=PI/1.1)
        line10.set_stroke(width=16)
        line10.set_color(GREEN)


        self.play(
            Create(line10)
        )

        self.highlight_node_red(graph,8)

        new_tekst_i = Tex("6").move_to(tekst_i[2].get_right(), RIGHT)
        new_tekst_i.scale(0.75)

        self.play(
            ReplacementTransform(tekst_i[2],new_tekst_i)
        )

        self.highlight_node_red(graph,7)

        new_tekst_h = Tex("6").move_to(tekst_h[2].get_right(), RIGHT)
        new_tekst_h.scale(0.75)

        self.play(
            ReplacementTransform(tekst_h[2], new_tekst_h)
        )

        self.highlight_node_red(graph,2)
        self.highlight_node_red(graph,0)

        self.wait(3)


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


    def create_graph(self):
        graph = []
        edges = {}

        radius,scale = 0.4, 0.9
        SHIFT =RIGHT * 2.5

        node_a = GraphNode('a', position= UP *2, radius=radius,scale=scale)
        node_b = GraphNode('b',position=UP*1 + LEFT*1.5, radius=radius, scale=scale)
        node_f = GraphNode('f', position=UP*1 + RIGHT * 2,radius=radius, scale=scale)
        node_c = GraphNode('c',position=LEFT*2.5 + DOWN, radius=radius,scale=scale)
        node_e = GraphNode('e', position=LEFT*3 + DOWN*3,radius=radius, scale=scale)
        node_d = GraphNode('d', position=DOWN + LEFT*0.5 , radius=radius, scale=scale)
        node_g = GraphNode('g', position= DOWN + RIGHT*1.5, radius=radius, scale=scale)
        node_h = GraphNode('h', position=DOWN + RIGHT*3.5, radius=radius, scale=scale)
        node_i = GraphNode('i',position=DOWN*3+ RIGHT *4, radius=radius, scale=scale)


        edges[('a', 'b')] = node_a.connect(node_b)
        edges[('a', 'f')] = node_a.connect(node_f)
        edges[('b', 'c')] = node_b.connect(node_c)
        edges[('c', 'e')] = node_c.connect(node_e)
        edges[('b', 'd')]= node_b.connect(node_d)
        edges[('f', 'g')] = node_f.connect(node_g)
        edges[('f', 'h')] = node_f.connect(node_h)
        edges[('h','i')] = node_h.connect(node_i)
        edges[('a', 'd')] = node_a.connectTilted(node_d, -PI/4)
        edges[('b', 'e')] = node_b.connectTilted1(node_e, PI/1.1)
        edges[('f', 'i')] = node_f.connectTilted2(node_i, -PI/1.1)

        graph.append(node_a)
        graph.append(node_b)
        graph.append(node_f)
        graph.append(node_c)
        graph.append(node_e)
        graph.append(node_d)
        graph.append(node_g)
        graph.append(node_h)
        graph.append(node_i)

        return graph,edges  

    def make_graph_mobject(self,graph, edge_dict, node_color = DARK_BLUE, stroke_color = BLUE, data_color = WHITE, edge_color = GRAY, scale_factor =1 , show_data = True):

        nodes = []
        edges = []

        for node in graph:
            node.circle.set_fill(color = node_color, opacity = 0.5)
            node.circle.set_stroke(color=stroke_color)
            node.data.set_color(color = data_color)

            nodes.append(VGroup(node.circle, node.data))

        for edge in edge_dict.values():
            edge.set_stroke(width = 7*scale_factor)
            edge.set_color(color = edge_color)
            edges.append(edge)
        

        return VGroup(*nodes), VGroup(*edges)