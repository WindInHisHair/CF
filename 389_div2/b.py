#!/bin/python

def check():
	s = raw_input().strip()
	t = raw_input().strip()

	if len(set(s)) != len(set(t)):
		return -1
		
	l = len(s)

	d = {}
	for i in range(l):
		if not d.get(s[i], None):
			d[s[i]] = t[i]
			if s[i] != t[i]:
				d[t[i]] = s[i]
		else:			
			if d[s[i]] != t[i] or d[t[i]] != s[i]:
				return -1


	if len(d) == 0:
		return 0
	else:
		d_keys = set(d.keys())
		removed = set()
		for k, v in d.items():
			if v in d_keys and k not in removed:
				removed.add(v)
			elif k == v:
				removed.add(v)

		for each in removed:
			del d[each]
		return d

def main():
	res = check()

	if isinstance(res, int):
		print res
	else:
		print len(res)
		for k, v in res.items():
			print k, v

if __name__ == '__main__':
	main()




