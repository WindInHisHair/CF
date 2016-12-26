#!/bin/python

def check():
	s = raw_input().strip()
	t = raw_input().strip()

	l = len(s)

	d = {}
	for i in range(l):
		if s[i] == t[i]:
			continue

		if not d.get(s[i], None):
			d[s[i]] = t[i]
		else:
			if d[s[i]] != t[i]:
				return -1


	if len(d) == 0:
		return 0
	else:
		d_keys = set(d.keys())
		removed = set()
		for k, v in d.items():
			if v in d_keys and k not in removed:
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




