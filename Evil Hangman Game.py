def parse(line):
	fields=line.split(",")
	return fields[0], fields[1:]


def creatDeck():
    deck=""
    numrank=0
    numsuit=0
    ranks=("Ace","2","3","4","5","6","7","8","9","10","jack","Queen","king")
    suit=("Spades","Clubs","Dimaond","Harts")
    rlist=list(ranks)
    slist=list(suit)
    deck=[]
    while numrank<13 and numsuit<4:
        deck.append((ranks[numrank], suit[numsuit]))
        numrank+=1

        if numrank>12:
            numsuit+=1
            numrank=0
    return deck




def shuffle():
    import random
    num=51
    time=0
    newdeck=[]
    deck=creatDeck()
    while time!=52:
            card=random.randint(0,num)
          
            choosen=deck.pop(card)
           
            newdeck.append(choosen)
            num=num-1
            time=time+1
    return newdeck

def file1():
        import random
        file=open("file1.txt","r")
        num=0
        i=random.randint(1,20)
        for line in file:
                num=num+1
                if num==i:
                        word=line
        return word
def hungman():
        time=0
        print("game starts!!!!!")
        s=""
        word=str(file1())
        print(word)
        wordlist=["-"]*(len(word)-1)
        showlist=s.join(wordlist)
        print(showlist)
        while time<10 and showlist.find('-')!=-1:
                guess=input("the letter you guess: ")
                if word.find(guess)!=-1:
                        print("right")
                        numletter=word.count(guess)
                        print("there are",numletter,"in",word)
                        wordpos=0
                        pos=word.find(guess)
                        wordlist[pos]=(guess)
                        secpos=word.find(guess,pos+numletter-1)
                        wordlist[secpos]=(guess)
                        showlist=s.join(wordlist)
                        print(showlist)
                        
                        time+=1
                else:
                        print("wrong guess")
                        time+=1
        if time<10:
                print("=== you win ===")
        else:
                print("=== game over ===")

                
    


