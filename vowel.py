val = str(input("Enter the letter a-z or A-Z"))
print(val)

for i in val:
	if (i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O' or i == 'u' or i == 'U'):
		print(val + " is a vowel")
	else:
		print(val + " is a consonant")
