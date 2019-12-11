def last_digit(L):
	import collections
	d = {x: a.count(x) for x in a}

	return d

if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]
	a = [x%10 for x in L]

	print(last_digit(s))
