# LuckyDice
# LuckyDice.py
# Huahao Shang
# Wilson
# hushang
from graphics import *
from random import randrange
#(CLOD) a class to make a Rectangle and draw message with color,text,point,size.
class aRectangle:
    #P1 and P2 are two points of the rectangle, message is the intstruction that printed
    #on the rectangle, P3 is the point for message to draw, txtSize is the text size.
    def __init__(self,win,P1,P2,color,message,P3,txtSize):
        self.P1=P1
        self.P2=P2
        self.P3=P3
        self.color=color
        self.win=win
        self.message=message
        self.txtSize=txtSize
    def display(self):
        aRect=Rectangle(self.P1,self.P2)
        aRect.setFill(self.color)
        Mess=Text(self.P3,self.message)
        Mess.setSize(self.txtSize)
        aRect.draw(self.win)
        Mess.draw(self.win)
        
#(GW)Set the GraphWin
def setGraph():
    win=GraphWin("dices:",800,640)
    win.setCoords(0,0,20,16)
    return win
#(GW)close graph window and draw a new graph window, parameter is the graphwin
def CloseSet(win):
    win.close()
    win=setGraph()
    return win
#(IMS)To check if the mouse click the specific rectangle area
# parameter is three point, mouse clicked and two point from rectangle
def checkButtonClick(clickedPoint,leftLower,rightUpper):
    X=clickedPoint.getX()
    Y=clickedPoint.getY()
    x1=leftLower.getX()
    x2=rightUpper.getX()
    y1=leftLower.getY()
    y2=rightUpper.getY()
    if X>x1 and X<x2 and Y>y1 and Y<y2:
        return 1
    else:
        return 0
#(IEB)To get the player's name by using entry box, return the name and a value that will use later 
def getName(win):
    win1=win
    a=0
    Welmessage=Text(Point(10,14),"Welcome to Lucky Dice!")
    Welmessage.setSize(18)
    Welmessage.setTextColor("red")
    Welmessage.draw(win)
    nameMessage=Text(Point(5,11),"Enter your name")
    nameMessage.setSize(15)
    nameBox=Entry(Point(5,10),20)
    nameBox.setTextColor("black")
    nameBox.setSize(18)
    nameBox.setText("")
    nameBox.draw(win1)
    nameMessage.draw(win1)
    subButton=Rectangle(Point(5,8.5),Point(7,9.5))
    subButton.setFill("orange")
    subBlable=Text(Point(6,9),"Submit")
    subBlable.setTextColor("white")
    subButton.draw(win1)
    subBlable.draw(win1)
    return nameBox,a
# check the player if he clicked the submit rectangle to submit name return the value a
#using in the while loop
def checkSubName(win):
    leftLower=Point(5,8.5)
    rightUpper=Point(7,9.5)
    clickedPoint=win.getMouse()
    a=checkButtonClick(clickedPoint,leftLower,rightUpper)
    return a
#check the plsyer if he clicked the help buttom and return 1 if clicked return 0 if not clicked
def checkSubHelp(win,clickedPoint):
    leftLower=Point(1,1)
    rightUpper=Point(3,2)
    help=checkButtonClick(clickedPoint,leftLower,rightUpper)
    return help
#display the game rules if the player clicked the help buttom
def helpDisplay(win,clickedPoint):
    help=checkSubHelp(win,clickedPoint)
    if help==1:
        helpMess1=Text(Point(5,9),"Ten dice total, player and computer have five each")
        helpMess2=Text(Point(5,8),"Player and computer both roll their dice")
        helpMess3=Text(Point(5,7),"Based on result,chose a dot and guess how many total")
        helpMess4=Text(Point(5,6),"player can see his fice dice, and also computer")
        helpMess5=Text(Point(5,5),"if the quantity >= the guessing means correct")
        helpMess6=Text(Point(5,4),"the player can Win, Lose and Tie")
        helpMess7=Text(Point(5,3),"Go to play, it is fun")
        helpMess1.draw(win)
        helpMess2.draw(win)
        helpMess3.draw(win)
        helpMess4.draw(win)
        helpMess5.draw(win)
        helpMess6.draw(win)
        helpMess7.draw(win)
#check if the player choose easy mode to play
def checkSubEasy(win,clickedPoint):                  
    leftLower=Point(14,6)
    rightUpper=Point(16,7)
    a=checkButtonClick(clickedPoint,leftLower,rightUpper)            
    return a
