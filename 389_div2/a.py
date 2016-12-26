#!/bin/python 
def main():
	l, d, k = map(int, raw_input().strip().split())

	l_index = (k / (2*d)) +1 if k %(2*d) != 0 else  (k /(2*d))
	r  = k % (2*d)

	if r == 0:		
		d_index = d
	else:
		d_index = r / 2 + 1 if r %2 != 0 else r /2


	
	side = 'R' if r % 2 == 0 else 'L'
	
	print '%s %s %s' %(l_index, d_index, side)

if __name__ == '__main__':
	main()