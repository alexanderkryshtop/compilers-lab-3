from node import Node
from node import parse_lex
from parse_grammar import parse_identifier
from parse_grammar import parse_expression


def parse_operator(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<оператор>")
    if parse_identifier(new_node, lexemes):
        if parse_lex(new_node, lexemes, ':='):
            if parse_expression(new_node, lexemes):
                tree.children.append(new_node)
                return True

    return False


def parse_operator_list_prime(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<список операторов’>")
    if parse_lex(new_node, lexemes, ';'):
        if parse_operator(new_node, lexemes):
            if parse_operator_list_prime(new_node, lexemes):
                tree.children.append(new_node)
                return True
        return False

    return True


def parse_operator_list(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<список операторов>")
    if parse_operator(new_node, lexemes):
        if parse_operator_list_prime(new_node, lexemes):
            tree.children.append(new_node)
            return True

    return False


def parse_block(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<блок>")
    if parse_lex(new_node, lexemes, 'begin'):
        if parse_operator_list(new_node, lexemes):
            if parse_lex(new_node, lexemes, 'end'):
                tree.children.append(new_node)
                return True

    return False


def parse_program(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<программа>")
    if parse_block(new_node, lexemes):
        tree.children.append(new_node)
        return True

    return False
