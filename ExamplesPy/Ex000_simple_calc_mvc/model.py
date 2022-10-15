value_a = 0
value_b = 0

def init(a, b):
    global value_a
    global value_b
    value_a = a
    value_b = b


def sum_two_num():
    return value_a + value_b


def sub_two_num():
    return value_a - value_b 


def mult_two_num():
    return value_a * value_b 


def div_two_num():
    return value_a / value_b


def div_int_two_num():
    return value_a // value_b


def div_mod_two_num():
    return value_a % value_b