#Из первой половины целочисленной последовательности a(n) удалить все простые числа.
#(Простое число - натуральное число, которое делится на единицу и на само себя.)
import random
import sympy

t = []
k = 0
while(k < 10):
    t.append(random.randint(1, 100))
    k+= 1
print(t)

for i in t[0:(int)(len(t)/2)]:
    if sympy.isprime(i):
        t.pop(t.index(i))

print(t)
