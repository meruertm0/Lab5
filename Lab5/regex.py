import re

with open("row.txt", "r", encoding="utf-8") as file:
    tests = file.read().splitlines()

#Task 1
def match_pattern_1(s):
    pattern = r'^a*b*$'
    return bool(re.fullmatch(pattern, s))

for test in tests:
    print(f"'{test}':{match_pattern(test)}")
    

#Task 2
def match_pattern(s):
    pattern = r'^ab{2,3}$'
    return bool(re.fullmatch(pattern, s))

for test in tests:
    print(f"'{tests}': {match_pattern(test)}")

#Task 3
def find_low_und(s):
    return re.findall(r'\b[a-z]+_[a-z]+\b', s)

#Task 4
def find_up_low(s):
    return re.findall(r'\b[A-Z][a-z]+\b', s)

#Task 5
def match_a_b(s):
    return bool(re.fullmatch(r'a.*b', s))

#Task 6
def replace_chars(s):
    return re.sub(r'[ ,.]', ':', s)

#Task 7
def snake_to_camel(s):
    return ''.join(word.capitalize() if i != 0 else word for i, word in enumerate(s.split('_')))

#Task 8
def split_upper(s):
    return re.findall(r'[^A-Z]*[A-Z][^A-Z]*', s)

#Task 9
def space_caps(s):
    return re.sub(r'(?<=[a-z])([A-Z])', r' \1', s)

#Task 10
def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

for test in tests:
    print(f"Lowercase with underscore: {find_low_und(test)}")
    print(f"Uppercase followed by lowercase: {find_up_low(test)}")
    print(f"Matches a.*b: {match_a_b(test)}")
    print(f"Replaced special chars: {replace_chars(test)}")
    print(f"Snake to Camel: {snake_to_camel(test)}")
    print(f"Split at uppercase: {split_upper(test)}")
    print(f"Inserted spaces between capitals: {space_caps(test)}")
    print(f"Camel to Snake: {camel_to_snake(test)}")
    
