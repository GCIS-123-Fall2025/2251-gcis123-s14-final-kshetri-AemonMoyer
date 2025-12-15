from node_stack import Stack
from dict_queue import Queue

"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #4 (25 points)
Filename: even_digits.py

Define a function named "even_digits" that declares a parameter for an 
    integer. The function should return a copy of the integer with the odd
    digits removed. You MUST NOT convert the integer to/from a string, but 
    instead may only use basic arithmetic operators (e.g. %, //, etc.).

    Given Input     Expected Output
    1               0
    2               2
    34              4
    1234567890      24680

For credit your function must use a stack or a queue in a significant way.
    You must not use any other data structures. For full credit, your 
    implementation must run in linear time.
"""

def even_digits(integer):
    stack2 = Stack()
    stack1 = Stack()
    integer_length_tool = integer
    length = 0
    stacking_tool = 0
    answer = 0
    while integer_length_tool > 0:
        length += 1
        integer_length_tool = integer_length_tool//10
    for x in range(length):
        value = integer // (10**x)
        stack1.push(value)
    count_tool = length
    #count_tool is being used because is_empty was being weird
    while count_tool > 0:
        value = stack1.pop()
        new_value = value - stacking_tool*(10)
        stacking_tool = value
        count_tool -= 1
        stack2.push(new_value)
    count = 0
    for x in range(length):
        value = stack2.pop()
        if value % 2 == 0:
            answer = answer + value*(10*count)
            print(answer)
    



even_digits(1234567890)


# several test cases provided for even digits - 1, 2, 34, 1234567890
def test_even_digits_1():
    # setup
    integer = 1
    expected = 0
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_2():
    # setup
    integer = 2
    expected = 2
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_34():
    # setup
    integer = 34
    expected = 4
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual

def test_even_digits_1234567890():
    # setup
    integer = 1234567890
    expected = 24680
    # invoke
    actual = even_digits(integer)
    # analyze
    assert expected == actual