x =int(input("Enter Number : "))
res=True
if x<=1:
    res=False
else:
    for i in range(2,int (x/2)+1):
         if x % i==0 :
             res=False
             break
print(res)