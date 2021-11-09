# Дз7 Списки
import random
a = [random.randint(1, 10) for _ in range(15)]
print(a)
b = len([i for i in a if (a[i+1] > a[i] and a[i+1] > a[i+2])])
print(b)

"""b = []
a = [random.randint(1, 10) for _ in range(15)]
print(a)
if all(i for i in a if (i+1) > i):
    b = [i for i in a if (i+1) > 8]
    print(b)
    print(len(b))"""


