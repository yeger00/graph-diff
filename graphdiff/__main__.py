#!/usr/bin/env python
import sys
import pydot
import graphdiff


def load_graph(path):
    '''
    Loads a graph from .dot file into a Graph() object.
    '''
    pydot_graph = pydot.graph_from_dot_file(path)[0]
    return graphdiff.from_dot(pydot_graph) 


def save_graph(graph, path):
    pydot_graph = graphdiff.to_dot(graph)
    pydot_graph.write_raw(path)


def print_graph(graph):
    pydot_graph = graphdiff.to_dot(graph)
    print(pydot_graph.to_string())


def main():
    before_graph = load_graph(sys.argv[1])
    after_graph = load_graph(sys.argv[2])
    diff = graphdiff.generate_diff_graph(before_graph, after_graph)
    save_graph(diff, sys.argv[3])
    # print_graph(diff)


if __name__ == "__main__":
    main()
