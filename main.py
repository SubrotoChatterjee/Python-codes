import random
# List of colors
colors = ["red", "blue", "green", "yellow", "orange", "purple", "black", "white"]
# Scoreboard
scoreboard = {"games_won": 0, "games_lost": 0, "player_name": ""}
def start_game():
    machine_color = random.choice(colors)
    attempts = 5
    won = False
    print("\nGame Started! Guess the color.")
    while attempts > 0:
        user_color = input("Enter the color: ").lower()
        if user_color not in colors:
            print("Invalid color!")
            continue
        attempts -= 1
        if user_color == machine_color:
            print(f"You won the game!\nNumber of attempts: {5 - attempts}")
            won = True
            scoreboard["games_won"] += 1
            break
        else:
            print(f"Your guess was wrong. Please try again.\nAttempts left: {attempts}")
    if not won:
        print(f"\nYou lost the game! The correct color was '{machine_color}'.")
        scoreboard["games_lost"] += 1
    post_game_menu()
def post_game_menu():
    while True:
        print("\n1> See scoreboard\n2> Play again\n3> Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            print(f"\n--- Scoreboard ---\nPlayer Name: {scoreboard['player_name']}")
            print(f"Games Won: {scoreboard['games_won']}")
            print(f"Games Lost: {scoreboard['games_lost']}")
        elif choice == "2":
            start_game()
        elif choice == "3":
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Try again.")
def main():
    print("Welcome to the Color Game >>>")
    scoreboard["player_name"] = input("Please enter your name for the scoreboard: ")
    while True:
        print("\n1> Start Game\n2> Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            start_game()
        elif choice == "2":
            print("Bye See You Next Time")
            break
        else:
            print("Invalid choice. Try again.")
if __name__ == "__main__":
    main()