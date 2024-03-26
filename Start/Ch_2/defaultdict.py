# Demonstrate the usage of defaultdict objects

from collections import defaultdict


# define a list of items that we want to count
fruits = ['apple', 'pear', 'orange', 'banana',
          'apple', 'grape', 'banana', 'banana']

#fruitCounter = defaultdict(int)
fruitCounter = defaultdict(lambda: 0)

for fruit in fruits:
    fruitCounter[fruit] += 1

print(fruitCounter)