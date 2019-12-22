def array_of_array_products(arr):
    products = []
    if len(arr) <= 1:
        return products
    for i, j in enumerate(arr):
        if not arr:
            return products

        if i == arr[i + 1]:
            return arr

        products.append(j * arr[i - 1])

    return products


print(array_of_array_products([1]))


print(array_of_array_products([2, 2]))