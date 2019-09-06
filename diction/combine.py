d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

from collections import Counter

d = Counter(d1) + Counter(d2)
print(d)

d3 = {}

for i in d1.keys():
	if i in d2.keys():
		d1[i] = d1[i] + d2[i]
		d2.pop(i)

for j in (d1,d2):
	d3.update(j)

print(d3)
