import string

txt=input("Enter Your paragraph :")
withoutpunc=txt.translate(str.maketrans('','',string.punctuation))
withoutpunc=withoutpunc.lower()
words=withoutpunc.split()
res={}
for i in words:
    res[i]=0
for i in words:
    res[i]+=1

mostfreq= sorted(res.items(), key=lambda x: x[1], reverse=True)
top3=mostfreq[:3]


for word,freq in top3:
    print(word,end=' ')