#check if the player choose the hard mode to play
def checkSubHard(win,clickedPoint):
    leftLower=Point(14,4)
    rightUpper=Point(16,5)
    a=checkButtonClick(clickedPoint,leftLower,rightUpper)
    return a
#the functoin that call previous functions to check which bottom the player click 
#and make the right operation
def checkGameMode(win,a):
    while a!=1:
        clickedPoint=win.getMouse()
        helpDisplay(win,clickedPoint)
        SubEasy=0
        SubHard=0
        SubEasy=checkSubEasy(win,clickedPoint)
        if SubEasy==1:
            a=1
            win=CloseSet(win)
            return SubEasy,SubHard,win
        elif SubEasy==0:
            SubHard=checkSubHard(win,clickedPoint)
            if SubHard==1:
                win=CloseSet(win)
                a==1
                return SubEasy,SubHard,win
            else:
                a=0
# the parameter name is the text that the player input. This function is the intro page
#of the game. It can show different selections for the player. Player can choose easy or
#hard mode or get help. parameter is geaphwin and the name that player enters 
def introPage(win,name):
    #(IEB)
    namStr=name.getText()
    #(OTXT)
    nameWelcome=Text(Point(10,14),"Hello "+namStr+"! Welcome to Lucky Dice!")
    nameWelcome.setSize(20)
    nameWelcome.draw(win)
    #(CLOD)using class
    helpR=aRectangle(win,Point(1,1),Point(3,2),"red","Help",Point(2,1.5),20)
    easyR=aRectangle(win,Point(14,6),Point(17,7),"yellow","Easy",Point(15.5,6.5),20)
    hardR=aRectangle(win,Point(14,4),Point(17,5),"green","Hard",Point(15.5,4.5),20)
    helpR.display()
    easyR.display()
    hardR.display()
    GdifMess=Text(Point(15.5,8),"Game Difficulty")
    GdifMess.setSize(20)
    GdifMess.draw(win)
#this funciton is connected with the previous function.
def gameStart(win):
    win=win
    gameDif=Text(Point(15,8),"Game Difficulty")
    gameDif.setSize(18)
    easyRec=Rectangle(Point(14,6),Point(16,7))
    easyRec.setFill("orange")
    easyRLable=Text(Point(15,6.5),"Easy")
    hardRec=Rectangle(Point(14,4),Point(16,5))
    hardRec.setFill("green")
    hardRLable=Text(Point(15,4.5),"Harder")
    helpRec=Rectangle(Point(1,1),Point(3,2))
    helpRLable=Text(Point(2,1.5),"Help")
    gameDif.draw(win)
    easyRec.draw(win)
    hardRec.draw(win)
    easyRLable.draw(win)
    hardRLable.draw(win)
    helpRec.draw(win)
    helpRLable.draw(win)
# this funciton shows the first game step, for guiding the player to roll the dice
#by chicking the specific reactngle area.
def drawdice1(win):
    D1=Image(Point(14,11),"Dice1.gif")
    D2=Image(Point(14,9),"Dice2.gif")
    D3=Image(Point(14,7),"Dice3.gif")
    D4=Image(Point(17,11),"Dice4.gif")
    D5=Image(Point(17,9),"Dice5.gif")
    D6=Image(Point(17,7),"Dice6.gif")
    D1.draw(win)
    D2.draw(win)
    D3.draw(win)
    D4.draw(win)
    D5.draw(win)
    D6.draw(win)
    clickMessage=Text(Point(6,11),"Click the buttom to toll the dice")
    clickRec=Rectangle(Point(4,8),Point(8,10))
    clickMessage.setSize(18)
    clickRec.setFill("Orange")
    clickMessage.draw(win)
    clickRec.draw(win)
    leftLower=Point(5,8.5)
    rightUpper=Point(7,9.5)
    c=0
    while not(c==1):
        #(IMS)
        clickedPoint=win.getMouse()
        c=checkButtonClick(clickedPoint,leftLower,rightUpper)
    win.close()
    win=setGraph()
    return win
