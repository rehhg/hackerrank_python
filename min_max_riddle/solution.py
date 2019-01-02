import math
import os


def max_of_minima_for_every_window_size(arr):
    """
    Returns an array to satisfy the min max riddle
    Given an integer array of size n, find the maximum of the minimum(s) of every window size in the array.
    The window size varies from 1 to n.
    """

    results = [None] * len(arr)
    inverted_map = inverted_max_window(arr)
    print("inverted_map {}".format(inverted_map))

    prev_largest_window_max = inverted_map[max(inverted_map.keys())]

    for window_size in range(len(results),  0,  -1):
        print("prev_largest_window_max {}".format(prev_largest_window_max))
        print("window_size {}".format(window_size))
        if window_size in inverted_map:
            results[window_size - 1] = inverted_map[window_size]
            prev_largest_window_max = inverted_map[window_size]
        else:
            results[window_size - 1] = prev_largest_window_max

    return results


def inverted_max_window(arr):
    """
    Return a map from window_size -> maximum_value
    """

    inverted_windows = dict()
    max_window = largest_window_map(arr)

    for max_value, window_size in max_window.items():
        if window_size not in inverted_windows:
            inverted_windows[window_size] = max_value
        else:
            inverted_windows[window_size] = max(inverted_windows[window_size], max_value)

    print("inverted_max_window {}".format(inverted_windows))
    return inverted_windows


def largest_window_map(arr):
    max_window = dict()
    largest_window = largest_minima_window(arr)
    for number, window in zip(arr, largest_window):
        if number not in max_window:
            max_window[number] = window
        else:
            max_window[number] = max(max_window[number], window)

    print("max_window {}".format(max_window))
    return max_window


def largest_minima_window(arr):
    left_window = largest_window_left(arr)
    right_window = largest_window_right(arr)
    print ("left_window {}, right_window {}".format(left_window, right_window))
    largest_minimal_window = []

    for left, right in zip(left_window, right_window):
        largest_minimal_window.append(left + right - 1)

    print ("largest_minima_window: {}".format(largest_minimal_window))
    return largest_minimal_window


def largest_window_left(arr):
    # Initialize a list to capture the number of elements to the left of the current value
    # for which the current value is the minimum.
    num_elements_minimum = [None] * len(arr)
    # The first element always has a span of one because nothing comes before it.
    num_elements_minimum[0] = 1
    # Use a stack to store the index of the last element smaller than the current element.
    index_of_last_min_element = [0]

    for index in range(1, len(arr)):
        while len(index_of_last_min_element) > 0 and arr[index] <= arr[index_of_last_min_element[-1]]:
            index_of_last_min_element.pop()

        if len(index_of_last_min_element) == 0:
            num_elements_minimum[index] = index + 1
        else:
            num_elements_minimum[index] = index - index_of_last_min_element[-1]

        index_of_last_min_element.append(index)
        print("num_elements_minimum {}, index_of_last_min_element {}".format(num_elements_minimum,
                                                                             index_of_last_min_element))

    return num_elements_minimum


def largest_window_right(arr):
    return list(reversed(largest_window_left(list(reversed(arr)))))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    _num_elements = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = max_of_minima_for_every_window_size(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
