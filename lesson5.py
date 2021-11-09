# Дз6 Списки

import random
a = [random.randint(1, 10) for _ in range(15)]
print(a) #для проверки начального списка
b = [random.randint(1, 10) for _ in range(15)]
print(b) #для проверки начального списка
c = list(set(a) & set(b)) #основной код
print(c)  #основной код
print(len(c))  #основной код
unique_numbers_a = list(set(a))
print(unique_numbers_a) #для проверки списка с уникальными числами
unique_numbers_b = list(set(b))
print(unique_numbers_b) #для проверки списка с уникальными числами
