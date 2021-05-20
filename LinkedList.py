"""
Name: Lucas March
ID: 20144315
CISC 235 Assignment 1 Q4 linked list stack implementation.
"""

class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


class Stack:
    def __init__(self):
        self.linkedlist = self.LinkedList()

    class LinkedList:
        def __init__(self):
            self.head = None
            self.size = 0

    def isEmpty(self):
        """Check if Stack is empty."""
        if self.linkedlist.head is None:
            return True
        else:
            return False

    def push(self, data):
        """Add element to stack."""
        if self.linkedlist.head is None:
            self.linkedlist.head = Node(data)
            self.linkedlist.size += 1
        else:
            new_node = Node(data)
            new_node.next = self.linkedlist.head
            self.linkedlist.head = new_node
            self.linkedlist.size += 1

    def pop(self):
        """Remove and return top element of stack"""
        if self.isEmpty():
            print("Stack is empty.")
        else:
            ans = self.linkedlist.head.element
            self.linkedlist.head = self.linkedlist.head.next
            self.linkedlist.size -= 1
            return ans

    def top(self):
        """Return and do not remove top element of stack."""
        if self.isEmpty():
            print("Stack is empty.")
        else:
            return self.linkedlist.head.element

    def size(self):
        """Return size of stack."""
        return self.linkedlist.size





if __name__ == "__main__":
    stack2 = Stack()
    print(stack2.isEmpty())
    stack2.push(3)
    stack2.push(5)
    print(stack2.size())
    print(stack2.top())
    stack2.pop()
    print(stack2.size())