#(FNC) the function that can show the rolling dice result. Creating two lists to
# collecet random number and put them into a list. And then print the rolling dice
# result on the graphwin also with dice pictures. retrurn the two list that represent
#player's dices and computer's dice.
def drawdice2(win):
    #(LOOD)
    diceList1=[0,0,0,0,0,0]
    diceList2=[0,0,0,0,0,0]
    for i in range(5):
        #(RND)
        dicNum1=randrange(0,6,1)
        dicNum2=randrange(0,6,1)
        diceList1[dicNum1]=diceList1[dicNum1]+1
        diceList2[dicNum2]=diceList2[dicNum2]+1
    D1=Image(Point(4,11),"Dice1.gif")
    D2=Image(Point(4,9),"Dice2.gif")
    D3=Image(Point(4,7),"Dice3.gif")
    D4=Image(Point(7,11),"Dice4.gif")
    D5=Image(Point(7,9),"Dice5.gif")
    D6=Image(Point(7,7),"Dice6.gif")
    D1N=Text(Point(5.4,11),diceList1[0])
    D2N=Text(Point(5.4,9),diceList1[1])
    D3N=Text(Point(5.4,7),diceList1[2])
    D4N=Text(Point(8.2,11),diceList1[3])
    D5N=Text(Point(8.2,9),diceList1[4])
    D6N=Text(Point(8.2,7),diceList1[5])
    YD=Text(Point(5.4,12.5),"Your Dices")
    YD.setSize(17)
    YD.draw(win)
    D1.draw(win)
    D2.draw(win)
    D3.draw(win)
    D4.draw(win)
    D5.draw(win)
    D6.draw(win)
    D1N.draw(win)
    D2N.draw(win)
    D3N.draw(win)
    D4N.draw(win)
    D5N.draw(win)
    D6N.draw(win)
    return diceList1,diceList2
    
# the functoins is using entry box to let the player to make guess
# return the necessary info form the entry box and two lists
def diceGuess(win):
    #(FNC)
    diceList1,diceList2=drawdice2(win)
    diceNumMessage=Text(Point(15,11),"Dice Number?")
    diceNumBox=Entry(Point(15,10),10)
    diceNumBox.setTextColor("black")
    diceNumBox.setText("0")
    diceNumBox.draw(win)
    diceNumMessage.draw(win)
    diceManyMessage=Text(Point(15,7),"How Many?")
    diceManyBox=Entry(Point(15,6),10)
    diceManyBox.setTextColor("black")
    diceManyBox.setText("0")
    diceManyBox.draw(win)
    diceManyMessage.draw(win)
    subButton2=Rectangle(Point(16,4),Point(18,4.5))
    subButton2.setFill("blue")
    subBlable2=Text(Point(17,4.25),"Submit")
    subBlable2.setTextColor("white")
    subButton2.draw(win)
    subBlable2.draw(win)
    #(IEB)
    DiceNum=diceNumBox.getText()
    DiceCount=diceManyBox.getText()
    a=0
    leftLower=Point(16,4)
    rightUpper=Point(18,4.5)
    while a!=1:
        #(IMS)
        clickedPoint=win.getMouse()
        a=checkButtonClick(clickedPoint,leftLower,rightUpper)
        DiceNum=diceNumBox.getText()
        DiceCount=diceManyBox.getText()
        if int(DiceCount)<=2 or int(DiceNum)<1 or int(DiceNum)>6:
            WrongEnt=Text(Point(10,15),"Please Change your valus, dice number should from 1 to 6, the amount need to bigger than 2")
            WrongEnt.setTextColor("red")
            WrongEnt.setSize(12)
            WrongEnt.draw(win)
            a=0
            
    win=CloseSet(win)
    return int(DiceNum),int(DiceCount),diceList1,diceList2,win
