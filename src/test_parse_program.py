import pytest

import node
from node import Node
from parse_program import parse_operator, parse_operator_list, parse_block, parse_program


@pytest.fixture
def reset_position():
    node.position = 0
    yield
    node.position = 0


@pytest.fixture
def create_tree():
    return Node("root")


def test_parse_operator_success(reset_position, create_tree):
    tree = create_tree
    lexemes = ["x", ":=", "10"]
    result = parse_operator(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<оператор>"


def test_parse_operator_success_with_semicolon(reset_position, create_tree):
    tree = create_tree
    lexemes = ["x", ":=", "10", ";"]
    result = parse_operator(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<оператор>"


def test_parse_operator_failure(reset_position, create_tree):
    tree = create_tree
    lexemes = ["x", ":=", "="]
    result = parse_operator(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0


def test_parse_operator_list_success(reset_position, create_tree):
    tree = create_tree
    lexemes = ["x", ":=", "10", ";", "y", ":=", "20"]
    result = parse_operator_list(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<список операторов>"


def test_parse_operator_list_failure(reset_position, create_tree):
    tree = create_tree
    lexemes = ["x", ":=", "10", ";", ":=", "20"]
    result = parse_operator_list(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0


def test_parse_block_success(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin", "x", ":=", "10", "end"]
    result = parse_block(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<блок>"


def test_parse_block_failure(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin", ":=", "10", "end"]
    result = parse_block(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0


def test_parse_program_success(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin", "x", ":=", "10", "end"]
    result = parse_program(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<программа>"


def test_parse_program_success_with_semicolon(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin", "x", ":=", "10", ";", "end"]
    result = parse_program(tree, lexemes)
    assert result is True
    assert len(tree.children) == 1
    assert tree.children[0].value == "<программа>"


def test_parse_program_failure(reset_position, create_tree):
    tree = create_tree
    lexemes = ["begin", ":=", "10", "end"]
    result = parse_program(tree, lexemes)
    assert result is False
    assert len(tree.children) == 0
