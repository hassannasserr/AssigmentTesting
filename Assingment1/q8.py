l1=list(map(int,input("Enter List of numbers : ").split()))
l2=input("Enter List of Chars: ").split()
# print(l1)
# print(l2)

def cust_ZIP (list1,list2):
    result=[]
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i],list2[i]))
    return result

print(cust_ZIP(l1,l2))





9