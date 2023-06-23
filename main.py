'''Advanced Cricket Tournament Simulation Program using Python'''

import random

class Player:

    def __init__(self, name, batting_ability, bowling_ability, fielding_ability, running_ability, experience):
        self.name = name
        self.batting_ability = batting_ability
        self.bowling_ability = bowling_ability
        self.fielding_ability = fielding_ability
        self.running_ability = running_ability
        self.experience = experience
        self.score = 0
        self.is_out = False

    def __repr__(self):
        return f"Player(name={self.name}, batting={self.batting_ability}, bowling={self.bowling_ability})"


class Team:

    def __init__(self, name):
        self.name = name
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def select_captain(self):
        max_experience = max(player.experience for player in self.players)
        captain = [player for player in self.players if player.experience == max_experience]
        return captain

    def send_next_player_to_field(self):
        for player in self.players:
            if not player.is_out:
                return player

    def decide_batting_order(self):
        batting_order = sorted(self.players, key=lambda player: player.batting_ability, reverse=True)
        return batting_order
    
    def choosing_bowler(self):
        choose_bowler = sorted(self.players, key=lambda player: player.bowling_ability, reverse=True)
        return choose_bowler[0]


class Field:

    def __init__(self, size, fan_ratio, pitch_conditions, home_advantage):
        self.size = size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

    def get_probability(self, event):
        if event == "six":
            return self.fan_ratio * self.pitch_conditions * self.home_advantage
        if event == "four":
            return self.size * self.fan_ratio * self.pitch_conditions * self.home_advantage
        elif event == "out":
            return 1 - self.size * self.fan_ratio * self.pitch_conditions
        elif event == "lbw":
            return self.pitch_conditions * self.home_advantage
        elif event == "catch":
            return self.pitch_conditions * (1 - self.home_advantage)
        elif event == "run_out":
            return self.fan_ratio
        else:
            return 1.0


class Umpire:

    def __init__(self, field):
        self.field = field
        self.overs = 0
        self.score = 0
        self.wicket = 0

    def predict_outcome_of_ball(self, batsman, bowler):
        batting_ability = batsman.batting_ability
        bowling_ability = bowler.bowling_ability

        total_probabilities = {
            "six": self.field.get_probability("six") * batting_ability,
            "four": self.field.get_probability("four") * batting_ability ,
            "two": self.field.get_probability("two") * batting_ability - bowling_ability,
            "out": self.field.get_probability("out") * (1 - batting_ability) * (1 - bowling_ability),
            "lbw": self.field.get_probability("lbw") * (1 - batting_ability) * (1 - bowling_ability),
            "catch": self.field.get_probability("catch") * (1 - batting_ability) * (1 - bowling_ability),
            "run_out": self.field.get_probability("run_out") * (1 - batting_ability)
        }

        probability_sum = sum(total_probabilities.values())
        probabilities = {event: prob / probability_sum for event, prob in total_probabilities.items()}

        outcome = random.choices(list(probabilities.keys()), list(probabilities.values()))[0]
        return outcome

    def keep_track_of_scores_wickets_overs(self, outcome, batsman):        
        if outcome == "six":
            runs_scored = 6
            batsman.score += runs_scored
        elif outcome == "four":
            runs_scored = 4
            batsman.score += runs_scored
        elif outcome == "two":
            runs_scored = 2
            batsman.score += runs_scored
        elif outcome == "out":
            batsman.is_out = True
        elif outcome == "lbw":
            batsman.is_out = True
        elif outcome == "catch":
            batsman.is_out = True
        elif outcome == "run_out":
            batsman.is_out = True

        self.overs += 1.0


class Commentator:

    def __init__(self, match):
        self.match = match

    def provide_commentary(self, ball_number, outcome, batsman):
        print(f"Ball {ball_number}: {batsman.name} {self.get_commentary(outcome)}!")

    def get_commentary(self, outcome):
        if outcome == "six":
            return "hits a six"
        elif outcome == "four":
            return "hits a four"
        elif outcome == "two":
            return "took two runs"
        elif outcome == "out":
            return "is out"
        elif outcome == "lbw":
            return "is out LBW"
        elif outcome == "catch":
            return "is caught out"
        elif outcome == "run_out":
            return "is run out"


class Match:

    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field

    def start_match(self):
        display_separator()
        print(f"Match between {self.team1.name} and {self.team2.name} starts!")
        self.play_innings(self.team1, self.team2)
        self.play_innings(self.team2, self.team1)
        display_separator()
        print("Match ended!")
        display_separator()

    def play_innings(self, batting_team, bowling_team):
        display_separator()
        print(f"{batting_team.name} is batting now!")
        display_separator()
        umpire = Umpire(self.field)
        commentator = Commentator(self)

        batting_team.is_out = False

        for _ in range(5):  # 5 overs per team
            all_out = False  # Flag to check if all players are out
            for ball_number in range(1, 7):  # 6 balls per over
                batsman = batting_team.send_next_player_to_field()
                if batsman is None:  # Check if all players are out
                    all_out = True
                    break

                bowler = bowling_team.choosing_bowler()
                outcome = umpire.predict_outcome_of_ball(batsman, bowler)
                umpire.keep_track_of_scores_wickets_overs(outcome, batsman)
                commentator.provide_commentary(ball_number, outcome, batsman)

                if outcome == "out" or outcome == "lbw" or outcome == "catch" or outcome == "run_out":
                    batsman.is_out = True

            if all_out:
                break

        total_runs = sum(player.score for player in batting_team.players)
        total_overs = umpire.overs
        total_wickets = sum(player.is_out for player in batting_team.players)
        display_separator()
        print(f"{batting_team.name} scored {total_runs} runs in {total_overs/6:.1f} overs with {total_wickets} wickets.")


#creating a seperter function to print "===" so that output is visually attractive
def display_separator():
    print("=" * 70)

    
# Create players and pass parameters as name, batting_ability, bowling_ability, fielding_ability, running_ability, experience

player1 = Player("MS Dhoni", 0.8, 0.2, 0.8, 0.6, 1)
player2 = Player("Virat Kohli", 0.9, 0.1, 0.4, 0.9, 0.9)
player3 = Player("Rohit Sharma", 0.8, 0.1, 0.5, 0.3, 0.8)
player4 = Player("Jasprit Bumrah", 0.2, 0.8, 0.4, 0.2, 0.5)
player5 = Player("Hardik Pandya", 0.6, 0.4, 0.3, 0.5, 0.7)
player6 = Player("Chris Gale", 0.4, 0.5, 0.7, 0.6, 0.9)
player7 = Player("Sachin Tendulkar", 0.7, 0.6, 0.3, 0.2, 1.2)
player8 = Player("Yuvraj Singh", 0.4, 0.6, 0.2, 0.3, 0.6)
player9 = Player("Shubman Gill", 0.6, 0.3, 0.5, 0.4, 0.7)
player10 = Player("Ravinder Jadeja", 0.2, 0.7, 0.4, 0.6, 0.9)

# Create teams
team1 = Team("Chennai Super Kings")
team1.add_player(player1)
team1.add_player(player2)
team1.add_player(player3)
team1.add_player(player4)
team1.add_player(player5)

team2 = Team("Delhi Daredevils")
team2.add_player(player6)
team2.add_player(player7)
team2.add_player(player8)
team2.add_player(player9)
team2.add_player(player10)

# Create field
field = Field(1.2, 0.8, 0.7, 0.9)

# Create match
match = Match(team1, team2, field)
match.start_match()
