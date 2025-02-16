class Node:
    """A node of a linked list"""
    def __init__(self, node_data):
        """node constructor""" 
        self._data = node_data
        self._next = None

    def get_data(self):
        """get node data (maintain data encapsulation)"""
        return self._data

    def set_data(self, node_data):
        """set node data (maintain data encapsulation)"""
        self._data = node_data

    # use to create a property of the class
    data = property(get_data, set_data)

    def get_next(self):
        """get next node"""
        return self._next
    
    def set_next(self, node_next):
        """set next node"""
        self._next = node_next

    next = property(get_next, set_next)

    # string repr of the node object
    def __str__(self):
        """String"""
        return str(self._data)

class UnorderedList:
    def __init__(self):
        """constructor for unordered list"""
        self.head = None
        self.tail = None

    def is_empty(self):
        """check if the head of the list is a reference to None"""
        return self.head == None
    
    def add(self, item):
        """add item to the front of the list"""
        # update the next pointer of the new item to the current head
        temp = Node(item)
        temp.next = self.head
        self.head = temp # appoint temp as the new head

        # set tail for new created unordered list w/ one node
        if (self.size == 1):
            self.tail = self.head
        
    def append(self, item):
        """implement append method for item in this UnorderedList O(1) implementation"""
        temp = self.tail
        temp.next = Node(item)
        self.tail = item 

    def size(self):
        """get the size of the UnorderedList"""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.next
        return count
    
    def search(self, item):
        """perform search of element with current unordered list"""
        current = self.head
        while current is not None:
            if current.data == item:
                return True # element exist
            current = current.next

        # element does not exist
        return False

    def remove(self, item):
        """remove the item from the list"""
        current = self.head
        previous = None
        
        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current is None:
            # the item is not on the list
            raise ValueError("{} is not in the list".format(item))
        if previous is None:
            # remove first element on the list
            self.head = current.next     
        else:
            if (current.next == None):
                # update tail to be previous node
                self.tail = previous
            
            # set the previous's next pointer to current.next
            previous.next = current.next

    def __repr__(self):
        """print UnorderedList Implementation"""
        temp = self.head
        s = "" 
        while (temp.next != None):
            s += str(temp.data) + " -> "
            temp = temp.next
        s += str(temp.data)
        return s

if __name__ == "__main__":
    my_list = UnorderedList()

    my_list.add(31)
    my_list.add(77)
    my_list.add(17)
    my_list.add(93)
    my_list.add(26)
    my_list.add(54)

    print(my_list)

    print(my_list.size())
    print(my_list.search(93))
    print(my_list.search(100))

    my_list.add(100)
    print(my_list.search(100))
    print(my_list.size())

    my_list.remove(54)
    print(my_list.size())
    my_list.remove(93)
    print(my_list.size())
    my_list.remove(31)
    print(my_list.size())
    print(my_list.search(93))

    my_list.append(12)
    print(my_list)
    print(my_list.size())

    try:
        my_list.remove(27)
    except ValueError as ve:
        print(ve)