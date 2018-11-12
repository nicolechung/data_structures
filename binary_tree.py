class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree(object):
  def __init__(self, root):
    self.root = Node(root)

  def print_tree(self, traversal_type):
    if traversal_type == 'preorder':
      return self.preorder_print(tree.root, "")
    elif traversal_type == 'inorder':
      return self.inorder_print(tree.root, "")
    elif traversal_type == 'postorder':
      return self.postorder_print(tree.root, "")
    elif traversal_type == 'breadth':
      return self.breadth_traverse()
    else:
      print("Traversal type " + str(traveral_type) + " is not supported")
      return False

  def preorder_print(self, start, traversal):
    """Root -> Left -> Right"""
    if start:
      traversal += (str(start.value) + "-")
      traversal = self.preorder_print(start.left, traversal)
      traversal = self.preorder_print(start.right, traversal)
    return traversal

  def inorder_print(self, start, traversal):
    """Left -> Root -> Right"""
    if start:
      traversal = self.inorder_print(start.left, traversal)
      traversal += (str(start.value) + "-")
      traversal = self.inorder_print(start.right, traversal)
    return traversal

  def postorder_print(self, start, traversal):
    """Left -> Right -> Root"""
    if start:
      traversal = self.postorder_print(start.left, traversal)
      traversal = self.postorder_print(start.right, traversal)
      traversal += (str(start.value) + "-")
    return traversal

  def breadth_traverse(self):
    """Root -> Left -> Right"""
    queue = [self.root]
    traversal = ''
    while len(queue) > 0:
      treeNode = queue.pop(0)
      traversal += str(treeNode.value) + '-'
      if treeNode.left:
        queue.append(treeNode.left)
      if treeNode.right:
        queue.append(treeNode.right)

    return traversal

# 1-2-4-5-3-6-7-8 -> preorder
# 4-2-5-1-6-3-7-8 -> inorder
# 4-5-2-6-8-7-3-1- -> postorder
#          1
#        /  \
#      2      3
#    /  \    / \
#   4    5  6   7
#                \
#                 8
tree = BinaryTree(1)

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree('breadth'))
