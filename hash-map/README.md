# Hash Map

A hash map is a data structure that stores key-value pairs with O(1) time complexity for basic operations.

## Key Operations & Time Complexity

- Add element: O(1)
- Remove element: O(1)
- Update value: O(1)
- Check if key exists: O(1)
- Find length: O(1)

## Advantages

- Fast operations (constant time)
- Flexible key types
- Direct access to values
- Useful for caching and counting

## Disadvantages®

- Higher memory usage
- Performance overhead for small datasets
- Expensive resizing operations
- Potential for collisions®

## Collisions

Collisions occur when different keys hash to the same value. Common solution:

- Chaining: Store multiple key-value pairs in linked lists at each array position

## Related: Sets

- Similar to hash maps but only store keys (no values)
- Used when only existence checking is needed
- All operations are O(1)
- Duplicates are automatically handled (only stored once)çççÇÇÇ 
