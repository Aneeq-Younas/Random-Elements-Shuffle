
import random

order_of_alphabet= ["a ", "b ", "c ", "d ", "e ", "f ", "g ", "h ",
                    "k ", "l ", "m ", "n ", "o ", "p ", "q ", "r ", "s ", "t ",
                    "u ", "v ", "w ", "x ", "y ", "z "]
order_of_numbers= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

random.shuffle(order_of_alphabet)
random.shuffle(order_of_numbers)
print(" ".join(order_of_alphabet))
print(order_of_numbers)
