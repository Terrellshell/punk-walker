# Punk Walker

Punk Walker is a simple, attitude-heavy step tracker designed to keep you moving with direct, no-nonsense motivation.

## What It Does
- Reads your daily step count from a CSV file or manual input
- Compares it to your daily goal
- Responds with a punk-style motivational message

## Example Messages
- "Move your boots, make the change."
- "You're not dead yet — keep walking."
- "Punk isn't about sitting still."
- "You hit your goal. Respect."
- "3,000 steps? That's adorable. Try again."

## How To Use
1. Add your daily steps to `steps.csv`
2. Run the script:


## Example CSV Format
date,steps  
2026-01-17,4500

## What I Learned
- Reading CSV files in Python
- Basic logic and conditionals
- Writing simple functions
- Using GitHub for version control

## New Tier-2 Feature: Daily Logging
Punk Walker now keeps a daily log of your steps in `log.csv`.

Each time you run the script:
- It records today's date
- It appends your step count
- It builds a history for future stats
