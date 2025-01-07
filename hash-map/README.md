a hash map is an unordered data structure that stores key-value pairs. A hash map can add and remove elements in
O
(
1
)
O(1), as well as update values associated with a key and check if a key exists, also in
O
(
1
)
O(1). You can iterate over both the keys and values of a hash map, but the iteration won't necessarily follow any
order (there are many implementations and this is language dependent for the built-in types).

In terms of time complexity, hash maps blow arrays out of the water. The following operations are all
O
(
1
)
O(1) for a hash map:

Add an element and associate it with a value
Delete an element if it exists
Check if an element exists
A hash map also has many of the same useful properties as an array with the same time complexity:

Find length/number of elements
Updating values
Iterate over elements

### Disvantages

The biggest disadvantage of hash maps is that for smaller input sizes, they can be slower due to overhead. Because big O
ignores constants, the
O
(
1
)
O(1) time complexity can sometimes be deceiving - it's usually something more like
O
(
10
)
O(10) because every key needs to go through the hash function, and there can also be collisions, which we will talk
about in the next section.

Hash tables can also take up more space. Dynamic arrays are actually fixed-size arrays that resize themselves when they
go beyond their capacity. Hash tables are also implemented using a fixed size array - remember that the size is a limit
set by the programmer. The problem is, resizing a hash table is much more expensive because every existing key needs to
be re-hashed, and also a hash table may use an array that is significantly larger than the number of elements stored,
resulting in a huge waste of space. Let's say you chose your limit as 10,000 items, but you only end up storing 10.
Okay, you could argue that 10,000 is too large, but then what if your next test case ends up needing to store 100,000
elements? The point is, when you don't know how many elements you need to store, arrays are more flexible with resizing
and not wasting space.

### Collisions

When different keys convert to the same integer, it is called a collision. Without handling collisions, older keys will
get overridden and data will be lost. There are multiple ways to handle collisions, but here we'll talk about a common
one called chaining.

### Sets

A set is another data structure that is very similar to a hash table. It uses the same mechanism for hashing keys into integers. The difference between a set and hash table is that sets do not map their keys to anything. Sets are more convenient to use when you only care about checking if elements exist. You can add, remove, and check if an element exists in a set all in 
O
(
1
)
O(1).

An important thing to note about sets is that they don't track frequency. If you have a set and add the same element 100 times, the first operation adds it and the next 99 do nothing.