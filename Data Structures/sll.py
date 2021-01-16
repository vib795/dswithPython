# Singly Linked List - python implementation by Utkarsh Singh
class SllNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SllNode object: data = {}".format(self.data)

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


# Singly Linked List class
class SLL:
    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<SLL object: head= {}>".format(self.head)

    def is_empty(self):
        """Returns True if Linked list is empty otherwise returns false"""
        if self.head is None:
            return True
        else:
            return False
        # return self.head is None OR return self.head == None

    def add_front(self, new_data):
        """Add a node whose data is the new_data argument to the front of the linked list"""
        temp = SllNode(new_data)
        temp.set_next(self.head)
        self.head = temp

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

    def remove(self, data):
        """Removes the first occurrence of a node that contains the data argument as its self.data variable and
        ir return nothing.

        Time complexity: O(n)
        """
        if self.head is None:
            return "Empty list. Nothing to remove."

        current = self.head
        previous = None
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "Data to delete not found in the list."
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def printList(self):
        """Prints the contents of the list, if list has elements. Otherwise, returns a meaningful message."""
        if self.head is None:
            return "This is an empty list. Nothing to print."
        else:
            count = 1
            current = self.head
            while current is not None:
                print("Element {0} is at location {1}".format(current.get_data(), count))
                count += 1
                current = current.get_next()

    def insert(self, position, data):
        """Inserts data in the list at the provided position."""
        if self.head is None and position == 1:
            print("List is current empty. Adding at the first position.")
            self.add_front(data)
        elif self.head is None and position > 1:
            print("List is currently empty. Cannot insert {0} at the provided position {1}".format(data, position))
        else:
            current = self.head
            previous = None
            index = 1
            temp = SllNode(data)
            while index != position:
                previous = current
                current = current.get_next()
                index += 1
            previous.set_next(temp)
            temp.set_next(current)

    def append(self, data):
        """Appends provided data at the end of the list and prints the updated list."""
        if self.head is None:
            print("List is empty. This is the first and the last element in the list. ")
            self.add_front(data)
        else:
            current = self.head
            temp = SllNode(data)
            previous = self.head
            while current is not None:
                previous = current
                print("Previous", previous)
                current = current.get_next()
                print("Current", current)
            previous.set_next(temp)
        print("Printing the final list below:S")
        self.printList()

    def reverse(self):
        """Reverse the order of elements in the linked list."""
        if self.head is None:
            return "The list is currently empty. Cannot be reversed."
        elif self.head is not None and self.size() == 1:
            return "There is only one item in the list. So, consider it reversed."
        else:
            current = self.head
            previous = None
            next = None

            while current is not None:
                next = current.get_next()
                current.set_next(previous)
                previous = current
                current = next
            self.head = previous

            print("Printing the updated list below:")
            self.printList()