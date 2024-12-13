print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
cross_road = input('You are infront of a cross road. Where do you want to go? choose "left" or "right": ').lower()
cross_river = input('You are infront of a river. Do you want to swim or wait for a boat? choose "swim" or "wait": ').lower()
through_door = input('You are infront of 3 doors. Which door do you want to go through? choose "red", "yellow", or "blue" ').lower()

if cross_road == "left":
    if cross_river == "wait":
        if through_door == "yellow":
            print("You found the door. You win")
        elif through_door == "red":
            print("You've entered a door full of fire. Game over")
        elif through_door == "blue":
            print("You've entered a room of beast. Game over")
        else:
            print("You have choosed a door that does not exist")
    else:
        print("You got attacked by angry trout. Game Over")
else:
    print("You fell into a hole. Game Over")