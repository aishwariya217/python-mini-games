import random
words=["tree","college","hostel","wonderful","water","airpods","laptop","notebook","bangle","school"]
r=random.choice(words)
print(r)
d=[]
life=12
eog=False
l=len(r)
print("HANGMAN MINI GAME",end="\n")
for i in range(l):d +="_"
while not eog:
    w=input("\n enter a letter:")
    if w in d:print("<<<<<<<<You Have Already Guesed It>>>>>>>>>")
    for j in range (l):
        if(r[j]==w):
            d[j]=r[j]
    if w not in r:
        print(f"You guessed {w}, that's not in the word. You lose a life.")
        life-=1
        if life==0:
            eog=True
            print("-----------------YOU LOSE---------------------")  
    print(f"{' '.join(d)}") 
    if "_"not in d:
        eog=True
        print("!!!!!!!!!!!!!!!!YOU WIN!!!!!!!!!!!!!!!!!!!")  