#(RND) for easy game mode, using random for computer to make their decision
# parameter are graphwin, a list of computer's dice and player's guessing
def EGuessdraw1(win,diceList2,DC,DN):
    #(RND)
    dnum=randrange(1,7,1)
    dcount=randrange(3,7,1)
    CompGuess=Text(Point(10,3),"The computer said there are "+str(dcount)+" dices facing up with number "+str(dnum))
    CompGuess.draw(win)
    YourGuess=Text(Point(10,4),"You said there are"+str(DC)+" dices facing up with number "+str(DN))
    YourGuess.draw(win)
    CD=Text(Point(15.4,12.5),"Computer's dice")
    CD.draw(win)
    cD1=Image(Point(14,11),"Dice1.gif")
    cD2=Image(Point(14,9),"Dice2.gif")
    cD3=Image(Point(14,7),"Dice3.gif")
    cD4=Image(Point(17,11),"Dice4.gif")
    cD5=Image(Point(17,9),"Dice5.gif")
    cD6=Image(Point(17,7),"Dice6.gif")
    cD1N=Text(Point(15.4,11),diceList2[0])
    cD2N=Text(Point(15.4,9),diceList2[1])
    cD3N=Text(Point(15.4,7),diceList2[2])
    cD4N=Text(Point(18.2,11),diceList2[3])
    cD5N=Text(Point(18.2,9),diceList2[4])
    cD6N=Text(Point(18.2,7),diceList2[5])
    cD1.draw(win)
    cD2.draw(win)
    cD3.draw(win)
    cD4.draw(win)
    cD5.draw(win)
    cD6.draw(win)
    cD1N.draw(win)
    cD2N.draw(win)
    cD3N.draw(win)
    cD4N.draw(win)
    cD5N.draw(win)
    cD6N.draw(win)
    return dnum,dcount
#To draw player's dice on the graphwin, the function will be called on the checking
#process, parameter are graphwin and player's dice list.
def EGuessdraw2(win,diceList1):
    D1=Image(Point(4,11),"Dice1.gif")
    D2=Image(Point(4,9),"Dice2.gif")
    D3=Image(Point(4,7),"Dice3.gif")
    D4=Image(Point(7,11),"Dice4.gif")
    D5=Image(Point(7,9),"Dice5.gif")
    D6=Image(Point(7,7),"Dice6.gif")
    D1N=Text(Point(5.4,11),diceList1[0])
    D2N=Text(Point(5.4,9),diceList1[1])
    D3N=Text(Point(5.4,7),diceList1[2])
    D4N=Text(Point(8.2,11),diceList1[3])
    D5N=Text(Point(8.2,9),diceList1[4])
    D6N=Text(Point(8.2,7),diceList1[5])
    YD=Text(Point(5.4,12.5),"Your Dices")
    YD.setSize(17)
    YD.draw(win)
    D1.draw(win)
    D2.draw(win)
    D3.draw(win)
    D4.draw(win)
    D5.draw(win)
    D6.draw(win)
    D1N.draw(win)
    D2N.draw(win)
    D3N.draw(win)
    D4N.draw(win)
    D5N.draw(win)
    D6N.draw(win)
#(LOOD) the hard mode for the computer to make the decision using list and if statement
def HGuessdraw1(win,diceList2,DC,DN):
    d1,d2,d3,d4,d5,d6=diceList2[0],diceList2[1],diceList2[2],diceList2[3],diceList2[4],diceList2[5]
    #(LOOD)
    Listd=[d1,d2,d3,d4,d5,d6]
    Listd.sort()
    Big=Listd[5]
    if Big==d1:
        dnum=1
    elif Big==d2:
        dnum=2
    elif Big==d3:
        dnum=3
    elif Big==d4:
        dnum=4
    elif Big==d5:
        dnum=5
    elif Big==d6:
        dnum=6
    #(RND)
    dcount=randrange(3,5,1)
    CompGuess=Text(Point(10,3),"The computer said there are "+str(dcount)+" dices facing up with number "+str(dnum))
    CompGuess.draw(win)
    YourGuess=Text(Point(10,4),"You said there are"+str(DC)+" dices facing up with number "+str(DN))
    YourGuess.draw(win)
    CD=Text(Point(15.4,12.5),"Computer's dice")
    CD.draw(win)
    cD1=Image(Point(14,11),"Dice1.gif")
    cD2=Image(Point(14,9),"Dice2.gif")
    cD3=Image(Point(14,7),"Dice3.gif")
    cD4=Image(Point(17,11),"Dice4.gif")
    cD5=Image(Point(17,9),"Dice5.gif")
    cD6=Image(Point(17,7),"Dice6.gif")
    cD1N=Text(Point(15.4,11),diceList2[0])
    cD2N=Text(Point(15.4,9),diceList2[1])
    cD3N=Text(Point(15.4,7),diceList2[2])
    cD4N=Text(Point(18.2,11),diceList2[3])
    cD5N=Text(Point(18.2,9),diceList2[4])
    cD6N=Text(Point(18.2,7),diceList2[5])
    cD1.draw(win)
    cD2.draw(win)
    cD3.draw(win)
    cD4.draw(win)
    cD5.draw(win)
    cD6.draw(win)
    cD1N.draw(win)
    cD2N.draw(win)
    cD3N.draw(win)
    cD4N.draw(win)
    cD5N.draw(win)
    cD6N.draw(win)
    return dnum,dcount
