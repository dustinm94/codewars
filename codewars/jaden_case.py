def toJadenCase(string):
    # ...
    splitter = string.split(' ')
    lst = []
    for i in splitter:
        print(i)
        if i[0].isupper() != True:
            i = i.capitalize()
            lst.append(i)
        else:
            lst.append(i)

    print(lst)
    return ' '.join(lst)