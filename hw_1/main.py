import ast
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

class Analyzer(ast.NodeVisitor):

    def __init__(self):
        self.graph = nx.Graph()
        self.labels = {}

    def visit_FunctionDef(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'func "{node.name}"'
        for el in node.body:
            self.graph.add_edge(node, self.visit(el))
        return node

    def visit_Assign(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'='
        for el in node.targets:
            self.graph.add_edge(node, self.visit(el))
        self.graph.add_edge(node, self.visit(node.value))
        return node

    def visit_BinOp(self, node):
        d = {ast.Add: "+", ast.Sub: "-"}
        self.graph.add_node(node)
        self.labels[node] = f'{d[type(node.op)]}'
        self.graph.add_edge(node, self.visit(node.left))
        self.graph.add_edge(node, self.visit(node.right))
        return node

    def visit_For(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'For cycle'
        self.graph.add_edge(node, self.visit(node.target))
        self.graph.add_edge(node, self.visit(node.iter))
        for el in node.body:
            self.graph.add_edge(node, self.visit(el))
        return node

    def visit_Name(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'{node.id}'
        return node

    def visit_Call(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'()'
        self.graph.add_edge(node, self.visit(node.func))
        for el in node.args:
            self.graph.add_edge(node, self.visit(el))
        return node

    def visit_List(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'List'
        for el in node.elts:
            self.graph.add_edge(node, self.visit(el))
        return node

    def visit_Constant(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'{node.value}'
        return node

    def visit_Subscript(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'[]'
        self.graph.add_edge(node, self.visit(node.value))
        self.graph.add_edge(node, self.visit(node.slice))
        return node

    def visit_Expr(self, node):
        return self.visit(node.value)

    def visit_Attribute(self, node):
        self.graph.add_node(node)
        self.labels[node] = f'.{node.attr}'
        self.graph.add_edge(node, self.visit(node.value))
        return node

    def report(self):
        figure(figsize=(8, 6), dpi=200)
        pos = nx.circular_layout(self.graph)
        nx.draw_networkx(self.graph, pos=nx.spring_layout(self.graph), with_labels=True, node_shape="s", node_size=300, labels=self.labels, arrows=True, arrowsize=2)
        plt.show()

def n_fibonacci(n):
    list = [0, 1]
    for i in range(n - 1):
        list.append(list[i] + list[i + 1])
    print(list)


if __name__ == '__main__':
    tree = ast.parse('''def n_fibonacci(n):
    list = [0, 1]
    for i in range(n-1):
        list.append(list[i] + list[i+1])
    print(list)
    ''')
    #help(Graph)
    pprint(ast.dump(tree))
    analyzer1 = Analyzer()
    analyzer1.visit(tree)
    analyzer1.report()
    #G = nx.Graph()
    #G.add_node("A")
    #G.add_node("B")
    #G.add_edge(*("A", "B"))
    #nx.draw(G)
    #plt.show()