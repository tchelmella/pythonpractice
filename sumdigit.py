def sumdigit(i):
	sum = 0
	while i:
		sum = sum + i % 10
		i = i//10

	return sum

num = int(input("Enter the number"))
print(sumdigit(num))
