def up_array(arr):
    for i in arr:
        if i < 0 or i > 9:
            return nil
    y = "".join(str(n) for n in arr)
    y = int(y)
    y = y + 1

    newNumber = [int(a) for a in str(y)]
    return newNumber

up_array([2,3,9])