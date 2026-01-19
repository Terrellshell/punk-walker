import csv
import random

MESSAGES = {
    "low": [
        "Move your boots, make the change.",
        "You're not dead yet — keep walking.",
        "Punk isn't about sitting still."
    ],
    "medium": [
        "Not bad. But you can do better.",
        "Keep pushing. Punk doesn't coast.",
        "You're warming up — now get loud."
    ],
    "high": [
        "You hit your goal. Respect.",
        "That's the spirit. Keep stomping.",
        "Punk approved. Now go drink water."
    ]
}

def log_steps(steps, filename="log.csv"):
    """Append today's steps to the log file."""
    today = date.today().isoformat()

    # Check if file exists and needs a header
    try:
        with open(filename, "r") as file:
            pass  # File exists, do nothing
    except FileNotFoundError:
        # Create file with header
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "steps"])

    # Append today's entry
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([today, steps])
        
def get_message(steps, goal=6000):
    if steps < goal * 0.5:
        return random.choice(MESSAGES["low"])
    elif steps < goal:
        return random.choice(MESSAGES["medium"])
    else:
        return random.choice(MESSAGES["high"])

def main():
    steps = int(input("Enter today's steps: "))
    log_steps(steps)
    message = get_message(steps)
    print(f"Today's steps: {steps}")
    print(message)

if __name__ == "__main__":
    main()



