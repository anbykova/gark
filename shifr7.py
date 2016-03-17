
from __future__ import print_function

import random
import math

file = open('rand.txt', 'r')
strr = file.read()
strr = strr.lower()
b =''
dict = {}
matr = []
matr1 = []
for i in range(97,123):
    b +=chr(i)
for i in range(48,58):
    b +=chr(i)
print("alphabet")
a = b
print(a)
adv = 'ADFGVX'
ii=0
jj=0
kol = len(strr)
for i in range (kol):
  if ii> 5:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  if a.find(strr[i])!=-1:
      matr1.append(strr[i])
      dict[strr[i]] = jj * 10 + ii
      a = a.replace(strr[i],'')
      ii+=1
kol = len(a)

for i in range (kol):
  if ii> 5:
      matr.append(matr1)
      matr1 = []
      ii = 0
      jj+=1
  matr1.append(a[0])
  dict[a[0]] = jj * 10+ ii
  a = a.replace(a[0],'')
  ii+=1

matr.append(matr1)
for i in range(6):
    for j in range(6):
        print(matr[i][j], end = '')
    print()

def help(kluch , itog , posl):
    matr2 = []
    matr1 = []
    print(itog)
    for i in range(len(kluch)):
        for j in range(int (math.ceil(float(len(itog))/ len(kluch) ))): #надо окргулить вверх
            if (j * (len(kluch)) + i) < len(itog):
               matr1.append(itog[j* len(kluch) + i])
            else: matr1.append('A')
        matr2.append(matr1)
        matr1 = []
    i = 0
    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()
    i = 1
    print(posl)

    while i < len(posl):
        l = matr2[int(posl[i])]
        matr2[int(posl[i])] = matr2[int(posl[i-1])]
        matr2[int(posl[i - 1])] = l
        i += 2
    newstr = ''
    print('newmatr')
    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()


    for i in range(len(kluch)):
        for j in range(int (math.ceil(float(len(itog))/ len(kluch)))):
            newstr += matr2[i][j]
    print(newstr)
    return newstr
    
def help1(kluch , itog , posl):
    matr2 = []
    matr1 = []
    print(itog)
    for i in range(len(kluch)):
        for j in range(int(math.ceil(float(len(itog))/ len(kluch)))): #надо окргулить вверх
             if (j * (len(kluch)) + i) < len(itog):
                matr1.append(itog[j + i* (int(math.ceil(float(len(itog))/ len(kluch)))) ])
             else: matr1.append('A')
        matr2.append(matr1)
        matr1 = []
    i = 0
    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()
    i = 1
    print(posl)

    while i < len(posl):
        l = matr2[int(posl[i])]
        matr2[int(posl[i])] = matr2[int(posl[i-1])]
        matr2[int(posl[i - 1])] = l
        i += 2
    newstr = ''
    print('newmatr')
    kol = len(matr2[0])
    for i in range(kol):
        for j in range(len(matr2)):
            print(matr2[j][i], end = '')
        print()


    for j in range(int (math.ceil(float(len(itog))/ len(kluch)))):
        for i in range(len(kluch)):
            newstr += matr2[i][j]
    print(newstr)
    return newstr


    

def kod():
    file3 = open('kluch.txt', 'r')
    kluch = file3.read()
    kluch = kluch.lower()
    kl =''
    i = 0
    while i < len(kluch):

      if b.find(kluch[i])== -1:
         kluch = kluch.replace(kluch[i],'')
      else:
         if kl.find(kluch[i])==-1:
             kl += kluch[i]
         i += 1
    print(kl)
    kluch = kl
    posl = ''
    for i in reversed(range(len(kluch))):
       for j in range(1, i + 1):
           if kluch[j-1] > kluch[j]:
                a = [kluch[0:j-1],kluch[j],kluch[j-1],kluch[j+1:]]
                kluch = ''.join(a)
                posl = posl + str (j) + str (j - 1)
    print(posl)
    file1 = open('message.txt', 'r')
    STROKA = file1.read()
    STROKA = STROKA.lower()
    i = 0
    num = 0

    while i < len(STROKA):
      if b.find(STROKA[i])== -1:
        STROKA = STROKA.replace(STROKA[i],'')
      else:
          i+=1
        
    newstr = ''
    itog = ''
    for i in range(len(STROKA)):
        zn = dict[STROKA[i]]
        zn2 = int(zn / 10)
        zn1 = zn % 10
        itog += adv[zn2]+ adv[zn1]
    matr2 = []
    matr1 = []

    jj = 0
    print(itog)
    kol = (len(kluch)) * (len(kluch))
    while jj < len(itog):
        newstr += help(kluch, itog[jj: jj+kol], posl)
        jj +=kol

    print(" itog ===   " , newstr)

    file2 = open('itog1.txt', 'w')
    #!!!!!!print(matr2)
    file2.write(newstr)
    file2.close()


def de():
    file3 = open('kluch.txt', 'r')
    kluch = file3.read()
    kluch = kluch.lower()
    i = 0
    kl = ''
    while i <len(kluch):
      if b.find(kluch[i])== -1:
         kluch = kluch.replace(kluch[i],'')
      else:
         if kl.find(kluch[i])==-1:
             kl += kluch[i]
         i+=1
    print(kl)
    kluch = kl
    file1 = open('itog1.txt', 'r')
    STROKA = file1.read()
    i = 0
    num = 0

    matr2 = []
    matr1 = []
                
    posl = ''

    for i in reversed(range(len(kluch))):
       for j in range(1, i + 1):
           if kluch[j-1] > kluch[j]:
                a = [kluch[0:j-1],kluch[j],kluch[j-1],kluch[j+1:]]
                kluch = ''.join(a)
                posl = str(j-1) + str(j) + posl
    print(posl)
    i = 0
    jj = 0
    newstr = ''
    itog = ''
    kol = (len(kluch)) * (len(kluch))
    while jj < len(STROKA):
        newstr += help1(kluch, STROKA[jj: jj+kol], posl)
        jj +=kol
    i = 0

    while i < len(newstr)-1:
        itog += matr[adv.find(newstr[i])][adv.find(newstr[i+1])]
        i+=2
    newstr = ''    
    file2 = open('message.txt', 'w')
    i = 0
    print(newstr)
    print(itog)
    file2.write(itog)
        
    file2.close()

#zn = int(input('if shifr then 0 else 1'))

z = int(input('0 - shifr, 1 - deshifr'))
if z == 0:
    kod()
else:
    de()

