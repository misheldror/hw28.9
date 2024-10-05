
l1: list[int] = [i for i in range(95, 106)]
print(l1)
l2: list[int] = [i for i in range(10, 21, 2)]
print(l2)
import random
l3: list[int] = []
l4: list[int] = [random.randint(1, 100) for i in range(10)]
print(l4)
l5: list[int] = [i for i in l4 if i > 50]
print(l5)
l6: list[int] = [random.randint(10, 99) for i in range(10)]
