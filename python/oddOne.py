"""
Find the element which appears only once in an array. Eg 4 in this case.
This is done using the XOR approach. 
"""


def program(arr: list) -> int:
    result = 0
    for element in arr:
        result = result ^ element
    return None if result == 0 else result


arr = [1, 4, 3, 1, 3]
print(program(arr))
