import random

user = int(input("Enter the random number to guess from 1 to 9"))

a = int(random.randint(1,9))
print(a)
print(type(a))

if (user > a):
	print("Guessed too high")
elif (user < a):
	print("Guessed too low")
else:
	print("Guessed exactly right")
