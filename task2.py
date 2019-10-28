def last_digit(L):
	d = {}
	for i in L:
		last = i % 10
		d[last] = d.get(last, 0) + 1
	# подсчитать последние цифры всех чисел
	return d


if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]	
	print(last_digit(L))

