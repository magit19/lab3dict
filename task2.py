from collections import defaultdict
def last_digit(L):
	d = defaultdict(int)
	
	for x in L:
		last = x%10
		d[last] += 1
	return d




if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]	
	print(last_digit(L))

