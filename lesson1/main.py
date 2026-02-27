# *args - позиційні
# **kwargs - ключові

func = lambda x: x * 3
# print(func(3))

#map
a = [1,2,3,4,5]

multiply =list(map(lambda x: x * 3, a))
# print(multiply)

t = 'Hello'
repl = list(map(lambda x: x.replace('l', 'o'), t))
# print(repl)

l1 = [1,2,3,4,5,6,7,8]

even = list(filter(lambda x: x % 2 == 0, l1))
# print(even)
age = 18
odd = 'Adult' if age >= 18 else 'Minor'
# print(odd)

a = set('Hello')
# print(a)
b = set('Hi, there')

# print(a.union(b)) #об'єднання
# print(a.intersection(b)) # перетин
# print(b.difference(a)) #різниця
# print(a.symmetric_difference(b))

t1 = (1,2,3,4,[5,6,7])
# print(t1)
t1[4].append(8)
t2 = t1[4]
# print(t2)

d1 = {
    'name' : 'John',
    123: 'ololo',
    (1,2,3) : 'John'
}


def out_func(x):
    def in_func(y):
        return x + y
    return in_func

clos = out_func(5)
print(clos(10))

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time} секунд")
        return result
    return wrapper

@timer
def some_function():
    for _ in range(1000000):
        pass

some_function()