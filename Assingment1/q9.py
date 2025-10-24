lst=list(map(int , input("Enter List of numbers: ").split()))
freq={}
for i in lst:
    freq[i] = freq.get(i, 0) + 1

res=[]
for i,cnt in freq.items():
    if cnt>0:
       res.append(i)
       cnt=0


print(res)