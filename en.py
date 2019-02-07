import string
alpha={}
al=list(string.ascii_lowercase)
for i in range(len(al)):
    alpha[1]=al[i]
alpha[26]="."
alpha[27]=" "
alpha[28]="\n"
with open(input("enter the name for encryption:"))as f:
    fl=list(f.read())
with open(input("enter filename in which encrypted data is saved:"),"w+")as en:
    for i in range(len(fl)):
        for j in range(len(alpha)):
            if fl[i]==alpha[j]:
                en.write(str(j))
                en.write('-')
    en.seek(0)
    el=list(en.read().split("-"))
#decryption
with open(input("enter the name of the file in which decrypted data is saved:"),"w+")as dec:
    for i in range(len(el)):
        for j  in range(len(alpha)):
            if a[i]==str(j):
                de.write(alpha[j])
          
