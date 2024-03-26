# deque objects are like double-ended queues

import collections
import string


d = collections.deque(string.ascii_lowercase)

print(f"Item Count: {len(d)}")

for elem in d:
    print(elem.upper())

d.pop()
d.popleft()
d.append(2)
d.appendleft(1)
print(d)

d.rotate(1)
print(d)