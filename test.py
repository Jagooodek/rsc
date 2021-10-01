import random
def is_sorted(x):
    for i in range(1, len(x)):
        if x[i] < x[i-1]:
            return False
    return True

x = [random.randrange(1000) for _ in range(20)]
print(x)
while is_sorted(x) is False:
    random.shuffle(x)
print(x)

