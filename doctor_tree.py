class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

class DoctorTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_name, employee_name, side):
        if side not in ("left", "right"):
            return False

        if self.root is None:
            if parent_name is None:
                self.root = DoctorNode(employee_name)
                return True
            return False
        return self._insert_recursive(
            self.root, parent_name, employee_name, side
        )

    def _insert_recursive(self, current, parent_name, employee_name, side):
        if current is None:
            return False

        if current.name == parent_name:
            if side == "left" and current.left is None:
                current.left = DoctorNode(employee_name)
                return True
            elif side == "right" and current.right is None:
                current.right = DoctorNode(employee_name)
                return True
            else:
                return False

        if self._insert_recursive(current.left, parent_name, employee_name, side):
            return True
        return self._insert_recursive(current.right, parent_name, employee_name, side)

    
    def preorder(self, node):
        result = []

        if node is not None:
            result.append(node.name)
            result.extend(self.preorder(node.left))
            result.extend(self.preorder(node.right))
        return result

    def inorder(self, node):
        result = []

        if node is not None:
            result.extend(self.inorder(node.left))
            result.append(node.name)
            result.extend(self.inorder(node.right))
        return result

    def postorder(self, node):
        result = []

        if node is not None:
            result.extend(self.postorder(node.left))
            result.extend(self.postorder(node.right))
            result.append(node.name)
        return result



# Test your DoctorTree and DoctorNode classes here
tree = DoctorTree()
tree.root = DoctorNode("Dr. Croft") 
# Test Inserting Values
print(tree.insert("Dr. Croft", "Dr. Goldsmith", "right"))
print(tree.insert("Dr. Croft", "Dr. Phan", "left"))
print(tree.insert("Dr. Phan", "Dr. Carson", "right")) 
print(tree.insert("Dr. Phan", "Dr. Morgan", "left"))

#Test Inserting a Value with a Missing Parent
print(tree.insert("Dr. Unknown", "Dr. Brown", "left"))
#Test Inserting with an Invalid Side
print(tree.insert("Dr. Croft", "Dr. Brown", "middle"))
#Test Inserting with an Occupied Side
print(tree.insert("Dr. Croft", "Dr. Green", "left"))

#Test Transversal Methods
print(tree.preorder(tree.root))
print(tree.inorder(tree.root)) 
print(tree.postorder(tree.root)) 

#Test Traversal with an Empty Tree
empty_tree = DoctorTree()
print(empty_tree.preorder(empty_tree.root))
print(empty_tree.inorder(empty_tree.root))
print(empty_tree.postorder(empty_tree.root))

#Test Inserting into a Empty Tree
new_tree = DoctorTree()
print(new_tree.insert(None, "Dr. Croft", "left"))
print(new_tree.preorder(new_tree.root))