class BST:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return  # assuming no duplicates allowed
        if self.key > data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = BST(data)  # we are creating a new node here
        else:
            if self.right:
                self.right.insert(data)
            else:
                self.right = BST(data)  # we are creating a new node here

root = BST(10)
list = [5, 15, 3, 7, 12, 18]
for i in list:
    root.insert(i)