from __future__ import print_function

import math
#file = open('text1.txt', 'r')

# Прочитаем набор байтиков из файла на диске
#data = file.read()
file = open('code.txt', 'r')
str2 = file.read()
str2 = str2.lower()
#str2 = 'winter, земляника, земляника.'

# Запишем байты обратно на диск
#file1.write(data)

#file1.close()  # Необязательно, но хороший стиль


class Foo(object):
    def __init__(self, name):
       self.name = name
  
    def __str__(self):
       return '%s' % self.name
strr = str(Foo(file.read()))
strr = strr.lower()
dict = {}
matr = []
matr1 = []
a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя!.,?-:;"()012345'
b = Foo(a)
strr= ''
for i in range(len(str2)):
    if a.find(str2[i])!= -1 and strr.find(str2[i])==-1:
        strr += str(Foo(str2[i]))
for i in range(len(a)):
    if strr.find(a[i])== -1:
        strr += str(Foo(a[i]))       
#strr = str(b)
a = strr
b = a
kol_vo = (math.sqrt(len(b)))

def prov(kol_vo, l):
    
    if kol_vo % 1> 0 :s
      for i in range(int(kol_vo), -1, -1):
         if l % i == 0:
            kol_vo = i - 1
            return kol_vo
            break
    else: return (int(kol_vo) - 1)
          
kol_vo = prov(kol_vo, len(b))
if kol_vo == 0: kol_vo = prov(math.sqrt(len(b)), len(b)+1)
ii = 0
jj=0
matr = []
kol = len(strr)
for i in range (kol):
  if ii> kol_vo :
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  if a.find(strr[i])!=-1:
      matr1.append(strr[i])
      dict[strr[i]] = ii * 10 + jj
      a = a.replace(strr[i],'')
      ii+=1
kol = len(a)
ii = 0
for i in range (kol):
  if ii> kol_vo :
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  matr1.append(a[0])
  dict[a[0]] = ii * 10+ jj
  a = a.replace(a[0],'')
  ii += 1


if len(matr)<= jj:
    matr1.append('1')
matr.append(matr1)

file1 = open('message.txt', 'r')
for i in range(jj+1):
    for j in range(kol_vo+1):
        print(matr[i][j], end= '')
    print()
STROKA = file1.read()
STROKA = STROKA.lower()
i = 0
num = 0

while i <len(STROKA):
  if b.find(STROKA[i])== -1:
    STROKA = STROKA.replace(STROKA[i],'')
  else:
      i+=1
    
newstr = ''
itog = ''
for i in range(len(STROKA)):
    zn = dict[STROKA[i]]
    zn1 = str(zn/10)
    zn2 = str(zn%10)
    itog =itog + str(zn1) + str(zn2)
       
print(itog)
file2 = open('itog.txt', 'w')
file2.write(itog)
file2.close()

