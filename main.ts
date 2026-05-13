game.splash("Welcome to Guess the number program")
let users_number = game.askForNumber("between 1 and 6")
let computers_number = randint(1, 6)
if (users_number == computers_number) {
    game.splash("Your answer is correct")
} else {
    game.splash("Your answer is wrong. The correct answer is: ", computers_number)
}
