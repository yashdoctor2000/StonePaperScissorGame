import random

print("Rules of the Rock Paper Scissor Game is :->\n"+
                        "Rock VS Paper -> Paper Wins\n"+
                        "Rock VS Scissor -> Rock Wins\n"+
                        "Paper VS Scissor -> Scissor Wins")
                        
print("Select one from this \n"+
        "1) Rock\n"+
        "2) Paper\n"+
        "3) Scissor")
        
game={
    1: "Rock",
    2: "Paper",
    3: "Scissor"
}
        

comp_n = random.randint(1,3)

ans = True

while ans:
    n = int(input("Enter the number you have decided "))
    print("Computer have taken ",game[comp_n])
    
    if (n==1 and comp_n==2) or (n==2 and comp_n==3):
        print("Computer win this Game")
        break
    if (n==2 and comp_n==1) or (n==3 and comp_n==2):
        print("You have won the Game")
        break
    