from functools import reduce
import time
import math
import os
import shutil

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

def list_files_dirs(path):
    return [f for f in os.listdir(path)]

def check_path_access(path):
    return {
        "exists": os.path.exists(path),
        "readable": os.access(path, os.R_OK),
        "writable": os.access(path, os.W_OK),
        "executable": os.access(path, os.X_OK)
    }

def check_path_existence(path):
    if os.path.exists(path):
        return os.path.basename(path), os.path.dirname(path)
    return None

def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return sum(1 for line in f)

def write_list_to_file(filename, lst):
    with open(filename, 'w') as f:
        f.writelines(f"{item}\n" for item in lst)

def generate_text_files():
    for letter in range(65, 91):
        with open(f"{chr(letter)}.txt", 'w') as f:
            f.write(f"File {chr(letter)}")

def copy_file(source, destination):
    shutil.copy(source, destination)

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):
        os.remove(path)

# Example usage:
print(multiply_list([1, 2, 3, 4]))
print(count_case("Hello World"))
print(is_palindrome("radar"))
delayed_sqrt(25100, 2123)
print(all_true((True, True, False)))
print(list_files_dirs("."))
print(check_path_access("test.txt"))
print(check_path_existence("test.txt"))
print(count_lines_in_file("test.txt"))
write_list_to_file("output.txt", ["one", "two", "three"])
generate_text_files()
copy_file("output.txt", "copy_output.txt")
delete_file("output.txt")
