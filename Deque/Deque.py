class Deque:
    """Deque implementation as a list"""

    def __init__(self):
        """creates new deque"""
        self._items = []

    def is_empty(self):
        """checks if the deque is empty"""
        return self._items == []

    def add_front(self, item):
        """Add an item to the front of the deque"""
        self._items.append(item)
    
    def add_rear(self, item):
        """Add an item to the rear of the deque"""
        self._items.insert(0, item)

    def remove_front(self):
        """Remove an item from the front of the deque"""
        return self._items.pop()
    
    def remove_rear(self):
        """Remove an item from the rear of the deque"""
        return self._items.pop(0)
    
    def size(self):
        """return the number of items in the deque"""
        return len(self._items)
