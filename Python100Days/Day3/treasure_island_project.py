"""
start off asking you, "You're at a crossroad.
Do you want to go left or right?"

If you selected left, then it's going to take you to a lake,
and it asks you whether if you want to wait for a boat or swim across.
And then the final step is it asks you, which door would you like to go through red, yellow or blue?

The Game will be over if any of the below actions are taken:
1. If choose to go right
2. If choose to swim
3. If choose Red or Blue door
"""

"""
To get ASCII ART to display on screen as a part of game : ctr + F 
"""

import pyfiglet

# Generate ASCII art for "GAME TIME"
ascii_art = pyfiglet.figlet_format("GAME TIME", font="slant")
print(ascii_art)


print("You're at a Crossroad.")
print("Your mission is to find the treasure.")


direction = (input("Where do you want to go left 'L' or right 'R'?")).lower()
activity = (input("Do you want to 'swim' or 'wait' for the boat?")).lower()
door = (input("Which door would you like to go through, 'Red', 'Yellow', 'Blue'?")).lower()

if direction == "l":
    # print("You are one step towards lake, You didn't fall into a hole, Game will continue...")
    if activity == 'wait':
        # print("You have arrived the island unarmed, which door you want to open?")
        if door == "yellow":
            print("You have opened the right door of treasure, You Win!")
else:
    print("Game Over!!!")


# You can as many if-else statements building story of the game, giving separate descriptions like
# Wrong move, beast on blue door, fire on red door, drained in water if choose swim etc.
# Try to write the messages in interesting way.