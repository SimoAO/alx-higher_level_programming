#!/usr/bin/python3
def weight_average(my_list=[]):
    n1 = 0
    n2 = 0
    if my_list:
        for i in my_list:
            n1 += i[0] * i[1]
            n2 += i[1]
        return (n1 / n2)
    return (0)
