import random

list2 = []
len_list = random.randint(5,15)

while (len(list2) < len_list):
	list2.append(random.randint(1,75))

list2.sort()
evenlist = [i for i in list2 if i%2 == 0]
list3 = []
list3.append(evenlist)
for j in list3:
	list3.sort(reverse=True)

print(list3)
print(list2)
print(evenlist)
