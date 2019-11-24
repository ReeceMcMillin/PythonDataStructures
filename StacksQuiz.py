class LinkedList:
    def __init__(self, head=None):
        self.head = head  # First element of linked list

    def insert_first(self, new_element):
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        delete = self.head
        self.head = delete.next

    def append(self, new_element):
        current = self.head  # We want to start at the head of the ll
        if self.head is not None:  # Make sure the head exists
            while current.next is not None:  # If there's a next element in the list
                current = current.next  # Keep iterating through linked list until we find an element without a .next
            current.next = new_element  # Once we've broken out of the linked list, set current.next to the new element
        else:  # If the list hasn't been initialized, initialize it
            self.head = new_element

    def get_position(self, position):
        current = self.head
        i = 0
        if self.head is not None:
            while current.next is not None:
                if i == position:
                    return current
                i += 1
                current = current.next
        return None

    def insert(self, new_element, desired_position):
        current = self.head
        current_position = 0
        if self.head is not None:
            while current.next is not None:
                if current_position + 1 == desired_position:
                    temp = current.next
                    current.next = new_element
                    new_element.next = temp
                current = current.next
                current_position += 1
        return None

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next is not None:  # If we aren't at the value and aren't at the end
            previous = current
            current = current.next  # Move to next element
        if current.value == value:  # If we've found the value
            if previous is not None:  # If there's a previous value
                previous.next = current.next  # Set the next element to the current element
            else:
                # If there's no previous value, we replace the current head with the next value.
                self.head = current.next


class Stack:
    elements = []  # Only here to keep track of things for easy printing

    def __init__(self, top=None):
        self.ll = LinkedList(top)
        self.elements.append(top)

    def push(self, new_element):
        self.elements.append(new_element)
        self.ll.insert_first(new_element)

    def pop(self):
        self.elements.pop()
        self.ll.delete_first()

    def __str__(self):
        return f'{" ".join([str(element.value) for element in self.elements])}'


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None  # reference to the next element of list

    def __str__(self):
        return 'Value: {}, Next: {}'.format(self.value, self.next)


my_stack = Stack(top=Element(4))
print(my_stack)  # 4
my_stack.push(Element(3))
print(my_stack)  # 4 3
my_stack.push(Element('Element with a different data type'))
print(my_stack)  # 4 3 Element with a different data type
my_stack.pop()
print(my_stack)  # 4 3
