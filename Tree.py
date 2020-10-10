from Node import Node
from Tokenizer import tokenize

class Tree:
    def __init__(self, expression):
        self.root = None
        self.expression = expression
        self.operators = ')+-*/('
        self.operands_stack = []
        self.operators_stack = []
        self.createTree(expression)

    def createTree(self, expression_string):
        index = 0
        expression = tokenize(expression_string, ['()+-*/', '012345789'])
        total = len(expression)

        while index != total:
            token = expression[index]
            if token != ' ':
                if self.operators.count(token) == 0:
                    self.operands_stack.append(Node(value=token))
                elif token == ')':
                    while self.operators_stack != [] and self.operators_stack[-1] == '(':
                        self.save_sub_tree()
                    self.operators_stack.pop()
                else:
                    if token != '(' and self.operators_stack != []:
                        op = self.operators_stack[-1]
                        try:
                            while op != '(' and self.operators_stack != [] and \
                                self.operators.index(op) >= self.operators.index(token):
                                    self.save_sub_tree()
                                    if self.operators_stack != []:
                                        op = self.operators_stack[-1]
                        except ValueError:
                            pass
                    self.operators_stack.append(token)
            index += 1
        
        self.root = self.operands_stack[-1]
        while self.operators_stack != []:
            if self.operators_stack[-1] == '(':
                self.operators_stack.pop()
            else:
                self.save_sub_tree()
                self.root = self.operands_stack[-1]

    def save_sub_tree(self):
        op2 = self.operands_stack.pop()
        op1 = self.operands_stack.pop()
        self.operands_stack.append(Node(self.operators_stack.pop(), op2, op1))

    def get_root(self):
        return self.root

    def get_preOrder(self):
        self.preOrder(self.root)

    def preOrder(self, node):
        if node != None:
            print(node.value)
            self.preOrder(node.left)
            self.preOrder(node.right)