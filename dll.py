# Doubly Linked List - python implementation by Utkarsh Singh
class DLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data = {}".format(self.data)

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of the self.data attribute with the new_data value"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of the self.next attribute with the new_next value"""
        self.next = new_next

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of the self.previous attribute with the new_previous value"""
        self.previous = new_previous

class DLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL object: head= {}>".format(self.head)

    def is_empty(self):
        return self.head is None

    def size(self):
        """Traverses a linked list and returns an integer value representing the number of nodes in the list.

        Time complexity is O(n): because every node in the linked list must be visited to calculate the size of the
        Linked list.
        """
        size = 0
        if self.head is None:
            return size

        current = self.head
        while current is not None:  # While we still have nodes to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the LL and returns true if data being searched for is present in one of the nodes otherwise
        it results false.

        Time complexity is O(n)
        """
        if self.head is None:
            return "Linked list is empty. No node to search."

        current = self.head
        count = 1
        while current is not None:
            # 1) Node's data matches what we are looking for
            if current.get_data() == data:
                return "{0} was found at location {1}".format(data, count)
            # 2) Data nor found
            else:
                current = current.get_next()
                count += 1
        return "{0} was not found in the list.".format(data)

    def add_front(self, new_data):
        """Add a node whose data is the new_data argument to the front of the linked list"""
        temp = DLLNode(new_data)
        temp.set_next(self.head)
        if self.head is not None:
            self.head.set_previous(temp)

        self.head = temp

    def remove(self, data):
        """Removes the first occurrence of a node that contains the data argument as its self.data attribute. Return
        nothing.

        Time complexity: O(n)
        """
        if self.head is None:
            return "Linked list is empty. No nodes to remove"

        current = self.head
        found = False
        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "Data to be removed was not found in the linked list."
                else:
                    current = current.get_next()

        # We found the data we are looking for
        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())

    def printList(self):
        """Prints the contents of the list, if list has elements. Otherwise, returns a meaningful message."""
        if self.head is None:
            return "This is an empty list. Nothing to print."
        else:
            count = 1
            current = self.head
            while current is not None:
                print("Element '{0}' is at location {1}".format(current.get_data(), count))
                count += 1
                current = current.get_next()

    def append(self, data):
        """Appends provided data at the end of the list and prints the updated list."""
        if self.head is None:
            print("The list is currently empty. The last element will also be the first element.")
            self.add_front(data)
        else:
            current = self.head
            _previous = self.head
            while current is not None:
                _previous = current
                current = current.get_next()
            new_node = DLLNode(data)

            _previous.set_next(new_node)
            new_node.set_previous(current)
        print("Printing the updated list below:")
        self.printList()

    def insert(self, position, data):
        """Inserts provided data at the provided position in the list and prints the list."""
        if self.head is None and position == 1:
            print("The list is currently. This will be the first element in the list.")
            self.add_front(data)
        elif self.head is None and position > 1:
            return "The list is currently empty. Cannot insert {0} at {1}".format(data, position)
        else:
            current = self.head
            _previous = self.head
            _next = self.head
            index = 1
            while index != position:
                _previous = current
                current = current.get_next()
                _next = current
                index += 1

            new_node = DLLNode(data)
            _previous.set_next(new_node)
            new_node.set_previous(_previous)
            new_node.set_next(current)

        print("Printing the updated list below:")
        self.printList()

    def reverse(self):
        """Reverses a doubly linked list and prints the result."""
        temp = None
        current = self.head

        while current is not None:
            temp = current.get_previous()
            current.set_previous(current.get_next())
            current.set_next(temp)
            current = current.get_previous()

        if temp is not None:
            self.head = temp.get_previous()

        print("Updated list is:")
        self.printList()