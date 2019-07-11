#!/usr/bin/env python
"""
This module generates a diff between two graphs.
"""

import pydot


class Edge(object):
    """
    Represent an edge in the graph.
    """

    def __init__(self, src, dest, label=None):
        self.src = src
        self.dest = dest
        if not label:
            self.label = ""
        else:
            self.label = label

    def __eq__(self, other):
        return self.src == other.src and self.dest == other.dest and self.label == self.label

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "(" + self.src + ", " + self.dest + ")"

    def __hash__(self):
        return hash((self.src, self.dest, self.label))


class Graph(object):
    """
    Represents a graph.
    """

    def __init__(self, edges=None, nodes=None):
        if not edges:
            self.edges = set()
        else:
            self.edges = edges
        if not nodes:
            self.nodes = set()
        else:
            self.nodes = nodes

    def add_edge(self, edge):
        """Adds an edge to the graph."""
        self.edges.add(edge)

    def clear_edges(self):
        """Clears all the edges from the graph."""
        self.edges = set()

    def add_node(self, node):
        """Adds a node to graph."""
        self.nodes.add(node)

    def clear_nodes(self):
        """Clears all the nodes from the graph."""
        self.nodes = set()


def generate_diff_graph(first_graph, second_graph):
    """Generates diff from two graph."""
    # generate nodes
    removed_nodes = set(first_graph.nodes) - set(second_graph.nodes)
    added_nodes = set(second_graph.nodes) - set(first_graph.nodes)
    nodes = set(second_graph.nodes) & set(first_graph.nodes)

    removed_edges = first_graph.edges - second_graph.edges
    for removed_edge in removed_edges:
        if removed_edge.src in removed_nodes:
            removed_edge.src = "-" + removed_edge.src
        if removed_edge.dest in removed_nodes:
            removed_edge.dest = "-" + removed_edge.dest

    added_edges = second_graph.edges - first_graph.edges
    for added_edge in added_edges:
        if added_edge.src in added_nodes:
            added_edge.src = "+" + added_edge.src
        if added_edge.dest in added_nodes:
            added_edge.dest = "+" + added_edge.dest
    edges = second_graph.edges & first_graph.edges

    graph = Graph()
    for removed_node in removed_nodes:
        graph.nodes.add("-" + removed_node)
    for added_node in added_nodes:
        graph.nodes.add("+" + added_node)
    for node in nodes:
        graph.nodes.add(node)

    for removed_edge in removed_edges:
        graph.edges.add(Edge(removed_edge.src, removed_edge.dest, "-" + removed_edge.label))
    for added_edge in added_edges:
        graph.edges.add(Edge(added_edge.src, added_edge.dest, "+" + added_edge.label))
    for edge in edges:
        graph.edges.add(edge)

    return graph


def remove_quotes(pydot_graph):
    """ For some reason, some pydot graph data is with quotes ('"name"', '"label"').
    This function removes it."""

    for node in pydot_graph.get_nodes():
        node.set_label(node.get_label().replace('"', ''))

    for edge in pydot_graph.get_edges():
        if edge.get_label():
            edge.set_label(edge.get_label().replace('"', ''))

def from_dot(pydot_graph):
    """Generated a graph from pydot graph."""
    remove_quotes(pydot_graph)
    graph = Graph()

    for node in pydot_graph.get_nodes():
        graph.nodes.add(node.get_label())

    for edge in pydot_graph.get_edges():
        source_label = edge.get_source()
        source_nodes = pydot_graph.get_node(source_label)
        if source_nodes:
            source_label = source_nodes[0].get_label()
        dest_label = edge.get_destination()
        dest_nodes = pydot_graph.get_node(dest_label)
        if dest_nodes:
            dest_label = dest_nodes[0].get_label()
        graph.edges.add(Edge(source_label, dest_label, edge.get_label()))
        graph.nodes.add(source_label)
        graph.nodes.add(dest_label)
    return graph


def to_dot(graph):
    """Generated a pydot graph from graph."""
    pydot_graph = pydot.Dot(graph_type='graph')
    for edge in graph.edges:
        pydot_graph.add_edge(pydot.Edge(edge.src, edge.dest, label=edge.label))
    for node in graph.nodes:
        pydot_graph.add_node(pydot.Node(node))
    return pydot_graph
