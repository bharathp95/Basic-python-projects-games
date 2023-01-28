import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choosed = int(input("Type 0 for rock, 1 for paper and 2 for scissors: "))

comp_choosed = random.randint(0,2)
print(f"the computer choosed {comp_choosed}")
if choosed == comp_choosed:
  print("its draw, run the program again")
elif choosed == 0 and comp_choosed == 1:
  print(f"{rock}\n{paper}You lose")
elif choosed == 0 and comp_choosed == 2:
  print(f"{rock}\n{scissors}You won")
elif choosed == 1 and comp_choosed == 0:
  print(f"{paper}\n{rock}you won")
elif choosed == 1 and comp_choosed == 2:
  print(f"{paper}\n{scissors} you lose")
elif choosed == 2 and comp_choosed == 0:
  print(f"{scissors}\n{rock} you lose")
elif choosed == 2 and comp_choosed == 1:
  print(f"{scissors}\n{paper} you win")
else:
    print("you have entered a wrong number")  

  
  
