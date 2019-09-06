d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
print(sum(d.values()))

dic = {'data1':100,'data2':-54,'data3':247}
print(sum(dic.values()))

prod = 1
for i in dic.values():
	prod = prod *i

print(prod)
