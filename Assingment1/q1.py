num=list(map(int,input("Enter Numbers :").split()))
evennum=list()
for i in num:
    if i%2==0 :
        evennum.append(i)
evennum.sort()
evennum.reverse()
print(evennum)

