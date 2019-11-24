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
    def __init__(self, top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)

    def pop(self):
        self.ll.delete_first()


class Element:
    def __init__(self, value):
        self.value = value
        self.next = None  # reference to the next element of list

    def __str__(self):
        return 'Value: {}, Next: {}'.format(self.value, self.next)


head_element = Element(5)
second_element = Element(6)
third_element = Element(7)
ll = LinkedList(head=head_element)
ll.append(second_element)
ll.append(third_element)
print(ll.get_position(0))
my_el = Element(15000)
ll.insert(my_el, 1)
print(ll.get_position(0))
ll.delete(15000)
print(ll.get_position(0))
ll.insert_first(Element(10000))
print(ll.get_position(0))
ll.delete_first()
print(ll.get_position(0))
