import random
random.seed()

x = random.randint(-5, 5)
print("x: ", x)

if x > 0:
    print("Diese Zahl ist positiv")
elif x < 0:
    print("Diese Zahl ist negativ")
else:
    print("Zahl ist 0")