import random

def computer_turn():
    return random.choice(["rock", "paper", "scissors"])

def decide_outcome(player, cpu):
    outcomes = {
        ("rock", "scissors"): "win",
        ("scissors", "paper"): "win",
        ("paper", "rock"): "win",
        ("scissors", "rock"): "lose",
        ("paper", "scissors"): "lose",
        ("rock", "paper"): "lose"
    }
    if player == cpu:
        return "tie"
    return outcomes.get((player, cpu), "lose")

def play_game():
    player_points = 0
    cpu_points = 0
    round_count = 1

    while True:
        print(f"\n--- Round {round_count} ---")
        player_choice = input("Your move (rock/paper/scissors or quit): ").strip().lower()

        if player_choice == "quit":
            print("\nThanks for playing! Final Score -> You:", player_points, "| Computer:", cpu_points)
            break

        if player_choice not in ["rock", "paper", "scissors"]:
            print("❗ Invalid input. Please choose rock, paper, or scissors.")
            continue

        cpu_choice = computer_turn()
        print(f"💻 Computer picked: {cpu_choice}")

        outcome = decide_outcome(player_choice, cpu_choice)

        if outcome == "win":
            print("✅ You won this round!")
            player_points += 1
        elif outcome == "lose":
            print("❌ You lost this round.")
            cpu_points += 1
        else:
            print("🤝 It's a tie.")

        print(f"Scoreboard → You: {player_points} | Computer: {cpu_points}")
        round_count += 1

if __name__ == "__main__":
    play_game()