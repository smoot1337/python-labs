Лабораторна робота 17: Generators and Data structures
--- 
Мета роботи:
Метою даної роботи є розвиток практичних навичок створення та використання генераторів у мові програмування Python. Завдання охоплюють різноманітні аспекти роботи з генераторами, що дозволить студентам зрозуміти їхню потужність та гнучкість у різних контекстах, включаючи обробку числових послідовностей, роботу з деревами та графами, маніпуляцію зі структурами даних та роботу з файлами.
---
Опис завдання: 
Generators and Data structures
Task 1: Create a generator to iterate over a list of
numbers.
Create a generator function named number_generator that takes a list of
numbers and yields each number one by one.
Task 2: Develop a generator that yields even numbers
from a given range.
Create a generator function named even_number_generator that takes two
integers, start and end , and yields even numbers within that range.
Example of function usage:
Task 3: Implement a generator to yield odd numbers
within a specified range.
Create a generator function named odd_number_generator that takes two
integers, start and end , and yields odd numbers within that range.
Task 4: Write a generator that produces Fibonacci
numbers.
Create a generator function named fibonacci_generator that produces
Fibonacci numbers indefinitely.
Example of function usage:
Task 5: Create a generator that yields prime numbers
up to a given limit.
Create a generator function named prime_number_generator that takes an
integer limit and yields prime numbers up to that limit.
Example of function usage:
Task 6: Develop a generator to traverse a binary tree in
pre-order.
Create a generator function named pre_order_traversal that takes the root of
a binary tree and yields its nodes in pre-order.
Task 7: Implement a generator for in-order traversal of
a binary tree.
Create a generator function named in_order_traversal that takes the root of a
binary tree and yields its nodes in in-order.
Example of function usage:
Task 8: Write a generator for post-order traversal of a
binary tree.
Create a generator function named post_order_traversal that takes the root of
a binary tree and yields its nodes in post-order.
Task 9: Create a generator to traverse a graph using
depth-first search (DFS).
Create a generator function named dfs_traversal that takes an adjacency list
representation of a graph and a starting node, and yields nodes in DFS order.
Task 10: Develop a generator for breadth-first search
(BFS) traversal of a graph.
Create a generator function named bfs_traversal that takes an adjacency list
representation of a graph and a starting node, and yields nodes in BFS order.
Task 11: Implement a generator that yields the keys of a
dictionary.
Create a generator function named dict_keys_generator that takes a dictionary
and yields its keys one by one.
Task 12: Write a generator that yields the values of a
dictionary.
Create a generator function named dict_values_generator that takes a
dictionary and yields its values one by one.
Task 13: Create a generator to iterate over key-value
pairs of a dictionary.
Create a generator function named dict_items_generator that takes a
dictionary and yields its key-value pairs as tuples one by one.
Example of function usage:
Task 14: Develop a generator that yields lines from a
file one by one.
Create a generator function named file_lines_generator that takes a file path
and yields its lines one by one.
Example of function usage:
Task 15: Implement a generator to iterate over words in
a text file.
Create a generator function named file_words_generator that takes a file path
and yields its words one by one.
Task 16: Write a generator that yields characters from a
string one by one.
Create a generator function named string_chars_generator that takes a string
and yields its characters one by one.
Task 17: Create a generator to yield unique elements
from a list.
Create a generator function named unique_elements_generator that takes a list
and yields its unique elements one by one.
Task 18: Develop a generator that yields elements of a
list in reverse order.
Create a generator function named reverse_list_generator that takes a list
and yields its elements in reverse order.
Task 19: Implement a generator to yield the Cartesian
product of two lists.
Create a generator function named cartesian_product_generator that takes
two lists and yields the Cartesian product of the two lists as tuples.
Example of function usage:
Task 20: Write a generator that yields permutations of a
list.
Create a generator function named permutations_generator that takes a list
and yields all possible permutations of the list.
Example of function usage:
Task 21: Create a generator to yield combinations of a
list of elements.
Create a generator function named combinations_generator that takes a list of
elements and yields all possible combinations of the elements.ge:
Task 22: Develop a generator to iterate over a list of
tuples.
Create a generator function named tuple_list_generator that takes a list of
tuples and yields each tuple one by one.
Task 23: Implement a generator that yields elements
from multiple lists in parallel.
Create a generator function named parallel_lists_generator that takes
multiple lists and yields elements from each list in parallel.
Task 24: Write a generator that yields elements from a
nested list (flattening the list).
Create a generator function named flatten_list_generator that takes a
nested list and yields each element in a flat sequence.
Task 25: Create a generator to yield elements from a
nested dictionary.
Create a generator function named nested_dict_generator that takes a nested
dictionary and yields its elements.
Task 26: Develop a generator to yield powers of 2 up to
a given number.
Create a generator function named powers_of_two_generator that takes an
integer n and yields powers of 2 up to 2^n .
Task 27: Implement a generator that yields powers of a
given base up to a specified limit.
Create a generator function named powers_of_base_generator that takes a
base and a limit, and yields powers of the base up to the specified limit.
Task 28: Write a generator to yield the squares of
numbers in a given range.
Create a generator function named squares_generator that takes a range of
numbers and yields their squares.
Task 29: Create a generator to yield cubes of numbers
in a specified range.
Create a generator function named cubes_generator that takes a range of
numbers and yields their cubes.
Task 30: Develop a generator that yields factorials of
numbers up to a given limit.
Create a generator function named factorials_generator that takes an integer
n and yields factorials of numbers from 0 up to n .:
Task 31: Implement a generator to yield numbers in the
Collatz sequence.
Create a generator function named collatz_sequence_generator that takes an
integer and yields numbers in the Collatz sequence.
Example of function usage:
Task 32: Write a generator that yields numbers in a
geometric progression.
Create a generator function named geometric_progression_generator that
takes an initial term, a common ratio, and a limit, and yields numbers in the
geometric progression.
Example of function usage:
Task 33: Create a generator to yield numbers in an
arithmetic progression.
Create a generator function named arithmetic_progression_generator that
takes an initial term, a common difference, and a limit, and yields numbers in the
arithmetic progression.
Task 34: Develop a generator that yields the running
sum of a list of numbers.
Create a generator function named running_sum_generator that takes a list of
numbers and yields their running sum.e:
Task 35: Implement a generator to yield the running
product of a list of numbers.
Create a generator function named running_product_generator that takes a list
of numbers and yields their running product.
---
Виконання роботи:
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from itertools import permutations, combinations
import math

