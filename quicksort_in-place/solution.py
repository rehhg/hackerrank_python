class QuickSort(object):
    def __init__(self, arr):
        self.arr = arr

    def sort(self, left_i, right_i):
        if right_i - left_i < 1:
            return
        pivot_i = self.partition(left_i, right_i)
        self.sort(left_i, pivot_i - 1)
        self.sort(pivot_i + 1, right_i)

    def partition(self, left_i, right_i):
        pivot_i = right_i
        lesser_i = left_i
        for i in range(left_i, right_i):
            if arr[i] < arr[pivot_i]:
                self.swap(i, lesser_i)
                lesser_i += 1
        self.swap(pivot_i, lesser_i)
        self.print_arr()
        return lesser_i

    def swap(self, index_1, index_2):
        arr[index_1], arr[index_2] = arr[index_2], arr[index_1]

    def print_arr(self):
        print(" ".join(list(map(str, arr))))


arr = list(map(int, input().strip().split(" ")))
quicksort = QuickSort(arr)
quicksort.sort(0, len(arr) - 1)
