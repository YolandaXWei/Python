
# lab7


def separateBycomma():
    text="filed1,field2,field3,field4"
    commaLoc=text.find(",")
    start=0
    while commaLoc!=-1:
        print(text[start:commaLoc])
        start=commaLoc+1
        commaLoc= text.find (",",start)
    print(text[start:])

def spliBycomma():
    text="field1,field2,field3,field4"
    fields=text.split(",")
    for aStr in fields:
        print(aStr)
def openfiles():
    fileOK=False
    while not fileOK:
        try:
            name=input("whats the name of file:")
            infile=open(name,"r")
            fileOK=True
        except FileNotFoundError:
            print("its wrong file")
    for line in infile:
         print(line,end="")
    infile.close()
def WeatherReport():
    higher=0
    lower=0
    start=0
    time=0
    total=0
    higherdata=0
    lowerdata=0
    infile=open("Weather.txt","r")
    for line in infile:
        if line.find("Min_TemperatureF")==-1:
            pos1=line.find(" ")
            pos2=line.find(" ",pos1+1)
            poshigh=line[pos1:pos2]
            poslow=line[pos2:]
            data=line[:pos1]
            while int(poshigh)>higher:
                higher=int(poshigh)
                higherdata=data
                
            while int(poslow)<lower:
                lower=int(poslow)
                lowerdata=data
            if line.find("Jan")!=-1:
                pos1=line.find(" ")
                pos2=line.find(" ",pos1+1)
                poshigh=int(line[pos1:pos2])
                total=total+poshigh
                time+=1
    ave=total/time
    print("the average high tem is", ave)
                
                
                
            
    print("highist tem is",higher,"on",higherdata,"lowist tem is",lower,"on",lowerdata)


def QuizCalc():
    start=0
    infile=open("Quizzes.txt","r")
    outfile=open("Grades.txt","w")
    for line in infile:
        if line.find("Name")==-1:
            com1=line.find(",")
            com2=line.find(",",int(com1)+1)
            com3=line.find(",",int(com2)+1)
            com4=line.find(",",int(com3)+1)
            name=line[:com1]
            score1=line[com1+1:com2]
            score2=line[com2+1:com3]
            score3=line[com3+1:com4]
            score4=line[com4+1:]
            ave=(int(score1)+int(score2)+int(score3)+int(score4))/4
            #print(name,score1,score2,score3,score4)
            result=print(name,ave)
            print(name,ave,file=outfile)
    outfile.close()
    infile.close()
    
    
        
        
