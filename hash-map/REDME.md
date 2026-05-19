
# Custom HashMap Implementation in Python

A clean and efficient Python implementation of a custom **HashMap** (`MyHashMap`) from scratch, designed without using any built-in dictionary libraries. This implementation handles integer key-value pairs and manages collisions effectively.

---

## Features & Methods

The `MyHashMap` class supports the following core operations:

* **`put(key, value)`**: Inserts a `(key, value)` pair into the HashMap. If the `key` already exists, its corresponding `value` is updated.
* **`get(key)`**: Returns the value to which the specified `key` is mapped, or `-1` if this map contains no mapping for the key.
* **`remove(key)`**: Removes the mapping for the specified `key` and its corresponding value if the map contains the mapping.

---

## Design Strategy

* **Bucket Array:** Uses a fixed-size list of `2069` buckets (a prime number to optimize data distribution and minimize collisions).
* **Collision Handling:** Implements **Chaining (Separate Chaining)** via nested Python lists at each index.
* **Hash Function:** Employs a standard modulo operator: `hash(key) = key % size`.

