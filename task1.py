def make_dict(L):
	d = {}
	d = {L[i]:L[i+1] for i in range(0, len(L), 2)}
	return d


if __name__ == '__main__':
	print("Введите четное количество слов в формате [ключ1, значение1, ключ2, значение2,...]:")
	s = input().split() 
	print(make_dict(s))
