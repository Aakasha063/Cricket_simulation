# Advanced Cricket Tournament Simulation Program using Python

This is an advanced cricket tournament simulation program implemented in Python. The program allows you to simulate cricket matches between two teams, calculate scores, and track player statistics based on their abilities and the field conditions.

## Methodology

The program is structured using several classes:
- `Player`: Represents a player with attributes such as name, batting ability, bowling ability, fielding ability, running ability, and experience.
- `Team`: Represents a cricket team and manages the players in the team.
- `Field`: Defines the characteristics of the cricket field, including size, fan ratio, pitch conditions, and home advantage.
- `Umpire`: Simulates the umpire's role by predicting the outcome of each ball based on player abilities and field conditions.
- `Commentator`: Provides commentary for each ball, describing the outcome and player actions.
- `Match`: Orchestrates the match by managing the innings, scoring, wickets, and overs.

The program uses probability calculations to determine the outcome of each ball based on the batting and bowling abilities of the players, field conditions, and randomization.

## Running the Program

To run the program, follow these steps:

1. Make sure you have Python installed on your system (version 3 or above).

2. Clone this repository to your local machine or download the source code files.

3. Open a command-line interface or terminal and navigate to the program files' directory.

4. Run the following command in the terminal to start the simulation or run the code in any IDE.

   python main.py

