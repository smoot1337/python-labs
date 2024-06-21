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
