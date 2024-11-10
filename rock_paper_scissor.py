import random 
computer = random.choice([-1,0,1]) 
yourchoice = input("enter your choice -> Rock , Paper , Scissor\n") 

Dict ={"rock":-1,"paper":0,"scissor":1} 
revDict={-1:"rock",0:"paper",1:"scissor"} 
you = Dict[yourchoice]  

print(f"you choose {revDict[you]} computer choose {revDict[computer]}") 

if computer == you: 
    print("match Draw !") 
    
else: 
    if (computer - you) == -1 or (computer - you) == 2 :
        print("you win !")
    else:
        print("computer wins !")
