#!/bin/python


tb = [[0 for _ in range(4)] for _ in range(4)]

steps = [-1, 0, 1]

def move_can_win(x,y, target):
	if x > 3 or x < 0 or y < 0 or y > 3:
		return False
	else:
		if tb[x][y] == target:
			return True
		else:
			return False

def can_win(pos_x, pos_y):
	for i in steps:
		for j in steps:
			if i == j and i == 0:
				continue
			else:
				x = pos_x +i
				y = pos_y + j
				if x < 0 or x > 3 or y < 0 or y > 3:
					continue
				else:
					if tb[x][y] == 2:
						continue
					elif tb[x][y] == 0:
						
						if move_can_win(x+i,y+j, 1):
							return True
						else:
							continue
					else:						
						if move_can_win(x+i, y+j, 0):
							return True
						else:
							continue

	return False

def main():

	i = 0
	for _ in range(4):
		ar = raw_input().strip()


		j = 0
		for each in ar:
			if each == 'x':
				tb[i][j] = 1
			elif each == 'o':
				tb[i][j] = 2
			j +=1

		i += 1


	possible = False
	for i in range(4):
		for j in range(4):
			if tb[i][j] == 1:
				if can_win(i, j):
					possible = True
					break

	if not possible:
		print 'NO'
	else:
		print 'YES'

if __name__ == '__main__':
	main()


