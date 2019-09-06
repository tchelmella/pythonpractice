d = {'a': [3, 4, 5], 'b': [1, 2, 3]}
for k, v in d.items():
	d[k] = sum(v) / len(v)

print(d)
