str=input()
str.lower()
res=0
for i in str:
    if i == 'a' or i=='e' or i=='i'or i =='o'or i=='u':
        res+=1
print(res)