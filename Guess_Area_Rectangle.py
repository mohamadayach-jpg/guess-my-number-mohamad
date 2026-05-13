# Guess the area of a rectangle
# This program will ask the user for the deminsions of a rectangle .
# It will then calculate the area and asks the user to guess it .

print ("Guess the area of the rectangle")

# get the length from the user and convert it to an integer.
base1 =  int(input("Enter the length (cm): "))

# get the width from the user and convert it to an integer.
base2 =  int(input("Enter the width (cm): "))

# calculate the area of the rectangle
area = base1 * base2
# ask the user to guess the area of the rectangle 
print("guess the area of the rectangle")

guess = int(input("Enter your guess (cm^2): "))
# check if the user's guess is correct
if guess == area:   
    print("Congratulations! You guessed the area correctly.")
else:       
    print("Sorry, your guess is wrong. The area of this rectangle is", area, "cm^2.")
