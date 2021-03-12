class Tree:
    """
    Описание класса дерево.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, number):
        if self.value:
            if number < self.value:
                if not self.left:
                    self.left = Tree(number)
                else:
                    self.left.add(number)
            else:
                if not self.right:
                    self.right = Tree(number)
                else:
                    self.right.add(number)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.value)
        if self.right:
            self.right.print_tree()



# tree = Tree(4, Tree(2, Tree(1), Tree(3)), Tree(6, Tree(5), Tree(7)))
tree = Tree(4)
tree.add(2)
tree.add(3)
tree.add(6)
tree.add(1)
tree.add(5)
tree.add(7)
# tree.print_tree()

def preorder(tree):
    if not tree:
        return
    stack = []
    stack.append(tree)
    while stack:
        tree = stack.pop()
        print(tree.value)
        if tree.right:
            stack.append(tree.right)
        if tree.left:
            stack.append(tree.left)

def inorder(tree):
    stack = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            print(tree.value)
            tree = tree.right

def postorder(tree):
    stack = []
    stack.append(tree)
    out = []
    while stack:
        current = stack.pop()
        out.append(current.value)
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)
    
    while out:
        print(out.pop())

def levelorder(tree):
    queue = []
    queue.append(tree)
    while queue:
        tree = queue.pop(0)
        print(tree.value)
        if tree.left:
            queue.append(tree.left)
        if tree.right:
            queue.append(tree.right)

print('\nПрямой обход:')
preorder(tree)

print('\nЦентрированный обход:')
inorder(tree)

print('\nОбратный обход:')
postorder(tree)

print('\nПоиск в ширину:')
levelorder(tree)