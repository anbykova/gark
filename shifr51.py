from __future__ import print_function
import math

# Прочитаем набор байтиков из файла на диске
#data = file.read()
file = open('code.txt', 'r')
str2 = file.read()
str2 = str2.lower()
#str2 = 'winter, земляника, земляника.'


class Foo(object):
    def __init__(self, name):
       self.name = name
  
    def __str__(self):
       return '%s' % self.name
strr = str(Foo(file.read()))
strr = strr.lower()
#print(strr)
dict = {}
matr = []
matr1 = []
a = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя!.,?-:;"()012345'

b = Foo(a)
strr= ''
for i in str2:
    if a.find(i)!= -1 and strr.find(i)==-1:
        strr += str(Foo(i))
for i in a:
    if strr.find(i)== -1:
        strr += str(Foo(i))
        
#strr = str(b)
#print(strr)
a = strr
b = a
kol_vo = (math.sqrt(len(b)))
def prov(kol_vo, l):
    if kol_vo % 1> 0 :
      for i in range(int(kol_vo), -1, -1):
         if l % i == 0:
            kol_vo = i - 1
            return kol_vo
            break
    else: return (int(kol_vo) - 1)
          
kol_vo = prov(kol_vo, len(b))
if kol_vo == 0: kol_vo = prov(math.sqrt(len(b)), len(b)+1)

ii=0
jj=0
matr = []
kol = len(strr)
for i in strr:
  if ii> kol_vo:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  if a.find(i)!=-1:
      matr1.append(str(i))
      dict[str(i)] = ii * 10 + jj
      a = a.replace(i,'')
      ii+=1
kol = len(a)
ii = 0
for i in range (kol):
  if ii> kol_vo:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  matr1.append(str(a[0]))
  dict[str(a[0])] = ii * 10+ jj
  a = a.replace(a[0],'')
  ii+=1
if len(matr)<= jj:
    matr1.append('1')
matr.append(matr1)
for i in range(jj+1):
    for j in range(kol_vo+1):
        print(matr[i][j], end= '')
    print()
file1 = open('itog.txt', 'r')

STROKA = file1.read()
i = 0
num = 0    
newstr = ''
itog = ''
i = 0
#print(STROKA)
while i < (len(STROKA)):
    while not (STROKA[i].isdigit()): i+=1
    zn1 = int(STROKA[i])
    zn2 = int(STROKA[i+1])
    i+=2
    itog += matr[zn2][zn1]
       
print(itog)
file2 = open('message.txt', 'w')
file2.write(itog)
file2.close()
