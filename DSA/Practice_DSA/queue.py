class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size

    def push(self, values):  # Accepts a list of values
        for value in values:
            if self.isFull():
                print("Queue is Full. Cannot push more values.")
                break
            self.queue.append(value)
            print(f"{value} added to queue.")

    def pop(self):
        if self.isEmpty():
            print("Queue is Empty.")
        else:
            removed = self.queue.pop(0)
            print("Removed:", removed)

    def front(self):
        if self.isEmpty():
            print("Queue is Empty.")
        else:
            print("Front element is:", self.queue[0])

    def display(self):
        print("Current Queue:", self.queue)


# User Interaction
size = int(input("Enter queue size: "))
q = Queue(size)

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Front")
    print("4. isEmpty")
    print("5. isFull")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        values = input("Enter values to push (space-separated): ").split()
        q.push(values)

    elif choice == 2:
        q.pop()

    elif choice == 3:
        q.front()

    elif choice == 4:
        print("Queue is Empty." if q.isEmpty() else "Queue is Not Empty.")

    elif choice == 5:
        print("Queue is Full." if q.isFull() else "Queue is Not Full.")

    elif choice == 6:
        q.display()

    elif choice == 7:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Try again.")

"""
A queue is a data structure that works on: First In, First Out (FIFO)
Think about standing in a line.The first person who comes in line is the first one to leave. New people join at the back.
Service happens from the front.

In simple words:

The first item you add is the first one removed.
Queues are used when order matters and tasks must be handled in the same sequence they arrive.
In AI, queues are used in algorithms like Breadth-First Search (BFS), where the system explores level by level instead of going deep. 
They’re also used in task scheduling, request handling, and simulations.

"""
