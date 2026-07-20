def main():
    while True:
        score_input = input("Enter your game score (or type 'stop' to end): ")
        cleaned = score_input.strip().lower()

        if cleaned == "stop":
            print("Game session ended!")
            break

        try:
            score = int(score_input)
        except ValueError:
            print("Please enter a valid number or 'stop'.")
            continue

        if score > 100:
            print("Wow! That's a new high score!")
        else:
            print("Good try, keep playing!")


if __name__ == "__main__":
    main()
