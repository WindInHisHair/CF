#!/bin/python 

def split_array():
	a = int(raw_input().strip())
	ar = map(int, raw_input().strip().split())

	tb = [[0 for _ in range(a)] for _ in range(a)]

	for i in range(a):
		for j in range(i, a):
			if i == j:
				tb[i][j] = ar[i]
			else:
				tb[i][j] = sum(ar[i:j+1])


	k = 0
	head = 0
	tail = 0
	res = []
	possible = True
	if tb[0][a-1] != 0:
		print 'YES'
		print 1
		print '%s %s' %(1, a)
		return 
		
	while tail < a:
		if tail == a -1:
			if tb[head][tail] == 0:
				possible = False
				break
			else:
				res.append([head+1, tail+1])
				k += 1
				tail += 1
		else:
			if tb[head][tail] == 0:
				tail += 1
			else:
				res.append([head+1, tail+1])
				head = tail+1
				tail = tail +1
				k += 1

	if not possible:
		print "NO"
	else:
		print 'YES'
		print k
		for each in res:
			print ' '.join(map(str, each))


if __name__ == '__main__':
	split_array()
