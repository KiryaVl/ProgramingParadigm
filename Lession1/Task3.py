def Declarative(array):
    pozitiv = len(list(filter(lambda x: x > 0, array))) 
    negativ = len(list(filter(lambda x: x < 0, array))) 
    zero = len(list(filter(lambda x: x == 0, array))) 
    count = [pozitiv, negativ, zero]
    return list(map(lambda x: x/len(array), count))


print(Declarative([1,4,0,-8,-5,0,1,2,-4,0]))