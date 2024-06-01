import node
from node import Node
from node import parse_lex


def parse_operation_type_multiplication(tree: Node, lexemes: list[str]) -> bool:
    if node.position >= len(lexemes):
        return False

    if lexemes[node.position] in ['*', '/']:
        new_node = Node("<операция типа умножения>")
        new_node.children.append(Node(lexemes[node.position]))
        tree.children.append(new_node)
        node.position += 1
        return True
    return False


def parse_operation_type_addition(tree: Node, lexemes: list[str]) -> bool:
    if node.position >= len(lexemes):
        return False

    if lexemes[node.position] in ['+', '-']:
        new_node = Node("<операция типа сложения>")
        new_node.children.append(Node(lexemes[node.position]))
        tree.children.append(new_node)
        node.position += 1
        return True
    return False


def parse_operation_relation(tree: Node, lexemes: list[str]) -> bool:
    if node.position >= len(lexemes):
        return False

    if lexemes[node.position] in ['<', '<=', '=', '<>', '>', '>=']:
        new_node = Node("<операция отношения>")
        new_node.children.append(Node(lexemes[node.position]))
        tree.children.append(new_node)
        node.position += 1
        return True
    return False


def parse_identifier(tree: Node, lexemes: list[str]) -> bool:
    if node.position >= len(lexemes):
        return False

    if lexemes[node.position].isalpha() and lexemes[node.position] not in ['begin', 'end']:
        new_node = Node("<идентификатор>")
        new_node.children.append(Node(lexemes[node.position]))
        tree.children.append(new_node)
        node.position += 1
        return True
    return False


def parse_const(tree: Node, lexemes: list[str]) -> bool:
    if node.position >= len(lexemes):
        return False

    try:
        value = int(lexemes[node.position])
    except:
        try:
            value = float(lexemes[node.position])
        except:
            return False

    new_node = Node("<константа>")
    new_node.children.append(Node(value))
    tree.children.append(new_node)
    node.position += 1
    return True


def parse_factor(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<фактор>")
    if parse_identifier(new_node, lexemes):
        tree.children.append(new_node)
        return True
    elif parse_const(new_node, lexemes):
        tree.children.append(new_node)
        return True
    elif parse_lex(new_node, lexemes, '('):
        if parse_arithmetic_expression(new_node, lexemes):
            if parse_lex(new_node, lexemes, ')'):
                tree.children.append(new_node)
                return True

    return False


def parse_therm_prime(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<терм’>")
    if parse_operation_type_multiplication(new_node, lexemes):
        if parse_factor(new_node, lexemes):
            if parse_therm_prime(new_node, lexemes):
                tree.children.append(new_node)
                return True

        return False

    return True


def parse_therm(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<терм>")
    if parse_factor(new_node, lexemes):
        if parse_therm_prime(new_node, lexemes):
            tree.children.append(new_node)
            return True

    return False


def parse_arithmetic_expression_prime(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<арифметическое выражение’>")
    if parse_operation_type_addition(new_node, lexemes):
        if parse_therm(new_node, lexemes):
            if parse_arithmetic_expression_prime(new_node, lexemes):
                tree.children.append(new_node)
                return True
        return False

    return True


def parse_arithmetic_expression(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<арифметическое выражение>")
    if parse_therm(new_node, lexemes):
        if parse_arithmetic_expression_prime(new_node, lexemes):
            tree.children.append(new_node)
            return True

    return False


def parse_expression(tree: Node, lexemes: list[str]) -> bool:
    new_node = Node("<выражение>")
    if parse_arithmetic_expression(new_node, lexemes):
        if parse_operation_relation(new_node, lexemes):
            if parse_arithmetic_expression(new_node, lexemes):
                tree.children.append(new_node)
                return True
            # else:
            return False

        tree.children.append(new_node)
        return True

    return False
