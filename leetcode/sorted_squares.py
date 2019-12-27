def sortedSquares(self, A: [int]) -> [int]:
    ans = []
    for num in A:
        num = num * num
        ans.append(num)
    ans.sort()
    return ans