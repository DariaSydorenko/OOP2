class Node:
    def __init__(self, code, qt, price=0.0):
        self.code = code
        self.qt = qt
        self.price = price
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.__price_list = {"001": 6.1, "275": 12.8, "314": 7.1,
                             "211": 10.9, "122": 2.4, "101": 6.8}

    def tree(self, root):
        if not self.root:
            root.price = self.find_price(root.code, root.qt)
            self.root = root
        else:
            code, qt = self.inp_data()
            self.add(root, code, qt)

    def inp_data(self):
        code = input("Enter code of product: ")
        qt = int(input("Enter quantity of products: "))
        return code, qt

    def add(self, root, code, qt):
        if code in self.__price_list:
            price = self.find_price(code, qt)
        else:
            print("! Code not found in price list. !")
            return 0
        if code < root.code:
            if not root.left:
                root.left = Node(code, qt, price)
            else:
                self.add(root.left, code, qt)
        else:
            if not root.right:
                root.right = Node(code, qt, price)
            else:
                self.add(root.right, code, qt)

    def find_price(self, code, qt):
        price = self.__price_list[code] * qt
        return round(price, 2)

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += f"({start.code}) {start.price}, "
            traversal = self.inorder_print(start.right, traversal)
        return traversal


root = Node("211", 8)
tree = BinaryTree()
tree.tree(root)
tree.tree(root)
tree.tree(root)
tree.tree(root)
print(tree.inorder_print(root, ""))
