seq1 = 'AGTTTATAG'

for i in range(0,len(seq1),3):
    print(seq1[i:i+3])

print(seq1[::-1])

dic = {'A':'T','T':'A','G':'C','C':'G'}
seq2 = ''
for i in seq1:
    seq2 += dic[i]
print(seq2)

def com2







print(seq1)
if seq1.find('C')>0:
    print('C')
else:
    print('XC')


x = []
a = 0
for i in range(len(seq1)):
    a=seq1[i:].find('TT')
    if a >=0:
        x.append(a+i)
print(x)

from collections import Counter
l = [3,1,1,2,0,0,2,3,3]
print(Counter(l)

d = {}
for i in l:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1 



