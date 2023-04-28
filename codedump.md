# CODIGO 1
Funca pero no sabemos exactamente como y porque.
```
import graphviz

class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children or []

    def __repr__(self):
        return self.label

def parse_E(tokens):
    node = Node('E')
    node.children.append(parse_T(tokens))
    node.children.append(parse_E_prime(tokens))
    return node

def parse_E_prime(tokens):
    if tokens and tokens[0] == '+':
        node = Node('+')
        tokens.pop(0) # consume the '+'
        node.children.append(parse_T(tokens))
        node.children.append(parse_E_prime(tokens))
        return node
    else:
        return Node('ε')

def parse_T(tokens):
    node = Node('T')
    node.children.append(parse_F(tokens))
    node.children.append(parse_T_prime(tokens))
    return node

def parse_T_prime(tokens):
    if tokens and tokens[0] == '*':
        node = Node('*')
        tokens.pop(0) # consume the '*'
        node.children.append(parse_F(tokens))
        node.children.append(parse_T_prime(tokens))
        return node
    else:
        return Node('ε')

def parse_F(tokens):
    if tokens and tokens[0] == '(':
        tokens.pop(0) # consume the '('
        node = parse_E(tokens)
        tokens.pop(0) # consume the ')'
        return node
    elif tokens and tokens[0].isidentifier():
        return Node(tokens.pop(0))
    else:
        raise ValueError('Expected an identifier or \'(\'')

def build_tree(node):
    if not node.children:
        return graphviz.Digraph(node.label)
    else:
        tree = graphviz.Digraph(node.label)
        for child in node.children:
            sub_tree = build_tree(child)
            tree.subgraph(sub_tree)
            tree.edge(node.label, child.label)
        return tree

def main():
    while True:
        try:
            s = input('> ')
            tokens = list(s)
            tree = build_tree(parse_E(tokens))
            tree.view()
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()
```

# CODIGO 2

```
import graphviz

def A(cadena):
    if len(cadena) == 0:
        return False
    if B(cadena) or C(cadena):
        return True
    return False

def B(cadena):
    if len(cadena) == 0:
        return False
    if cadena[0] == 'D':
        return A(cadena[1:])
    if cadena[0] == 'b':
        return True
    return False

def C(cadena):
    if len(cadena) == 0:
        return False
    if cadena[0] == 'c':
        return C(cadena[1:]) and A(cadena[2:])
    return False

def D(cadena):
    if len(cadena) == 0:
        return False
    if cadena[0] == 'd' and cadena[1] == 'd':
        return True
    return False

#cadena = input("Ingrese una cadena: ")
#if A(cadena):
 #   print("La cadena es válida para la gramática.")
#else:
 #   print("La cadena NO es válida para la gramática.")


def draw_tree(cadena):
    dot = graphviz.Digraph(comment='Árbol gramatical')
    dot.node('A', 'A')
    dot.node('B', 'B')
    dot.node('C', 'C')
    dot.node('D', 'D')
    dot.node('b', 'b')
    dot.node('c', 'c')
    dot.node('d', 'd')
    dot.node('dd', 'dd')
    dot.edge('A', 'B')
    dot.edge('A', 'C')
    dot.edge('B', 'D')
    dot.edge('B', 'b')
    dot.edge('C', 'c')
    dot.edge('C', 'A')
    dot.edge('A', 'B')
    dot.edge('D', 'd')
    dot.edge('D', 'dd')
    dot.format = 'png'
    dot.render('tree', view=True)

cadena = input("Ingrese una cadena: ")
draw_tree(cadena)
```