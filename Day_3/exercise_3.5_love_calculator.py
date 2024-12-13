print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

name = name1 + name2
name = name.lower()
T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")
TRUE = T + R + U + E
print(TRUE)
L = name.count("l")
O = name.count("o")
V = name.count("v")
E = name.count("e")
LOVE = L + O + V + E
print(LOVE)

love_score = str(TRUE) + str(LOVE)

if love_score < "10" or love_score > "90":
    print("Your score is {love_score}, you go together like coke and mentos")
elif love_score >= "40" and love_score <= "50":
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
