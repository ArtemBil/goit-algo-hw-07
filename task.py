class Node(object):
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:

            self.root = Node(data)
        else:
            self.insert_node(data, self.root)


    def insert_node(self, data, node):

        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data)

        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:

                node.right_child = Node(data)


    def remove(self, data):
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)

        else:
            if not node.left_child and not node.right_child:
                del node
                return None

            if not node.left_child:
                temp_node = node.right_child
                del node
                return temp_node

            elif not node.right_child:
                temp_node = node.left_child
                del node
                return temp_node

            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)
        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

    def get_sum_of_values(self):
        if self.root:
            return self._get_sum(self.root)

    def _get_sum(self, node):
        if node is None:
            return 0
        return node.data + self._get_sum(node.left_child) + self._get_sum(node.right_child)

    def traversal(self, path):
        if self.root:
            self.pre_order_traversal(self.root, path)

    def pre_order_traversal(self, node, path):
        if node:
            path.append(node)
            self.pre_order_traversal(node.left_child, path)
            self.pre_order_traversal(node.right_child, path)

    def search(self, data):
        return self.search_node(data, self.root)

    def search_node(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search_node(data, node.left_child)
        return self.search_node(data, node.right_child)

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(20)
bst.insert(2)
bst.insert(7)
bst.insert(30)

print("Max value:", bst.get_max_value())
print("Min value:", bst.get_min_value())
print("Sum of values:", bst.get_sum_of_values())
