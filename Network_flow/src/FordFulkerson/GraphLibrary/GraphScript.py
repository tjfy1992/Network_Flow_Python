"""
Date: 10/08/2019
A script for building am example graph.
"""

from src.FordFulkerson.GraphLibrary.Graph import Graph
from src.FordFulkerson.GraphLibrary.Vertex import Vertex
from src.FordFulkerson.GraphLibrary.DirectedEdge import DirectedEdge
from src.FordFulkerson.GraphLibrary.UndirectedEdge import UndirectedEdge


# build an undirected graph. This graph is same as the one on page 5 of slides "IntroductionToGraphs"
def build_undirected_graph():
    print("/-------------------undirected graph starts---------------------/")
    u_graph = Graph(False)

    # build 6 vertices
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    x = Vertex('x')
    y = Vertex('y')
    z = Vertex('z')

    # add the vertices into the graph
    u_graph.insert_vertex(u)
    u_graph.insert_vertex(v)
    u_graph.insert_vertex(w)
    u_graph.insert_vertex(x)
    u_graph.insert_vertex(y)
    u_graph.insert_vertex(z)

    # build 8 undirected edges
    a = UndirectedEdge(u, v, 'a')
    b = UndirectedEdge(v, x, 'b')
    c = UndirectedEdge(u, w, 'c')
    d = UndirectedEdge(v, w, 'd')
    e = UndirectedEdge(w, x, 'e')
    f = UndirectedEdge(w, y, 'f')
    g = UndirectedEdge(x, y, 'g')
    h = UndirectedEdge(x, z, 'h')

    # add the edges into the graph
    u_graph.insert_undirected_edge(a.get_vertex_1(), a.get_vertex_2(), a)
    u_graph.insert_undirected_edge(b.get_vertex_1(), b.get_vertex_2(), b)
    u_graph.insert_undirected_edge(c.get_vertex_1(), c.get_vertex_2(), c)
    u_graph.insert_undirected_edge(d.get_vertex_1(), d.get_vertex_2(), d)
    u_graph.insert_undirected_edge(e.get_vertex_1(), e.get_vertex_2(), e)
    u_graph.insert_undirected_edge(f.get_vertex_1(), f.get_vertex_2(), f)
    u_graph.insert_undirected_edge(g.get_vertex_1(), g.get_vertex_2(), g)
    u_graph.insert_undirected_edge(h.get_vertex_1(), h.get_vertex_2(), h)

    # get the number of vertices
    print("number of vertices: ", u_graph.get_vertices_number())

    # get all vertices and print out their labels
    vertices = u_graph.get_vertices()
    for vertex in vertices:
        print(vertex.label, end=" ")
    print()

    # get the number of edges
    print("number of edges: ", u_graph.get_edges_number())

    # get all edges and print out their end vertices
    edges = u_graph.get_edges()
    for edge in edges:
        print(edge.label, ":", "vertex1:", edge.get_vertex_1().label, ", vertex2:", edge.get_vertex_2().label)

    # print the degree of edge w.
    print("degree of edge w is:", u_graph.get_degree(w))

    # print whether edge b is directed.
    print("edge b is directed?", u_graph.is_directed_edge(b))

    # get vertex x's all adjacent vertices and print their labels out
    adjacent_vertices = u_graph.get_adjacent_vertices(x)
    print("x's adjacent vertices:", end=" ")
    for vertex in adjacent_vertices:
        print(vertex.label, end=" ")
    print()

    # get vertex v's all incident edges and print their labels out
    incident_edges = u_graph.get_incident_edges(v)
    print("v's incident edges:", end=" ")
    for edge in incident_edges:
        print(edge.label, end=" ")
    print()

    # print the two end vertices of edge a
    t = u_graph.get_end_vertices(a)
    print("edge a's end vertices:", t[0].label, t[1].label)

    # print whether u and v are adjacent
    print("vertex u and v are adjacent?", u_graph.are_adjacent(u, v))

    # get vertex u by it's label
    print("got vertex u by its label:", u_graph.get_vertex_by_label('u') == u)

    print("/-------------------undirected graph ends-----------------------/")