def number_generator(numbers):
    for number in numbers:
        yield number

def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_number_generator(limit):
    num = 2
    while num <= limit:
        if is_prime(num):
            yield num
        num += 1

def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val

def dfs_traversal(graph, start):
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph[node]))

def bfs_traversal(graph, start):
    queue = deque([start])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])

def dict_keys_generator(dictionary):
    for key in dictionary:
        yield key

def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def string_chars_generator(string):
    for char in string:
        yield char

def unique_elements_generator(lst):
    seen = set()
    for element in lst:
        if element not in seen:
            seen.add(element)
            yield element

def reverse_list_generator(lst):
    for element in reversed(lst):
        yield element

def cartesian_product_generator(list1, list2):
    for item1 in list1:
        for item2 in list2:
            yield (item1, item2)

def permutations_generator(lst):
    for perm in permutations(lst):
        yield perm

def combinations_generator(lst):
    n = len(lst)
    for r in range(1, n + 1):
        for combo in combinations(lst, r):
            yield combo

def tuple_list_generator(lst):
    for tup in lst:
        yield tup

def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items

def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

def powers_of_base_generator(base, limit):
    power = 0
    result = base ** power
    while result <= limit:
        yield result
        power += 1
        result = base ** power

def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

def factorials_generator(n):
    for i in range(n + 1):
        yield math.factorial(i)

def collatz_sequence_generator(start):
    while start != 1:
        yield start
        if start % 2 == 0:
            start //= 2
        else:
            start = 3 * start + 1
    yield 1

def geometric_progression_generator(a, r, limit):
    term = a
    while term <= limit:
        yield term
        term *= r

def arithmetic_progression_generator(a, d, limit):
    term = a
    while term <= limit:
        yield term
        term += d

def running_sum_generator(numbers):
    running_sum = 0
    for num in numbers:
        running_sum += num
        yield running_sum

def running_product_generator(numbers):
    running_product = 1
    for num in numbers:
        running_product *= num
        yield running_product
```
---
Висновки: Після написання цього коду я значно покращив свої навичкі у Python.
---
