import os
import random
import re
import sys


# Complete the funGame function below.
def funGame(a, b, n):
    s = [a[x] + b[x] for x in range(n)]
    add = c = 0
    for i in range(n):
        index = s.index(max(s))
        if c == 0: add += a[index]
        if c == 1: add -= b[index]
        s.pop(index)
        a.pop(index)
        b.pop(index)
        c = 1 - c
    if add > 0:
        print('First')
        return "First"
    elif add < 0:
        print('Second')
        return "Second"
    else:
        print('Tie')
        return "Tie"


if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'test1.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = funGame(a, b, n)

        fptr.write(result + '\n')

    fptr.close()
