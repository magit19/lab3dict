def response(Dfiles, Doperations):
    d = {}
    for key, value in Doperations.items():
        if str(value[1]) in Dfiles:
            if value[0] == "read":
                if "R" in Dfiles.get(str(value[1])):
                    print("OK")
                else:
                    print("Access denied")
            if value[0] == "write":
                if "W" in Dfiles.get(str(value[1])):
                    print("OK")
                else:
                    print("Access denied")
            if value[0] == "execute":
                if "X" in Dfiles.get(str(value[1])):
                    print("OK")
                else:
                    print("Access denied")
        else:
            print("Error: file not found!")


if __name__ == '__main__':
    print("Введите количество файлов")
    n = input()
    s={}
    for i in range(int(n)):
        d = input().split()
        s.update({d[0]:d[1:]})
    print(s)
    print("Введите количество запросов")
    n = input()
    q={}
    for i in range(int(n)):
        q.update({i : input().split()})
    print(q)
    response(s,q)
    #L = [int(x) for x in s]
    #print(last_digit(L))
