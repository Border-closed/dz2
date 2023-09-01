# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

def data_user():
    return input('Введите строку вида a/b ')

def data_text_split(data_user):
    return data_user.split('/')

def gcd (a, b): #наименьший общий делитель
    while b:
        a, b = b, a % b
    return a

def lcm (a, b): #наименьшее общее кратное
    return abs(a * b) // gcd(a, b)

def total(data_split_1, data_split_2):
    if data_split_1[1] == data_split_2[1]:
        numerator = int(data_split_1[0]) + int(data_split_2[0])
        result = str(numerator) + '/' + data_split_1[1]
    else:
        delimetr = lcm(int(data_split_1[1]), int(data_split_2[1]))
        dop_multi_1 = delimetr / int(data_split_1[1])
        dop_multi_2 = delimetr / int(data_split_2[1])
        numerator = int(data_split_1[0]) * int(dop_multi_1) + int(data_split_2[0]) * int(dop_multi_2)
        delimetr_1 = int(data_split_1[1]) * int(dop_multi_1)
        result = str(numerator) + '/' + str(delimetr_1)
    return result

def multiply(data_split_1, data_split_2):
    result = [int(data_split_1[0]) * int(data_split_2[0]), int(data_split_1[1]) * int(data_split_2[1])]
    return result

fraction1 = data_text_split(data_user())
fraction2 = data_text_split(data_user())
print('Произведение дроби ', fraction1[0], '/', fraction1[1], ' на ', fraction2[0], '/', fraction2[1], ' равно ',  multiply(fraction1, fraction2)[0], '/', multiply(fraction1, fraction2)[1])
print('Сумма дроби ', fraction1[0], '/', fraction1[1], ' и ', fraction2[0], '/', fraction2[1], ' равнa ', total(fraction1, fraction2))