def make_dict(L):
	d = {}
	for i in range(0,len(L),2): 
		d[L[i]] = L[i+1]
	return d


if __name__ == '__main__':
	print("Введите четное количество слов:")
	s = input().split()
	print(make_dict(s))

