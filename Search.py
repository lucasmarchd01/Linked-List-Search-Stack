"""
Name: Lucas March
ID: 20144315
CISC 235 Assignment 1 Q3
"""
import timeit
import random


def linearSearch(inputArr, x):
    """Linear search algorithm to find a given element in an array-based list and a list of values to search.
    :param inputArr: Array to search from
    :param x: Element to find in array
    :return: True if element was found.
    """
    # Search for each element in the list
    for i in inputArr:
        # Element was found
        if i == x:
            return True
    return False

def mergeSort(inputArr):
    """Merge Sort algorithm for a given array-based list.
    :param inputArr: Array to sort
    :return: Sorted array
    """
    if len(inputArr) > 1:

        # Find midpoint of the array
        mid = len(inputArr) // 2

        # Divide array into left side and right side
        Left = inputArr[:mid]
        Right = inputArr[mid:]

        # Sort the two halves
        mergeSort(Left)
        mergeSort(Right)

        i = 0
        j = 0
        k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                # Value from left is inserted
                inputArr[k] = Left[i]
                i += 1
            else:
                # Value from right is inserted
                inputArr[k] = Right[j]
                j += 1
            k += 1

        # For remaining values
        while i < len(Left):
            inputArr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            inputArr[k] = Right[j]
            j += 1
            k += 1

def binarySearch(inputArr, x):
    """Binary search algorithm for an array-based list and a list of values to search.
    :param inputArr: Array to search from
    :param x: Element to find
    :return: True if element was found
    """

    low = 0
    high = len(inputArr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # Take out left half if x is greater than mid
        if inputArr[mid] < x:
            low = mid + 1

        # Take out right half if x is less than mid
        elif inputArr[mid] > x:
            high = mid - 1

        # mid is x
        else:
            return True

    # Element was not found
    return False

def doBinSearch(Search, x_list):
    """
    Sort a list of values and search for each value in a list.
    :param Search: List of values to sort and search from.
    :param x_list: List of values to search.
    :return:

    """
    # Sort the list
    mergeSort(Search)

    # Search each element in the list of values
    for x in range(len(x_list)):
        binarySearch(Search, x_list[x])

def doLinSearch(Search, x_list):
    for x in range(len(x_list)):
        linearSearch(Search, x_list[x])

def k_list(k):
    """Generate a list of k values, half of which are in S and half of which are not.
    :param k: number of elements in list desired
    :return k_list: List of k values, half of which are in S and half of which are not.
    """
    l = []
    for i in range(k):
        if i % 2 == 0:
            l.append(random.randrange(10, 100000, 2))
        else:
            l.append(random.randrange(11, 100000, 2))
    return l


if __name__ == '__main__':

    # List for n = 1000
    S1 = random.sample(range(10, 100000, 2), 1000)
    SETUPLIN = 'from __main__ import doLinSearch, list_to_test, S1'
    STARTERLIN = 'doLinSearch(S1, list_to_test)'
    SETUPBIN = 'from __main__ import doBinSearch, list_to_test, S1'
    STARTERBIN = 'doBinSearch(S1, list_to_test)'

    # List for n = 5000
    S2 = random.sample(range(10, 100000, 2), 5000)
    SETUPLIN2 = 'from __main__ import doLinSearch, list_to_test, S2'
    STARTERLIN2 = 'doLinSearch(S2, list_to_test)'
    SETUPBIN2 = 'from __main__ import doBinSearch, list_to_test, S2'
    STARTERBIN2 = 'doBinSearch(S2, list_to_test)'

    # List for n = 10000
    S3 = random.sample(range(10, 100000, 2), 10000)
    SETUPLIN3 = 'from __main__ import doLinSearch, list_to_test, S3'
    STARTERLIN3 = 'doLinSearch(S3, list_to_test)'
    SETUPBIN3 = 'from __main__ import doBinSearch, list_to_test, S3'
    STARTERBIN3 = 'doBinSearch(S3, list_to_test)'

    k1 = 50
    while True:  # For n = 1000
        # Create a list of k values to search for
        list_to_test = k_list(k1)

        # Time linear and binary search
        linspeed = timeit.repeat(setup=SETUPLIN, stmt=STARTERLIN, repeat=3, number=10)
        binspeed = timeit.repeat(setup=SETUPBIN, stmt=STARTERBIN, repeat=3, number=10)

        # Check if binary search is faster
        if sum(binspeed) < sum(linspeed):
            print("for n = 1000, k =", k1)
            break
        k1 += 1

    k2 = 50
    while True:  # For n = 5000
        list_to_test = k_list(k2)
        linspeed = timeit.repeat(setup=SETUPLIN2, stmt=STARTERLIN2, repeat=3, number=10)
        binspeed = timeit.repeat(setup=SETUPBIN2, stmt=STARTERBIN2, repeat=3, number=10)
        if sum(binspeed) < sum(linspeed):
            print("for n = 5000, k =", k2)
            break
        k2 += 1

    k3 = 50
    while True:  # For n = 10000
        list_to_test = k_list(k3)
        linspeed = timeit.repeat(setup=SETUPLIN3, stmt=STARTERLIN3, repeat=3, number=10)
        binspeed = timeit.repeat(setup=SETUPBIN3, stmt=STARTERBIN3, repeat=3, number=10)
        if sum(binspeed) < sum(linspeed):
            print("for n = 10000, k =", k3)
            break
        k3 += 1