a = [1, 5, 8, 3]
b = [1, 5, 8, 3]

def grpval(a,n):
	if (n in a):
		return True
	else:
		return False

print(grpval(a,5))
print(grpval(a,-1))
