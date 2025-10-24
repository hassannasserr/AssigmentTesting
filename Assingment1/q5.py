num =int(input())
res=[]
num1 = 0
num2 =1
res.append(0)
for i in range(1,num):
    if i ==1 :
        res.append(1)
        continue
    res.append(num2+num1)
    x=num2+num1
    num1=num2
    num2=x

print(res)