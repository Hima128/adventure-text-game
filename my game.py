import random
import time


def show_options(options):
    """Display options to the player."""
    print("Choose an option:")
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")


def get_user_choice(options):
    """Get the user's choice."""
    choice = get_valid_input("Enter the number of your choice: ", list(map(str, range(1, len(options) + 1))))
    return int(choice)


def update_score(points):
    """Update the score by adding the given points."""
    global score
    score += points


def show_score():
    """Display the current score to the player."""
    print(f"Score: {score}")ybb


def start_game():
    """Start the game."""
    global score
    score = 0

    print("Welcome to the Adventure Game!")
    time.sleep(1)

    print("After discovering an old map, you find yourself at an archaeological site.")
    time.sleep(2)

    print("You feel a strong urge to explore the site.")
    time.sleep(2)

    while True:
        options = ["Explore the first room", "Go to the second room", "Go to the third room", "Exit"]
        show_options(options)
        choice = get_user_choice(options)

        if choice == 1:
            print("While exploring the first room, you find a rare artifact.")
            time.sleep(2)
            points = random.randint(1, 10)
            print(f"You gained {points} points!")
            update_score(points)
            time.sleep(1)
        elif choice == 2:
            print("You enter the second room and are surprised to find a giant monster!")
            time.sleep(2)
            print("A fierce battle ensues.")
            time.sleep(2)
            if random.random() > 0.5:
                print("You managed to defeat the monster!")
                points = random.randint(10, 20)
                print(f"You gained {points} points!")
                update_score(points)
                time.sleep(1)
                play_again = get_valid_input("Would you like to play again? (yes/no): ", ['yes', 'no'])
                if play_again == "yes":
                    start_game()
                else:
                    break
            else:
                print("The monster defeated you. Game over!")
                break
        elif choice == 3:
            print("You enter the third room and discover a hidden treasure.")
            time.sleep(2)
            points = random.randint(5, 15)
            print(f"You gained {points} points!")
            update_score(points)
            time.sleep(1)
        elif choice == 4:
            print("Thank you for playing!")
            break

        show_score()


def get_valid_input(prompt, valid_answers):
    """Ask the user for input and check if it's in the list of valid answers."""
    while True:
        user_input = input(prompt)
        if user_input in valid_answers:
            return user_input
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    start_game()
