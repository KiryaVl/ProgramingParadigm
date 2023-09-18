def searchImperative(number, array):
    for i in range(len(array)):
        if array[i] == number:
            return True
    return False

print(searchImperative(5, [1,2,3,4,5]))