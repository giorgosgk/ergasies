harhsnum=[]
numbers2=[]
for i in range(1,1001):
    string=str(i)
    athrismaPsifiwn=0
    ginomenoPsifiwn=1
    for j in range(0,len(string)):
        athrismaPsifiwn+=int(string[j])
        ginomenoPsifiwn*=int(string[j])
    if i%athrismaPsifiwn==0:
        harhsnum.append(i)
    if ginomenoPsifiwn==0:
        continue
    if i%ginomenoPsifiwn==0:
        numbers2.append(i)
print('harshard numbers mexi to 1000')
print('************************')
print(harhsnum)
print(' ')
print('arithmoi pou to ginomeno tvn psifiwn tous diairei ton idio ton arithmo')
print('**********************')
print(numbers2)