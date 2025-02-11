class Queue:
    """Queue implementation as a list"""

    def __init__(self):
        """Create new queue"""
        self._items = []

    def is_empty(self):
        """Check if the queue is empty"""
        return not bool(self._items)

    def enqueue(self, item):
        """Add item to the queue"""
        self._items.insert(0, item)
    
    def dequeue(self, item):
        """Remove item from the queue"""
        self._items.pop()

    def size(self):
        """Get the number of items in the queue"""
        return len(self._items)
    
