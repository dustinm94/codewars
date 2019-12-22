def twoSum(arr, target):
    idxes = {}

    for i, k in enumerate(arr):
        if target - k in idxes:
            return [idxes[target-k], i]
        else:
            idxes[k] = i

if __name__ == '__main__':
    print(twoSum([3, 2, 4], 6))
