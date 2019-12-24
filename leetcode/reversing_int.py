def reverse_int(x):
    neg_limit = -0x80000000
    pos_limit = 0x7fffffff
    if x < 0:
        string = str(x)
        dash = string[0]
        string = string.replace('-','')
        ans = dash + string

    else:
        string = str(x)
        return int(string[::-1])

    if x < 0:
        val = x & neg_limit
        if val == neg_limit:
            return x
        else:
            return 0
    elif x == 0:
        return x
    else:
        val = x & pos_limit
        if val == x:
            return x
        else:
            return 0

    # string = str(x)
    # if string[0] == '-':
    #     dash = string[0]
    #     string = string.replace('-','')
    #     ans = dash + string[::-1]
    #     return int(ans)
    # else:
    #     return int(string[::-1])




if __name__ == '__main__':
    print(reverse_int(-123))