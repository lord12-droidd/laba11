"""а) Дан текстовий файл f. Видалити з нього останній рядок, результат записати у
файл g.
Мельник Д.В. 122А
"""
import random

with open('f.txt', 'w+') as f:
    sample = ['Python', 'top', 'za', 'svoi', 'money']
    for i in range(5):  # згенеруємо 5 рядків, в кожному по 5 слів у рандомному порядку
        f.write(' '.join((random.choices(sample, k = 5))) + '\n')


with open('f.txt', 'r') as f:  # Відкриваємо текстовий файл f для читання
    lines = f.readlines()  # Зчитуємо всі рядки
    lines = lines[:-1]  # Видаляємо останній

with open('g.txt', 'w') as f:
    f.writelines(lines)  # Записуємо рядки,які залишились у файл g


g = open('g.txt', 'r')  # Відкриваємо текстовий файл для зчитування
print('Вміст файлу g: ',end = '\n\n')
print(g.read())  # Зчитуємо рядки та виводимо на екран
g = g.close()  # Закриваємо файли
f = f.close()
