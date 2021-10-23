from math import e
import random
champion = ['c','h','a','m','p','i','o','n']
random.shuffle(champion)
meticulous = ['m','e','t','i','c','u','l','o','u','s']
random.shuffle(meticulous)
hexagon = ['h','e','x','a','g','o','n']
random.shuffle(hexagon)
word = [champion, meticulous, hexagon]
print(random.choice(word))
guess = str(input("Your answer: "))
if guess == "champion":
    print('👍')
elif guess == "meticulous":
    print('👍')
elif guess == "hexagon":
    print('👍')
else:
    print('👎')