# those peremeters are the data that from previous steps. Using those data to determine if the play
#win lost or tie the game by using if statement and draw the approate result on the GrahWIn
#Win,Lost,Tie are parameters that record of the player win, lose or tie the game.
# Parameter player's guessing, two lists contain player's dice and computer's
# computer's guessing and values for record game result
def Evaluation(win,DC,DN,diceList1,diceList2,dnum,dcount,Win,Lost,Tie):
    diceplayer0=diceList1[0]+diceList2[0]
    dicecomp0=diceList1[0]+diceList2[0]
    #(FNC)
    if DN==1 or dnum==1:
        diceplayer0,dicecomp0=addEvaluation(DC,DN,dcount,dnum,diceplayer0,dicecomp0)
    if DC<=diceList1[DN-1]+diceList2[DN-1]+diceplayer0 and int(dcount)>diceList1[int(dnum)-1]+diceList2[int(dnum)-1]+dicecomp0:
        winRec=Rectangle(Point(15,4),Point(17,6))
        winRec.setFill("orange")
        winMessage=Text(Point(16,5),"You WIN")
        winRec.draw(win)
        winMessage.draw(win)
        Win=Win+1
    elif DC>diceList1[DN-1]+diceList2[DN-1]+diceplayer0 and int(dcount)<=diceList1[int(dnum)-1]+diceList2[int(dnum)-1]+dicecomp0:
        winRec=Rectangle(Point(15,4),Point(17,6))
        winRec.setFill("orange")
        winMessage=Text(Point(16,5),"You Lose")
        winRec.draw(win)
        winMessage.draw(win)
        Lost=Lost+1
    elif DC<=diceList1[DN-1]+diceList2[DN-1]+diceplayer0 and int(dcount)<=diceList1[int(dnum)-1]+diceList2[int(dnum)-1]+dicecomp0:
        winRec=Rectangle(Point(15,4),Point(17,6))
        winRec.setFill("orange")
        if DC>int(dcount):
            winMessage=Text(Point(16,5),"You WIN")
            winRec.draw(win)
            winMessage.draw(win)
            Win=Win+1
        if DC<int(dcount):
            winMessage=Text(Point(16,5),"You Lose")
            winRec.draw(win)
            winMessage.draw(win)
            Lost=Lost+1
        if DC==int(dcount):
            winMessage=Text(Point(16,5),"Tie game")
            winRec.draw(win)
            winMessage.draw(win)
            Tie=Tie+1
    elif DC>diceList1[DN-1]+diceList2[DN-1]+diceplayer0 and int(dcount)>diceList1[int(dnum)-1]+diceList2[int(dnum)-1]+dicecomp0:
        winRec=Rectangle(Point(15,4),Point(17,6))
        winRec.setFill("orange")
        winMessage=Text(Point(16,5),"Tie game")
        winRec.draw(win)
        winMessage.draw(win)
        Tie=Tie+1
    return Win,Lost,Tie
# the function is to deal some special situation in order to make the checking process
# more accurate.
def addEvaluation(DC,DN,dcount,dnum,diceplayer0,dicecomp0):
    if DN==1 and dnum==1:
        diceplayer0=0
        dicecomp0=0
        return diceplayer0,dicecomp0
    elif dnum==1 and DN!=1:
        dicecomp0=0
        return diceplayer0,dicecomp0
    elif DN==1 and dnum!=1:
        diceplayer0=0
        return diceplayer0,dicecomp0
#(FNC) the function that calls the previous funcitons to accomplish the process.
#Also using class to crate two necessary rectangles.
def easyEval(win,DC,DN,diceList1,diceList2,Win,Lost,Tie):
    dnum,dcount=EGuessdraw1(win,diceList2,DC,DN)
    EGuessdraw2(win,diceList1)
    Win,Lost,Tie=Evaluation(win,DC,DN,diceList1,diceList2,dnum,dcount,Win,Lost,Tie)
    #(CLOD)
    PlayAgain=aRectangle(win,Point(1,1),Point(4,2),"yellow","Play Again",Point(2.5,1.5),15)
    PlayAgain.display()
    Quit=aRectangle(win,Point(5,1),Point(9,2),"yellow","Quit and show record",Point(7,1.5),15)
    Quit.display()
    return Win,Lost,Tie
