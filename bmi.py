def bmi(weight,height):
	bmi = round(weight/(height*height),2)
	return bmi

w = float(input("Enter the weight in kilograms"))
h = int(input("Enter the height metres"))
print(bmi(w,h))
