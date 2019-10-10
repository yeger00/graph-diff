#!/usr/bin/env python
import sys
import pydot
import argparse
from . import graphdiff
from . import __version__ as version

def load_graph(path):
    '''
    Loads a graph from .dot file into a Graph() object.
    '''
    with open(path) as f:
        data = f.read()
    graph = graphdiff.Graph()
    if data:
        # TODO: handle multiple graphs
        pydot_graph = pydot.graph_from_dot_data(data)[0]
        graph = graphdiff.from_dot(pydot_graph) 
    return graph


def save_graph(graph, path):
    pydot_graph = graphdiff.to_dot(graph)
    pydot_graph.write_raw(path)


def print_graph(graph):
    pydot_graph = graphdiff.to_dot(graph)
    print(pydot_graph.to_string())


def main():
    parser = argparse.ArgumentParser(description='graph-diff')
    parser.add_argument('--version', action='version', version=version.__version__)
    parser.add_argument('before', action='store')
    parser.add_argument('after', action='store')
    args = parser.parse_args()

    before_graph = load_graph(args.before)
    after_graph = load_graph(args.after)
    diff = graphdiff.generate_diff_graph(before_graph, after_graph)
    print_graph(diff)


if __name__ == "__main__":
    main()
