room = "hall"
has_key = False

print("You are in a hall. Exits: north, east")

while True:
    move = input("\n> ").lower()

    if room == "hall":
        if move == "east":
            room = "kitchen"
            print("You are in the kitchen. A key lies on the table. Exit: west")
        elif move == "south":
            if has_key:
                print("You unlock the door and escape! You win!")
                break
            else:
                print("The door is locked")
        else:
            print("You can't do that")

    elif room == "kitchen":
        if move == "take key":
            has_key = True
            print("You take the key")
        elif move == "west":
            room = "hall"
            print("You are back in the hall. The locked door is south")
        else:
            print("You can't do that")