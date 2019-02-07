import string
alpha={}
al=list(string.ascii_lowercase)
for i in range(len(al)):
    alpha[i]=al[i]
    alpha[26]="."
    alpha[27]=" "
    alpha[28]="\n"
with open(input("enter the name of file to be encrypted:"))as f:
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
            if el[i]==str(j):
                dec.write(alpha[j])
          
