import pytest

import node
from node import Node
from node import parse_lex


@pytest.fixture
def reset_position():
    node.position = 0
    yield
    node.position = 0


@pytest.fixture
def create_tree():
    return Node("root")


def test_parse_lex_success_single(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin"]
    assert parse_lex(tree, lexemes, "begin") is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "begin"


def test_parse_lex_success_multiple(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin", "end"]
    assert parse_lex(tree, lexemes, "begin") is True
    assert parse_lex(tree, lexemes, "end") is True
    assert len(tree.children) == 2
    assert tree.children[0].value == "begin"
    assert tree.children[1].value == "end"


def test_parse_lex_failure(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin"]
    assert parse_lex(tree, lexemes, "end") is False
    assert len(tree.children) == 0


def test_parse_lex_position_out_of_bounds(reset_position, create_tree):
    tree = create_tree
    lexemes = []
    assert parse_lex(tree, lexemes, "begin") is False
    assert len(tree.children) == 0
