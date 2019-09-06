d = {'A':5,'B':5,'C':7,'D':9,'E':1}

#print(d.fromkeys('A'))
#print(d.get('C'))
#print(d.items())
#print(d.keys())
#print(d.values())

dic = {}

for i,j in d.items():
	if j not in dic.values():
		dic[i] = j

print(dic)

print(dict(set(d.items())))
