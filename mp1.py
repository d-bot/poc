"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    new_line = move(line)
    return replace_dups(new_line)



def move(array):
    """
    Move 0s at the end of array
    """
    new_array = list(array)

    for value in array:
        if value == 0:
            new_array.remove(0)
            new_array.append(0)

    return new_array


def replace_dups(array):
    """
    slide pairs
    """
    for index, value in enumerate(array):
        idx = (index+1) % len(array)
        if idx != 0:
            if value == array[idx]:
                value += array[idx]
                array[index] = value
                del array[idx]
                array.append(0)

    return array




print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])
