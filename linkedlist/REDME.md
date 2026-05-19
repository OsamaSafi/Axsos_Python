# Singly Linked List Implementation in Python

A clean and intuitive Python implementation of a **Singly Linked List** (`SList`) along with its node structure (`SLNode`). This project covers essential linked list operations, including insertion, traversal, and deletion.

---

## Features & Methods

The `SList` class supports the following core operations:

*   **`add_to_front(val)`**: Inserts a new node with the given value at the beginning of the list. (Supports method chaining).
*   **`add_to_back(val)`**: Appends a new node with the given value to the end of the list. (Supports method chaining).
*   **`print_values()`**: Traverses the list and prints the value of each node sequentially.
*   **`remove_from_front()`**: Removes the first node from the list and returns its value. Returns `None` if the list is empty.
*   **`remove_from_back()`**: Removes the last node from the list and returns its value. Returns `None` if the list is empty.
*   **`remove_val(val)`**: Finds and removes the first node that matches the specified `val`, returning its value. Returns `None` if the value is not found.

---

## Usage Example

Here is how you can initialize the list, chain insertion methods, and perform deletions:

```python
# Create a new Singly Linked List
my_list = SList()

# Chain adding elements
my_list.add_to_front("B").add_to_front("A").add_to_back("C").add_to_back("D")

print("Original List:")
my_list.print_values()
# Output:
# A
# B
# C
# D

print("\nRemoved from front:", my_list.remove_from_front()) # Output: A
print("Removed from back:", my_list.remove_from_back())   # Output: D

print("\nList after front/back removals:")
my_list.print_values()
# Output:
# B
# C

# Remove a specific value
my_list.remove_val("B")
print("\nList after removing 'B':")
my_list.print_values()
# Output:
# C