def make_dict(L):
	d = {}
	for H in (0, len(L), 2):
		d[L[H] ] = L[H+1]
	# .... сделать из списка словарь
	return d


if __name__ == '__main__':
	print("Введите четное количество слов:")
	s = input().split()
	print(make_dict(s))

