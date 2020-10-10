from Tree import Tree

def apply(node):
    operator = node.value
    if operator == '+':
        node.value = float(node.right.value) + float(node.left.value)
    elif operator == '-':
        node.value = float(node.right.value) - float(node.left.value)
    elif operator == '*':
        node.value = float(node.right.value) * float(node.left.value)
    elif operator == '/':
        node.value = float(node.right.value) / float(node.left.value)

def evaluateTree(node):
    if node.left != None:
        evaluateTree(node.left)
        evaluateTree(node.right)
        apply(node)

if __name__ == "__main__":
    tree = Tree('10+8*5/10')
    root = tree.get_root()
    evaluateTree(root)
    print(tree.expression + ' = ' + str(root.value))