import random as r
u_score = 0
c_score = 0

for i in range(5):
    u_choice=input("Enter your choice : rock , paper , scissor --->")
    c_choice=r.choice(["rock","paper","scissor"])

    if ((u_choice == "rock" and c_choice == "rock")|(u_choice == "paper" and c_choice == "paper")|(u_choice == "scissor" and c_choice == "scissor")):
        print("Computer Choice --->",c_choice)
        print("   DRAW! , Choice of your and  the computer is same")
        u_score+=1
        c_score+=1
        print("   Computer : ",c_score)
        print("   You : ",u_score)
        print()

    elif((u_choice == "rock" and c_choice == "paper")|(u_choice == "scissor" and c_choice == "rock")):
        print("Computer Choice --->",c_choice)
        print("   Computer win.")
        c_score+=1
        print("   Computer : ",c_score)
        print("   You : ",u_score)
        print()

    elif((u_choice == "paper" and c_choice == "rock")|(u_choice == "scissor" and c_choice == "paper")):
        print("Computer Choice --->",c_choice)
        print("   You Win !")
        u_score+=1
        print("   Computer : ",c_score)
        print("   You : ",u_score)
        print()

    elif((u_choice == "paper" and c_choice == "scissor")):
        print("Computer Choice --->",c_choice)
        print("   Computer Win !")
        c_score+=1
        print("   Computer : ",c_score)
        print("   You : ",u_score)
        print()

    elif(u_choice == "rock" and c_choice == "scissor"):
        print("Computer Choice --->",c_choice)
        print("   You win ! ")
        u_score+=1
        print("   Computer : ",c_score)
        print("   You : ",u_score)
        print()

    else:
        print("InCorrect Choice.")

print("\nScore board after 5-rounds:")
print("------------------------------")
print("Computer: ",c_score)
print("You: ",u_score)

if(c_score > u_score):
    print("Computer Won this game.")
elif(c_score < u_score):
    print("You Won this game.")
else:
    print("Game is Draw.")