# Условие
# На вход подается: список целых чисел arr

# Задача
# Реализовать императивную функцию, которая возвращает три числа:
# Долю позитивных чисел
# Долю нулей
# Долю отрицательных чисел
def Imperative(array):
    pozitiv = 0
    negativ = 0
    zero = 0
    for i in array:
        if i > 0:
            pozitiv += 1
        elif i < 0 :
            negativ += 1
        else:
            zero += 1
    pozitiv = pozitiv / len(array)
    negativ = negativ / len(array)
    zero = zero / len(array)
    return pozitiv, negativ, zero

print(Imperative([1,4,0,-8,-5,0,1,2,-4,0]))