class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.size

    def push(self, value):
        if self.isFull():
            print("Stack is Full. Cannot push.")
        else:
            self.stack.append(value)
            print(f"{value} pushed into stack.")

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            removed = self.stack.pop()
            print("Removed:", removed)

    def top(self):
        if self.isEmpty():
            print("Stack is Empty.")
        else:
            print("Top element is:", self.stack[-1])

    def display(self):
        print("Current Stack:", self.stack)


# User Interaction
size = int(input("Enter stack size: "))
s = Stack(size)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. isEmpty")
    print("5. isFull")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        values = input("Enter values separated by space: ").split()
        for value in values:
            s.push(value)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.top()

    elif choice == 4:
        print("Stack is Empty." if s.isEmpty() else "Stack is Not Empty.")

    elif choice == 5:
        print("Stack is Full." if s.isFull() else "Stack is Not Full.")

    elif choice == 6:
        s.display()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

"""
A stack is a data structure that works on Last In, First Out (LIFO).
The last item you add is the first one you remove.

Example: like a stack of plates — you can only take the top plate off.

We use a stack when we need to:
Undo recent actions
Track function calls
Check brackets
Go back to previous steps (backtracking)

In AI, stacks are used in search algorithms like Depth-First Search (DFS), 
where the system explores one path deeply and goes back if it fails.

"""
