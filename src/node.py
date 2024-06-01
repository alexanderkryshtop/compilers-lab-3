from graphviz import Digraph

from typing_extensions import Self
from typing import Any

position = 0


class Node:
    def __init__(self, data: Any):
        self.value = data
        self.children = []

    def build_graphviz(self, tree: Self = None, parent_value: str = "", identifier: str = "main"):
        if not tree:
            tree = Digraph()
            tree.node_attr["shape"] = "plain"

        tree.node(identifier, str(self.value))
        if parent_value:
            tree.edge(parent_value, identifier)

        for i, child in enumerate(self.children):
            child.build_graphviz(tree, identifier, identifier + "." + str(i))

        return tree


def parse_lex(tree: Node, lexemes: list[str], lex: str) -> bool:
    global position
    if position >= len(lexemes):
        return False

    if lexemes[position] == lex:
        tree.children.append(Node(lex))
        position += 1
        return True

    return False
