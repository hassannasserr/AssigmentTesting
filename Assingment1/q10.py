import string
txt=input("Enter Your paragraph :")
withoutpunc=txt.translate(str.maketrans('','',string.punctuation))
withoutpunc=withoutpunc.lower()
words=withoutpunc.split()
print(len(words))
