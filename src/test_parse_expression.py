import pytest
import node
from node import Node
from parse_grammar import parse_expression


@pytest.fixture
def reset_position():
    node.position = 0
    yield
    node.position = 0


@pytest.fixture
def create_tree():
    return Node("root")


def test_parse_expression_simple_arithmetic(reset_position, create_tree):
    tree = create_tree
    lexemes = ["3", "+", "2"]
    result = parse_expression(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<выражение>"


def test_parse_expression_with_relation(reset_position, create_tree):
    tree = create_tree
    lexemes = ["3", "+", "2", ">", "1"]
    result = parse_expression(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<выражение>"


def test_parse_expression_invalid_expression(reset_position, create_tree):
    tree = create_tree
    lexemes = ["3", "+"]
    result = parse_expression(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0


def test_parse_expression_empty_lexemes(reset_position, create_tree):
    tree = create_tree
    lexemes = []
    result = parse_expression(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0


def test_parse_expression_relation_only(reset_position, create_tree):
    tree = create_tree
    lexemes = ["<", "2"]
    result = parse_expression(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0
