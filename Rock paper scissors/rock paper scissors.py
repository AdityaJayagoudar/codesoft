import random

# Function to get user's choice
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

# Function to get computer's random choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner and update the score
def determine_winner(user_choice, computer_choice, scores):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        scores['user'] += 1  # User wins this round
        return "You win!"
    else:
        scores['computer'] += 1  # Computer wins this round
        return "Computer wins!"

# Function to play the game
def play_game(scores):
    print("\n=== Welcome to Rock, Paper, Scissors Game! ===")
    
    user_choice = get_user_choice()  # Get user's choice
    computer_choice = get_computer_choice()  # Get computer's choice
    
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice, scores)  # Determine who won
    print(f"Result: {result}")

    # Display current score
    print(f"Score -> You: {scores['user']} | Computer: {scores['computer']}")

# Main function to run the game with replay option
def main():
    scores = {'user': 0, 'computer': 0}  # Initialize scores for user and computer
    
    while True:
        play_game(scores)  # Play the game and update the score
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nFinal Score -> You: {scores['user']} | Computer: {scores['computer']}")
            print("Thanks for playing!")
            break

# Call the main function to start the game
if __name__ == "__main__":
    main()