# build a directed graph. This graph is same as the one on page 16 of slides "GreedyGraphAlgorithms"
def build_directed_graph():
    print("/---------------------directed graph starts---------------------/")
    d_graph = Graph(True)

    # build 6 vertices
    s = Vertex('s')
    t = Vertex('t')
    u = Vertex('u')
    v = Vertex('v')
    w = Vertex('w')
    z = Vertex('z')

    # add the vertices into the graph
    d_graph.insert_vertex(s)
    d_graph.insert_vertex(t)
    d_graph.insert_vertex(u)
    d_graph.insert_vertex(v)
    d_graph.insert_vertex(w)
    d_graph.insert_vertex(z)

    # build 10 directed edges. The weight is the capacity.
    a = DirectedEdge(s, v, 'a', 6)
    b = DirectedEdge(s, w, 'b', 3)
    c = DirectedEdge(s, u, 'c', 5)
    d = DirectedEdge(v, t, 'd', 3)
    e = DirectedEdge(v, w, 'e', 1)
    f = DirectedEdge(u, w, 'f', 1)
    g = DirectedEdge(u, z, 'g', 2)
    h = DirectedEdge(w, t, 'h', 7)
    i = DirectedEdge(w, z, 'i', 9)
    j = DirectedEdge(z, t, 'j', 5)

    # add the edges into the graph
    d_graph.insert_directed_edge(a.get_from_vertex(), a.get_to_vertex(), a)
    d_graph.insert_directed_edge(b.get_from_vertex(), b.get_to_vertex(), b)
    d_graph.insert_directed_edge(c.get_from_vertex(), c.get_to_vertex(), c)
    d_graph.insert_directed_edge(d.get_from_vertex(), d.get_to_vertex(), d)
    d_graph.insert_directed_edge(e.get_from_vertex(), e.get_to_vertex(), e)
    d_graph.insert_directed_edge(f.get_from_vertex(), f.get_to_vertex(), f)
    d_graph.insert_directed_edge(g.get_from_vertex(), g.get_to_vertex(), g)
    d_graph.insert_directed_edge(h.get_from_vertex(), h.get_to_vertex(), h)
    d_graph.insert_directed_edge(i.get_from_vertex(), i.get_to_vertex(), i)
    d_graph.insert_directed_edge(j.get_from_vertex(), j.get_to_vertex(), j)

    # print the origin vertex and destination vertex's label of edge a
    print("edge a's origin vertex:", a.get_from_vertex().label, "destination vertex:", a.get_to_vertex().label)

    # print edge a's weight
    print("edge a's weight:", a.weight)

    # print vertex w's incoming edges' labels, origin vertex and destination vertex
    print("vertex w's incoming edges:")
    w_incoming_edges = d_graph.get_incoming_edges(w)
    for edge in w_incoming_edges:
        print(edge.label, ":", edge.get_from_vertex().label, "->", edge.get_to_vertex().label)
    print()

    # print vertex w's outgoing edges' labels, origin vertex and destination vertex
    print("vertex w's outgoing edges:")
    w_outgoing_edges = d_graph.get_outgoing_edges(w)
    for edge in w_outgoing_edges:
        print(edge.label, ":", edge.get_from_vertex().label, "->", edge.get_to_vertex().label)
    print()

    # print vertex v's incident edges
    print("vertex v's incident edges:")
    v_incident_edges = d_graph.get_incident_edges(v)
    for edge in v_incident_edges:
        print(edge.label, ":", edge.get_from_vertex().label, "->", edge.get_to_vertex().label)
    print()

    # print the degree and in-degree of v
    print("vertex v's degree:", d_graph.get_degree(v))
    print("vertex v's in-degree:", d_graph.get_in_degree(v))

    # remove the edge from z to t
    # z and t are adjacent before removing
    print("z and t are adjacent?", d_graph.are_adjacent(z, t))
    d_graph.remove_directed_edge(j)
    # z and t are no longer adjacent before removing
    print("z and t are adjacent?", d_graph.are_adjacent(z, t))
    # edge z -> t is no longer in z's incident edges
    z_incident_edges = d_graph.get_incident_edges(z)
    for edge in z_incident_edges:
        print(edge.label, ":", edge.get_from_vertex().label, "->", edge.get_to_vertex().label)
    print()

    # remove vertex w
    d_graph.remove_vertex(w)
    print("w is in graph?", d_graph.get_vertex_by_label('w'))
    # print all the edges in the graph
    all_edges = d_graph.get_edges()
    # all edges with end w are removed from the graph
    print("existed edges in graph:")
    for edge in all_edges:
        print(edge.get_from_vertex().label, "->", edge.get_to_vertex().label)

    print("/---------------------directed graph ends-----------------------/")


if __name__ == "__main__":
    build_undirected_graph()
    print()
    build_directed_graph()
