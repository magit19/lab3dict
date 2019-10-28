def last_digit(L):
	d = {}
	# подсчитать последние цифры всех чисел
	for x in L:
		last = x % 10
		d[last] = d.get(last, 0) + 1
	return d


if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]	
	print(last_digit(L))

