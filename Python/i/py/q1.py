class Stack:
    def __init__(self):
        self.items = []

    # 1. Push an element
    def push(self, value):
        self.items.append(value)

    # 2. Pop an element
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None

        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    # 3. Display from top to bottom
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return

        print("Stack (top to bottom):", end=" ")

        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i], end=" ")

        print()

    # 5. Reverse stack using another stack
    def reverse(self):
        another_stack = Stack()

        while not self.is_empty():
            value = self.pop()
            another_stack.push(value)

        # Use the reversed stack as the current stack
        self.items = another_stack.items


# 4. Reverse string using a stack
def reverse_string(text):
    stack = Stack()

    for character in text:
        stack.push(character)

    reversed_text = ""

    while not stack.is_empty():
        reversed_text += stack.pop()

    return reversed_text


# Main program
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("After pushing 10, 20 and 30:")
stack.display()

print("Popped element:", stack.pop())

print("After pop:")
stack.display()

text = "PYTHON"
print("Original string:", text)
print("Reversed string:", reverse_string(text))

stack.push(40)

print("Before reversing:")
stack.display()

stack.reverse()

print("After reversing:")
stack.display()