# 🔗 Linked Lists - Simple Guide

## What is a Linked List?

Think of a **linked list** like a chain of people holding hands. Each person knows who's next to them, but they can't see the whole line.

```
Person A → Person B → Person C → Person D → End
```

In programming, instead of people, we have **nodes**. Each node has:
- **Data** (the actual information)
- **Pointer** (address of the next node)

## Visual Example

```
┌───────┐    ┌───────┐    ┌───────┐
│ 10 │→ │    │ 20 │→ │    │ 30 │→ │
└───────┘    └───────┘    └───────┘
```

## Basic Python Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link them together
node1.next = node2
node2.next = node3

# node1 is our "head" (starting point)
```

## How to Print All Values

```python
def print_list(head):
    current = head
    while current:
        print(current.data)
        current = current.next

print_list(node1)  # Prints: 10, 20, 30
```

## Adding New Nodes

### Add at Beginning
```python
def add_front(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

# Add 5 to the front
head = add_front(node1, 5)
# Now: 5 → 10 → 20 → 30
```

### Add at End
```python
def add_end(head, data):
    new_node = Node(data)
    if not head:
        return new_node
    
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

head = add_end(head, 40)
# Now: 5 → 10 → 20 → 30 → 40
```

## Why Use Linked Lists?

### 1. **Dynamic Size**
- Regular arrays have fixed size
- Linked lists grow/shrink as needed

### 2. **Efficient Insertion**
- Adding to front of array: Move all elements (slow)
- Adding to front of linked list: Just change one pointer (fast)

```
Array:       [1][2][3][4] → Need to shift everything to add at front
Linked List: 1→2→3→4      → Just attach new node at front
```

## What If We Don't Use Them?

### Problems with Arrays Only:

1. **Memory Waste**: Create array of size 1000, use only 10 slots
2. **Slow Insertions**: Adding at beginning requires moving all elements
3. **Fixed Size**: Can't grow beyond initial capacity

## When to Use What?

| Need | Array | Linked List |
|------|-------|-------------|
| Access by index (arr[5]) | ✅ Fast | ❌ Slow |
| Add/remove at beginning | ❌ Slow | ✅ Fast |
| Memory efficiency | ❌ | ✅ |
| Random access | ✅ | ❌ |

## Complete Example: Student List

```python
class Student:
    def __init__(self, name):
        self.name = name
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None
    
    def add_student(self, name):
        new_student = Student(name)
        new_student.next = self.head
        self.head = new_student
    
    def show_all(self):
        current = self.head
        while current:
            print(current.name)
            current = current.next

# Usage
class_list = StudentList()
class_list.add_student("Alice")
class_list.add_student("Bob")
class_list.add_student("Charlie")

class_list.show_all()  # Prints: Charlie, Bob, Alice
```

## Key Points

1. **Nodes** = containers with data + pointer to next
2. **Head** = first node in the list
3. **Traversal** = following pointers from start to end
4. **Dynamic** = size can change during runtime
5. **Trade-off** = Fast insertion vs slow random access

## Memory Visualization

```
Array in Memory:     [A][B][C][D] ← All together
Linked List Memory:  [A]→  [C]→  [B]→  [D] ← Scattered but connected
```

That's it! Linked lists are just connected nodes that can grow and shrink efficiently.


## Types of Linked Lists

There are in total 4 types of linked lists:

1. **`Singly Linked List`**: Each item points to the next one. <br>
![Singly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Singly-linked-list.svg/408px-Singly-linked-list.svg.png)

2. **`Doubly Linked List`**: Each item points to the next and previous one. <br>
![Doubly Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/408px-Doubly-linked-list.svg.png)

3. **`Circular Linked List`**: The last item points back to the first one. <br>
![Circular Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Circularly-linked-list.svg/408px-Circularly-linked-list.svg.png)

4. **`Doubly Circular Linked List`**: A mix of the above two. Each item points to the next and previous one, and the last item points back to the first one. <br>
![Doubly Circular Linked List](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Doubly-linked-list.svg/408px-Doubly-linked-list.svg.png)


## Links
1. [Single linked list](1.single_linked_lists.md) <br>
2. [Doubly linked list](2.doubly_linked_lists.md) <br>
3. [Circular linked list](3.circular_linked_lists.md) <br>
4. [Doubly circular linked list](4.doubly_circular_linked_lists.md)