"""
Date: 11/27/2019
The main class which lets the user choose the algorithm
"""


import sys as system
from numpy import *
from src.Simplex.Simplex import Simplex
from src.Simplex.StandardForm import StandardForm
from src.FordFulkerson.GraphLibrary.Graph import Graph
from src.FordFulkerson.GraphLibrary.Vertex import Vertex
from src.FordFulkerson.GraphLibrary.DirectedEdge import DirectedEdge
from src.FordFulkerson.FordFulkersonAlgorithm import FordFulkersonAlgorithm
from src.FordFulkerson.GraphLibrary.VertexObj import VertexObj


# call the simplex algorithm
def call_simplex():
    simplex = Simplex()
    A = array([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [-1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, -1, 1, 0, 0, 1, -1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, -1, 0, 0, -1, 1, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, 0, -1, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 1, -1, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -1, 1, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, -1, 1]
    ])

    b = array([
        [10.0],
        [9.0],
        [10.0],
        [4.0],
        [15.0],
        [15.0],
        [5.0],
        [8.0],
        [10.0],
        [15.0],
        [4.0],
        [6.0],
        [15.0],
        [10.0],
        [16.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0],
        [0.0]
    ])
    c = array([1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0])
    standard_form = StandardForm(A, b, c)
    simplex.simplex(standard_form)


# call the ford_fulkerson algorithm
def call_ford_fulkerson():
    # initialize the graph
    d_graph = initialize_graph()
    ford_fulkerson = FordFulkersonAlgorithm(d_graph)
    d_graph = ford_fulkerson.get_max_flow()
    max_flow_value = 0
    vertex_s = d_graph.get_vertex_by_label('s')
    for edge in d_graph.get_outgoing_edges(vertex_s):
        max_flow_value = max_flow_value + edge.weight
    print("max flow is: ", max_flow_value)
    for edge in d_graph.get_edges():
        print(edge.from_vertex.label, "->", edge.to_vertex.label, ":", edge.weight)


# initialize the graph
def initialize_graph() -> Graph:
    # initialize the graph
    d_graph = Graph(True)

    # build 8 vertices
    vertex_s = Vertex('s', VertexObj(['s'], None))
    vertex_t = Vertex('t', VertexObj(['t'], None))
    vertex_A = Vertex('A', VertexObj(['A'], None))
    vertex_B = Vertex('B', VertexObj(['B'], None))
    vertex_C = Vertex('C', VertexObj(['C'], None))
    vertex_D = Vertex('D', VertexObj(['D'], None))
    vertex_E = Vertex('E', VertexObj(['E'], None))
    vertex_F = Vertex('F', VertexObj(['F'], None))

    # add the vertices into the graph
    d_graph.insert_vertex(vertex_s)
    d_graph.insert_vertex(vertex_t)
    d_graph.insert_vertex(vertex_A)
    d_graph.insert_vertex(vertex_B)
    d_graph.insert_vertex(vertex_C)
    d_graph.insert_vertex(vertex_D)
    d_graph.insert_vertex(vertex_E)
    d_graph.insert_vertex(vertex_F)

    # build 15 directed edges. The weight is the current f. The obj is the capacity
    x1 = DirectedEdge(vertex_s, vertex_A, 'x1', 0.0)
    x1.obj = 10.0

    x2 = DirectedEdge(vertex_A, vertex_B, 'x2', 0.0)
    x2.obj = 9.0

    x3 = DirectedEdge(vertex_B, vertex_t, 'x3', 0.0)
    x3.obj = 10.0

    x4 = DirectedEdge(vertex_A, vertex_C, 'x4', 0.0)
    x4.obj = 4.0

    x5 = DirectedEdge(vertex_A, vertex_D, 'x5', 0.0)
    x5.obj = 15.0

    x6 = DirectedEdge(vertex_B, vertex_D, 'x6', 0.0)
    x6.obj = 15.0

    x7 = DirectedEdge(vertex_s, vertex_C, 'x7', 0.0)
    x7.obj = 5.0

    x8 = DirectedEdge(vertex_C, vertex_D, 'x8', 0.0)
    x8.obj = 8.0

    x9 = DirectedEdge(vertex_D, vertex_t, 'x9', 0.0)
    x9.obj = 10.0

    x10 = DirectedEdge(vertex_s, vertex_E, 'x10', 0.0)
    x10.obj = 15.0

    x11 = DirectedEdge(vertex_C, vertex_E, 'x11', 0.0)
    x11.obj = 4.0

    x12 = DirectedEdge(vertex_F, vertex_C, 'x12', 0.0)
    x12.obj = 6.0

    x13 = DirectedEdge(vertex_D, vertex_F, 'x13', 0.0)
    x13.obj = 15.0

    x14 = DirectedEdge(vertex_F, vertex_t, 'x14', 0.0)
    x14.obj = 10.0

    x15 = DirectedEdge(vertex_E, vertex_F, 'x15', 0.0)
    x15.obj = 16.0

    # add the edges into the graph
    d_graph.insert_directed_edge(x1.get_from_vertex(), x1.get_to_vertex(), x1)
    d_graph.insert_directed_edge(x2.get_from_vertex(), x2.get_to_vertex(), x2)
    d_graph.insert_directed_edge(x3.get_from_vertex(), x3.get_to_vertex(), x3)
    d_graph.insert_directed_edge(x4.get_from_vertex(), x4.get_to_vertex(), x4)
    d_graph.insert_directed_edge(x5.get_from_vertex(), x5.get_to_vertex(), x5)
    d_graph.insert_directed_edge(x6.get_from_vertex(), x6.get_to_vertex(), x6)
    d_graph.insert_directed_edge(x7.get_from_vertex(), x7.get_to_vertex(), x7)
    d_graph.insert_directed_edge(x8.get_from_vertex(), x8.get_to_vertex(), x8)
    d_graph.insert_directed_edge(x9.get_from_vertex(), x9.get_to_vertex(), x9)
    d_graph.insert_directed_edge(x10.get_from_vertex(), x10.get_to_vertex(), x10)
    d_graph.insert_directed_edge(x11.get_from_vertex(), x11.get_to_vertex(), x11)
    d_graph.insert_directed_edge(x12.get_from_vertex(), x12.get_to_vertex(), x12)
    d_graph.insert_directed_edge(x13.get_from_vertex(), x13.get_to_vertex(), x13)
    d_graph.insert_directed_edge(x14.get_from_vertex(), x14.get_to_vertex(), x14)
    d_graph.insert_directed_edge(x15.get_from_vertex(), x15.get_to_vertex(), x15)

    return d_graph


# the main method
def main(argv):
    if len(argv) < 2:
        print("Incorrect argument number")
        return
    if argv[1] == "simplex":
        call_simplex()
    elif argv[1] == "Ford-Fulkerson":
        call_ford_fulkerson()
    else:
        print("Incorrect argument")


if __name__ == "__main__":
    main(system.argv)
