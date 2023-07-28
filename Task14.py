# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

num_n = int(input('Введите число N: '))

degree_k = 0
result = 1
while result <= num_n + 1:
    print(f'2^{degree_k} = {result}')
    degree_k += 1
    result = 2 ** degree_k