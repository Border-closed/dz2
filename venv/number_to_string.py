# Напишите программу, которая получает целое число и возвращает его
# шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def user_input():
    data_user = input('Введите целое число ')
    number_data = int(data_user)
    return number_data

def number_to_string(number_data):
    i = number_data
    DIVIDER = 16
    data_text = ''
    digits = '0123456789ABCDEF'
    while i % DIVIDER > 0 and i != 0:
        data_text = digits[i % DIVIDER] + data_text
        i = i // DIVIDER
    return data_text

def print_text(data_user, data_text):
    return print('Число ', data_user, ' в шестнадатиричном формате: ', data_text)

data = user_input()
print_text(data, number_to_string(data))
print('Проверка через функцию hex возвращает: ', hex(data)[2:].upper())