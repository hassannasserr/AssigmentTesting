x=list(map(str,input("Enter Strings: ").split()))
res={}
for i in x:
    res[i]= len(i)
print(res)
