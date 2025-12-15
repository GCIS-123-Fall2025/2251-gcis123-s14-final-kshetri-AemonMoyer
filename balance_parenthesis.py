
"""
Course: GCIS 123 (2251)
Exam: Final Exam
Question: Question #3 (25 points)
Filename: balance_parenthesis.py

Complete the bracket balancing function below. It checks if (  and  ) brackets are balanced, using a stack.

Function returns 0 if brackets are balanced,
-1 if there are more closing brackets than needed,
and x otherwise, where x is the index of the most recent
unbalanced left bracket.

Examples:
"--(---(------)--"  returns  2 
"()----)" returns -1
"-----() -- ( () )" returns 0

"""
from node_stack import Stack

def balance_parenthesis(a_string):
    balance = 0
    recent = 0
    stack1 = Stack()
    for x in a_string:
        stack1.push(x)
    length = len(stack1)
    for x in range(length):
        value = stack1.pop()
        if value == '(':
            balance = balance + 1
            if balance > 0:
                recent = length-1-x
        if value == ")":
            balance = balance - 1
        else:
            continue
    if balance == 0:
        return 0
    if balance < 0:
        return -1
    if balance > 0:
        return recent


def main():
    print(balance_parenthesis("-----())() -- ( () )"))

if __name__ == "__main__":    main()