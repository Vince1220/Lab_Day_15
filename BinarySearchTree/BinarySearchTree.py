from binary_node import Binary_node

class Binary_Search_Tree:
    def __init__(self, data):
        self.root_node = None
        self.data = data
    def insert_node(self, data):
        if self.data:
            if data < self.data: 
                if self.left_node is None:
                    self.left_node = self.data
            else:
                self.left_node.insert(self.data)
        elif data > self.data:
          if self.right_node == None:
                self.right_node == self.data
          else:
                self.right_node.insert(self.data)
        
        pass
    def search_for_node(self,find_data):
        if find_data == self.data:
            if find_data < self.data:
                if self.left_node:
                    self.left_node.search_for_node(find_data)
                else:
                    if self.right_node:
                        self.right_node.search_for_node(find_data)
        
        pass