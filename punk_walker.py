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

def read_steps(filename="steps.csv"):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        return int(rows[-1]["steps"])

def get_message(steps, goal=6000):
    if steps < goal * 0.5:
        return random.choice(MESSAGES["low"])
    elif steps < goal:
        return random.choice(MESSAGES["medium"])
    else:
        return random.choice(MESSAGES["high"])

def main():
    steps = read_steps()
    message = get_message(steps)
    print(f"Today's steps: {steps}")
    print(message)

if __name__ == "__main__":
    main()
