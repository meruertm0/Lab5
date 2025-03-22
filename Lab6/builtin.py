from functools import reduce
import time
import math

def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

def is_palindrome(s):
    return s == s[::-1]

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}")

def all_true(tpl):
    return all(tpl)

# Example usage:
print(multiply_list([1, 2, 3, 4]))
print(count_case("Hello World"))
print(is_palindrome("radar"))
delayed_sqrt(25100, 2123)
print(all_true((True, True, False)))
