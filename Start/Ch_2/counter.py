# Demonstrate the usage of Counter objects

from collections import Counter


# list of students in class 1
class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
          "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

# list of students in class 2
class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
          "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

c1 = Counter(class1)
c2 = Counter(class2)

print(c1["James"])

print(sum(c1.values()),"students in class 1")

c1.update(class2)
print(sum(c1.values()),"students in class 1 after class 2 added")

print(c1.most_common(3))

c1.subtract(c2)

print(c1 & c2," is the intersection")
