mydict={}
txt = open("sample.txt", "r")
for line in txt:
	words = line.split()
	for word in words:
		if word in mydict:
			mydict [word] += 1
		else:
			mydict[word] = 1
txt.close()
def freq(item):
	return item[1]
mylist = sorted(mydict.items(), key=freq, reverse=True)
for i in range(10):
	print(mylist[i][0], mylist[i][1])