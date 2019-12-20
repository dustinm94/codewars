def minimum_bribes(q):
    bribe_count = 0
    for i, j in enumerate(q):
        if (j - 1) - i > 2:
            return "Too Chaotic"
    for i in range(q[i] - 1):
        print(i)

if __name__ == '__main__':
    print(minimum_bribes([2,5,1,3,4]))
    print(minimum_bribes([2,1,5,3,4]))