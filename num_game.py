import random
wining_number = random.randint(1,100)
guess = 1
num = int(input("Guess number between 1 to 100: "))
game_over = False
while not game_over:
    if num == wining_number:
        print(f"You Won. Number gussed in {guess} attempt. ")
        game_over = True
    else:
        if num < wining_number:
            print("You Guess Too Low. Guess Again.")
        else:
            print("You Guess Too High. Guess Again.")

        guess += 1
        num = int(input("Guess Again: "))
        if guess == 10:
            game_over = True
            print("You tried maximum attempt. Game Over")
    
