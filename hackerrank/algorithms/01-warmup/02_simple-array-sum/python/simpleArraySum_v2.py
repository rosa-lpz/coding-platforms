import sys

def simpleArraySum(n, ar):
    sum = 0
    for i in ar:
        sum += i
    return sum

if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().strip().split(' ')))
    print("array: ", ar)
    result = simpleArraySum(n, ar)
    print(result)