#(FNC) the function that calls the previous funcitons to accomplish the process.
#Also using class to crate two necessary rectangles.The hard mode.
def hardEval(win,DC,DN,diceList1,diceList2,Win,Lost,Tie):
    dnum,dcount=HGuessdraw1(win,diceList2,DC,DN)
    EGuessdraw2(win,diceList1)
    Win,Lost,Tie=Evaluation(win,DC,DN,diceList1,diceList2,dnum,dcount,Win,Lost,Tie)
    #(CLOD)
    PlayAgain=aRectangle(win,Point(1,1),Point(4,2),"yellow","Play Again",Point(2.5,1.5),15)
    PlayAgain.display()
    Quit=aRectangle(win,Point(5,1),Point(9,2),"yellow","Quit and show record",Point(7,1.5),15)
    Quit.display()
    return Win,Lost,Tie
# a function that to check if the player wants to keep play
def checkplayAgain(win):
    #(IMS)
    clickedPoint=win.getMouse()
    leftLower=Point(1,1)
    rightUpper=Point(4,2)
    a=0
    while a!=1:
        clickedPoint=win.getMouse()
        a=checkButtonClick(clickedPoint,leftLower,rightUpper)
        if a==1:
            quit=0
            win=CloseSet(win)
        elif a==0:
            leftLower=Point(5,1)
            rightUpper=Point(9,2)
            a=checkButtonClick(clickedPoint,leftLower,rightUpper)
            if a==1:
                win=CloseSet(win)
                quit=1
            else:
                quit=0
    return quit,win
#(IFL OFL LOOD) read the previous records from a finl and put it into a list, adding the
#new player record to the list, and then print those in the GraphWin, also print to
#an output file (input file and output file have the same name)
def inputfile(win,name,Win,Lost,Tie,SubEasy):
    #(IFL)
    infile=open("inputfile.txt","r")
    #(LOOD)
    List=[]
    for line in infile:
        List.append(line.rstrip())
    if SubEasy==1:
        rec=name.getText()+"\t"+str(Win)+"\t"+str(Tie)+"\t"+str(Lost)+"\tEasy"
    if SubEasy==0:
        rec=name.getText()+"\t"+str(Win)+"\t"+str(Tie)+"\t"+str(Lost)+"\tHard"
    List.append(rec)
    infile.close()
    x,y=8,15
    for mess in range(len(List)):
        Record1=Text(Point(x,y-mess),List[mess])
        Record1.draw(win)
    #(OFL)
    infile=open("inputfile.txt","w")
    for i in range(len(List)):
        print(List[i],file=infile)
    infile.close()
    quitmess=Text(Point(10,3),"Thanks for playing the Lucky Dice "+name.getText()+" !")
    quitmess2=Text(Point(10,2),"Click anywhere to quit")
    quitmess.setSize(15)
    quitmess2.setSize(15)
    quitmess.draw(win)
    quitmess2.draw(win)
def main():
    #Setting up the graphwin
    win=setGraph()
    #getting the player's name
    name,a=getName(win)
    #while loop to make sure the player click the right place.
    while a!=1:
        a=checkSubName(win)
    #close the window and creat a new one.
    win=CloseSet(win)
    #the guide page of the game
    introPage(win,name)
    a=0
    quit=0
    Win=0
    Lost=0
    Tie=0
    #for player to choose the difficulty of the game.
    SubEasy,SubHard,win=checkGameMode(win,a)
    while quit!=1:
        win=drawdice1(win)
        DN,DC,diceList1,diceList2,win=diceGuess(win)
        #the game in easy mode
        if SubEasy==1:
            Win,Lost,Tie=easyEval(win,DC,DN,diceList1,diceList2,Win,Lost,Tie)
            quit,win=checkplayAgain(win)
        #the game in hard mode
        elif SubHard==1:
            Win,Lost,Tie=hardEval(win,DC,DN,diceList1,diceList2,Win,Lost,Tie)
            quit,win=checkplayAgain(win)
    #read input file and print the game record and then store on output file.
    inputfile(win,name,Win,Lost,Tie,SubEasy)
    win.getMouse()
    win.close()
main()
    



        
