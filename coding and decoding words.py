alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(code,a,sft):
    if code=="encode":
        etxt=""
        for l in a:
            p=alph.index(l)
            newp=p+sft
            newl=alph[newp]
            etxt+=newl
        print(f"The encoded text is : {etxt}")
    else:
        etxt=""
        for l in a:
            p=alph.index(l)
            newp=p-sft
            newl=alph[newp]
            etxt+=newl
        print(f"The encoded text is : {etxt}")
d=input("enter 'encode' for encoding and 'decode' for decoding:\n")
s=input("enter the word : ").lower()
shift=int(input("shift value : "))
encrypt(d,s,shift)
