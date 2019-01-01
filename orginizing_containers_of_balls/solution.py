import os


# Complete the organizingContainers function below.
def organizingContainers(container):
    col = set([sum(x) for x in zip(*container)])
    row = set([sum(y) for y in container])
    return 'Possible' if col == row else 'Impossible'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
