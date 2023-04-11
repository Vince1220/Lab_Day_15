from LinkedList.node import Node
class LinkedList:
    def __init__(self):
        self.root_node = None
        pass

    def add_node(self,data):
        new_node = Node(data)
        print (new_node.data)
        if self.root_node == None:
            self.root_node = new_node
            self.last_node = new_node
        else:
            self.last_node.next_node = new_node
            self.last_node =self.last_node.next_node
            

    def search_node (self, data_to_find): 
        current_node =self.root_node
        while current_node != None:
            if current_node.data == data_to_find:
                return True
            else:
                current_node = current_node.next_node
        return False       
    

