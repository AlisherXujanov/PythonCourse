# Linked lists

Imagine a train where each car is connected to the next one. That's exactly how a linked list works! 🚂

## What is a Linked List?
A linked list is like a chain of items where each item points to the next one, just like train cars connected together.

### Simple Example
```
[First Item] → [Second Item] → [Third Item] → null
```

## Why Use Linked Lists?
- Easy to add or remove items (like adding or removing train cars)
- Can grow or shrink as needed
- Great for making lists that change a lot

## Basic Parts
1. **Node**: Each item in the list (like a train car)
2. **Data**: The actual thing we want to store
3. **Next**: The link to the next item

## Operations
1. Add a new item (like adding a new train car)
    - append   (to the end)
    - prepend  (to the beginning)
    - insert   (at given index)
2. Remove an item
    - remove   (by value)
    - remove at (by index)
    - remove last
    - remove first
3. Find an item
    - get first
    - get last
    - find by index
4. Go through all items
    - iterate
    - reverse iterate
5. Other
    - size
    - clear
    - is empty

Remember: Unlike an array where everything is in a line, linked list items can be anywhere in memory - they just need to know where the next item is!


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