val1 = int(input("Enter value1"))
val2 = int(input("Enter value2"))
val3 = int(input("Enter value3"))

m1 = min(val1,val2,val3)
m2 = max(val1,val2,val3)
m3 = (val1+val2+val3) - m1 - m2

print("Numbers in sorted order: ", m1, m3, m2)
