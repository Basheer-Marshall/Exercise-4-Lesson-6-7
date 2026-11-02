fruits = ["apple", "bannana", "pear"]

for fruit in fruits:
    print(fruit)

countdown = 5

while countdown >= 1:
    print(countdown)
    countdown -= 1

for i in range(1, 11):
    square = i ** 2
    print(f"the square of {i} is {square}")

import random

colors = ["red", "blue", "green", "yellow", "purple", "orange"]

for i in range(3):
    random_color = random.choice(colors)
    print(random_color)