import node
from node import Node
from parse_program import parse_program
from split import tokenize

code = '''
begin
    a := 42;
    b := a + 4;
    c := b - 90
end
'''

tokens = tokenize(code)
print(tokens)

tree = Node("root")
if not parse_program(tree, tokens) or node.position != len(tokens):
    raise RuntimeError("parsing error")

graph = tree.build_graphviz()
graph.render("tree", format="png", view=True)
