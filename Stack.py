"""
Name: Lucas March
ID: 20144315
CISC 235 Assignment 1 Q4 stack implementation
"""

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        """Check if Stack is empty."""
        return self.items == []

    def push(self, item):
        """Add element to Stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return element from stack."""
        return self.items.pop()

    def top(self):
        """Remove and do not return element from stack."""
        return self.items[len(self.items) - 1]

    def size(self):
        """Return size of stack."""
        return len(self.items)

if __name__ == "__main__":
    stack1 = Stack()
    print(stack1.isEmpty())
    stack1.push(3)
    stack1.push(5)
    print(stack1.size())
    print(stack1.top())
    stack1.pop()
    print(stack1.size())


