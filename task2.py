def last_digit(L):
	import collections

	d = {x:s.count(x) for x in L}

	return d

if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]

	print(last_digit(s))
