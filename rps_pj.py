import random
choose = ["rock","paper","scissores"]
user_input = input("enter rock or paper or scissores : ").lower()
comp = random.choice(choose)
print("computer choise : ",comp)
if (user_input == comp):
    print("it's a tie !")
elif (user_input == "rock" and comp == "scissores") or (user_input == "paper" and comp == "rock") or (user_input == "scissores" and comp == "paper"):
    print("you won !")
else :
    print("you lose !")