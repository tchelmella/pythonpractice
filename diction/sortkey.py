d = {5:10,1:1,5:5,9:18,3:9}

d2 = dict(sorted(d.items()))

for i in d2:
#	print(i,j)
	print("%s %s" % (i,d[i]))
