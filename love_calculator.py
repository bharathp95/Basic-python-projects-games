# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

n1=name1.lower()
n2=name2.lower()

final = n1+n2

f1 = final.count("t")
f2 =final.count("r")
f3 =final.count("u")
f4 =final.count("e")
 
final_tcount = f1+f2+f3+f4

fl1 = final.count("l")
fl2 =final.count("o")
fl3 =final.count("v")
fl4 =final.count("e")

final_lcount= fl1+fl2+fl3+fl4

ft = str(final_tcount)
fl = str(final_lcount)

love =ft+fl

love_score = int(love)
if love_score < 10 or love_score >90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")    
elif love_score > 50 and love_score <90:
    print(f"Your score is {love_score}.")


print("sorry bro better luck next time")
