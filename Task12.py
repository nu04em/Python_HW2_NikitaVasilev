# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

from random import randint
import math

first_number = randint(1, 1000)
second_number = randint(1, 1000)
print(f'Петя загадал числа: {first_number} и {second_number}')

sum = first_number + second_number
composition = first_number * second_number
print(f'Сумма загаданных чисел равна: {sum}\nПроизведение загаданных чисел равно: {composition}')

# Первый вариант без использования циклов, через теорему Виета

# first_number = math.ceil(sum + (sum**2 - 4 * composition)**0.5) // 2
# second_number = math.ceil(sum - (sum**2 - 4 * composition)**0.5) // 2
# print(f'\nЗагаданные Петей числа: {first_number} и {second_number}')

# Второй вариант с циклами

for first_num_katya in range(1, 1000):
    sec_num_katya = sum - first_num_katya
    if first_num_katya <= sec_num_katya and first_num_katya*sec_num_katya == composition:
        print(f'\nЗагаданные Петей числа: {first_num_katya} и {sec_num_katya}')
        break

