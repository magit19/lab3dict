def last_digit(L):
	d = {}
	for i in L:
		end = i % 10
		d[end] = d.get(end, 0) + 1
	return d


if __name__ == '__main__':
	print("Введите список чисел:")
	s = input().split()
	L = [int(x) for x in s]
	print(last_digit(L))
