a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list1 = []

for i in a:
	if (i % 2 == 0):
		list1.append(i)

print(list1)


b = [i for i in a if i%2 == 0]

print(b)
