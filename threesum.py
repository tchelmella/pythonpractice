def three(a,b,c):
	if (a==b or a==c or b==c):
		return 0
	else:
		return a+b+c

print(three(1,2,3))
print(three(1,1,2))
