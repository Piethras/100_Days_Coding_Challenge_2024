import random

names_string = input("give me everybody's names, separate by a comma: ")
names = names_string.split(", ")
print(names)

# random_choice = random.randint(0, len(names) - 1)
# print(random_choice)
# random_name = names[random_choice]
random_name = random.choice(names)
print(random_name + " is going to pay for the meal.")