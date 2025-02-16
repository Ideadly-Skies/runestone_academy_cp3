from LinkedList import Node

class OrderedList:
    def __init__(self):
        """constructor for OrderedList"""
        self.head = None

    def is_empty(self):
        """check if the head of the list is a reference to None"""
        return self.head == None
    
    def size(self):
        """get the size of the UnorderedList"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    
    def search(self, item):
        """search for the item in the list"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            if current.data > item:
                # starting from the head what if it's bigger
                # than the item? and the list is ordered in increasing order 
                return False
            current = current.next
        return False

    def add(self, item):
        """add a new node"""
        # set self.head to current and previous to None
        current = self.head
        previous = None
        temp = Node(item)

        while current is not None and current.data < item:
            # traverse until we meet insertion position 
            previous = current
            current = current.next

        # add at the beginning of the list
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            # set the next and previous counter 
            temp.next = current
            previous.next = temp