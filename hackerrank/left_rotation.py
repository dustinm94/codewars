def left_rotation(a,d):
    count = 0
    while count < d:
        first = a.pop(0)
        a.append(first)
        count += 1
        print(a)
    return a

if __name__ == '__main__':
    left_rotation([1,2,3,4,5],4)