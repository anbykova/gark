file = open('matr.txt', 'r')
str1 = file.read()
a = str1.split()
a = [int(x) for x in a]
matr = []
kol = 0
while a != []:
	matr1 = a[:9]
	matr.append(matr1)
	a = a[9:]
	kol += 1

def add(matr1, matr2):
        matr3 = []
        for i in range(len(matr1)):
            matr3.append((matr1[i]+matr2[i])% 2)
        return matr3

def mul(matr1, matr2):
	matr3 = []
	for j in range(3):
		for i in range(3):
			matr11 = matr1[3* j:][:3]
			matr22 = matr2[i::3]
			s = 0
			for i in range(len(matr22)):
      				  s+= (matr11[i]*matr22[i])
			matr3.append(s%2)
	return matr3

for i in range(kol):
    for j in range(kol):
        if add(matr[j],matr[i]) == matr[j]:
            check = True
            print('Нулевой элемент найден: ')
            q = matr[j]
            print(q[0],q[1], q[2])
            print(q[3],q[4],q[5])
            print(q[6],q[7], q[8])
            null = q
            break
if not(check):
    print('Нулевой элемент не найден')
else: 
    check = False
    for i in range(kol):
        for j in range(kol):
            if mul(matr[j],matr[i]) == matr[j] and matr[j] != null:
                check = True
                print('Единичный элемент найден: ')
                q = matr[j]
                print(q[0],q[1],q[2])
                print(q[3],q[4],q[5])
                print(q[6],q[7],q[8])
                ed = q
                break
    if not(check):
        print('Единичный элемент не найден')
    check = False
    for i in range(kol):
        for j in range(kol):
            if add(matr[j],matr[i]) != add(matr[i],matr[j]):
                check = True
                break
    if check:
        print('Коммутативность сложения НЕ выполняется')
    else:
        print('Коммутативность сложения выполняется')
    h = 0
    for i in range(kol):
        check = False
        if matr[i] != null:
            for j in range(kol):
                if add(matr[j],matr[i]) == null:
                    check = True
                    break
            if not(check):
                print('Не найдены противоположные эл-ты')
                print(matr[i])
                h = 1
    if h != 1:
        print('Найдены все противоположные элементы')
    
    if ed != 1:
        s = 0
        for i in range(kol):
            if matr[i] != null:
                check = False 
                for j in range(kol):
                    if mul(matr[i],matr[j]) == ed:
                        check = True
                        break
                if not(check):
                    print('НЕ найдены обр эл-ты для некотрого элемента')
                    print(matr[i])
                    s = 1
        if s != 1:
            print('Найдены обр эл-ты для всех')
        else:
       	    print('Единчиный эл-т не найден! обратные эл-ты искать не можем')
    else:
   	 print('нулевого эл-та нет! проверять некторые  условия не можем.')
            
check = False
for i in range(kol):
    for j in range(kol):
        for k in range(kol):
            if add(add(matr[j],matr[i]),matr[k]) != add(matr[i],add(matr[j],matr[k])):
                check = True
                break
if check:
    print('Ассоциативность сложения НЕ выполняется')
else:
    print('Ассоциативность сложения выполняется')

check = False
for i in range(kol):
    for j in range(kol):
        if mul(matr[j],matr[i]) != mul(matr[i],matr[j]):
            check = True
            break
if check:
    print('Коммутативность умножения НЕ выполняется')
else:
    print('Коммутативность умножения выполняется')
check = False
for i in range(kol):
    for j in range(kol):
        for k in range(kol):
            if mul(mul(matr[j],matr[i]),matr[k]) != mul(matr[i],mul(matr[j],matr[k])):
                check = True
                break
if check:
    print('Ассоциативность умножения НЕ выполняется')
else:
    print('Ассоциативность умножения выполняется')

check = False
for i in range(kol):
    for j in range(kol):
        for k in range(kol):
            if mul(add(matr[i],matr[j]),matr[k]) != add(mul(matr[i],matr[k]),mul(matr[j],matr[k])):
                check = True
                break
if check:
    print('Дистрибутивность умножения относительно сложения НЕ выполняется')
else:
    print('Дистрибутивность умножения относительно сложения выполняется')

