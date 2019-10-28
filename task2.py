from collections import Counter

def last_digit(L):
	lasts = [x%10 for x in L]
	return Counter(lasts)


if __name__ == '__main__':
	print("Введите числа:")
	s = input().split()
	L = [int(x) for x in s]	
	print(last_digit(L))

