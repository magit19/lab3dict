def last_digit(L):
	d = {}
	for i in range(0, len(L), 1):
		d[L[i]] = L[i%10]
	return d


if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]
	print(last_digit(s))

