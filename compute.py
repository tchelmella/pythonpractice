val = int(input("Enter the value of n"))

n1 = int("%s" %val)
n2 = int("%s%s" %(val,val))
n3 = int("%s%s%s" %(val,val,val))
print(n1+n2+n3)
