#!/bin/python


def detect_chat(names, lines):

	known = set([])
	possible = dict(zip(range(len(lines)), [set(names) for _ in range(len(lines))]))
	print lines
	print possible

	for index, value in enumerate(lines):
		if value[0] !='?':
			possible[index] = set([value[0]])
		else:
			for each in value[1:]:
				for each_name in names:
					if each_name in each:
						possible[index].remove(each_name)


	for i in range(len(lines)):
		pre = i -1
		nxt = i +1
		if pre < 0:
			continue
		else:
			if lines[pre][0] in possible[i]:
				possible[i].remove(lines[pre][0])

		if nxt >=  len(lines):
			continue
		else:
			if lines[nxt][0] in possible[i]:
				possible[i].remove(lines[nxt][0])


	print possible
	if any( i != 1 for i in map(len, possible.values())):
		print 'Impossible'
	else:
		for i in range(len(lines)):
			# print type(list(possible[i]))
			# print possible[i]
			# print lines[1:]
			print ': '.join(list(possible[i]) + lines[i][1:])


def main():

	n = int(raw_input().strip())
	for _ in range(n):
		user = int(raw_input().strip())
		names = raw_input().strip().split()
		t = int(raw_input().strip())
		lines = []
		for _ in range(t):
			lines.append(raw_input().strip().split(': '))

		detect_chat(names, lines)

if __name__ == '__main__':
	main()

