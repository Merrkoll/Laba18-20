import time
import sys

class Foo:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return self.city + " " + self.street

class Poo:
    def __init__(self, city, street):
        self.city = city
        self.street = street

    def __str__(self):
        return "{} {}".format(self.city, self.street)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factor(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

start_time = time.time()
inefficient_list = []
for i in range(100001):
    inefficient_list.append(i)
end_time = time.time()
print(f'Неэффективное время: {end_time - start_time}')
print(f'Неэффективное использование памяти: {sys.getsizeof(inefficient_list)} байт')

start = time.time()
efficient_list = list(range(100001))
end = time.time()
print(f'Эффективное время: {end - start}')
print(f'Эффективное использование памяти: {sys.getsizeof(efficient_list)} байт\n')

st_time = time.time()
a = factorial(928)
en_time = time.time()
print(f'Неэффективное время: {en_time - st_time}')
print(f'Неэффективное использование памяти: {sys.getsizeof(factorial)} байт')

s_time = time.time()
b = factor(928)
e_time = time.time()
print(f'Эффективное время: {e_time - s_time}')
print(f'Эффективное использование памяти: {sys.getsizeof(factor)} байт\n')

Start_time = time.time()
for i in range(10001):
    c = Foo("Москва", "Набережная")
    c.__str__()
End_time = time.time()
print(f'Неэффективное время: {End_time - Start_time}')
print(f'Неэффективное использование памяти: {sys.getsizeof(Foo)} байт')

starttime = time.time()
for i in range(10001):
    d = Poo("Москва", "Набережная")
    d.__str__()
endtime = time.time()
print(f'Эффективное время: {endtime - starttime}')
print(f'Эффективное использование памяти: {sys.getsizeof(Poo)} байт')