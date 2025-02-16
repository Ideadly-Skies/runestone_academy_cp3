from Deque import Deque

def pal_checker(a_string):
    """check if a_string is valid palindrome"""
    # create a char deque
    char_deque = Deque()

    # enqueue each character from the rear
    for char in a_string:
        char_deque.add_rear(char)

    # dequeue from front and back and check if equal
    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if (first != last):
            # invalid palindrome
            return False

    # valid palindrome 
    return True

if __name__ == "__main__":
    print(pal_checker("abcba"))