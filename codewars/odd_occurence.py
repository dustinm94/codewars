def odds(arr):
    leng = len(arr)
    for i in range(0, leng):
        count = 0
        for j in range(0, leng):
            if arr[i] == arr[j]:
                count += 1
        if count % 2 != 0:
            return arr[i]


def main():
    arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 4, 4, 2]
    print(odds(arr))
main()