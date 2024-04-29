import threading
import time
import random
import unittest

class Team:
    def __init__(self, name):
        self.name = name

class Match:
    def __init__(self, match_id, team1, team2, team1_score=None, team2_score=None):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.team1_score = team1_score
        self.team2_score = team2_score
        self.winner = None

class Match_Result_Tracker:
    def __init__(self):
        self.matches = {}
        self.next_match_id = 1
        self.team_stats = {}  # Dictionary to store team statistics

    def create_match(self, team1, team2):
        match_id = self.next_match_id
        match = Match(match_id, team1, team2)
        self.matches[match_id] = match
        self.next_match_id += 1
        print(f"Match {match_id} created between {team1.name} and {team2.name}")

    def update_match_score(self, match_id, team1_score, team2_score):
        match = self.matches.get(match_id)
        if match:
            match.team1_score = team1_score
            match.team2_score = team2_score
            if team1_score > team2_score:
                match.winner = match.team1.name
            elif team2_score > team1_score:
                match.winner = match.team2.name
            else:
                match.winner = "Draw"
            self._update_team_stats(match.team1, match.team2, match.winner)
            self._update_team_stats(match.team2, match.team1, match.winner)
            print(f"Match {match_id} score updated")

    def _update_team_stats(self, winning_team, losing_team, result):
        if winning_team.name in self.team_stats:
            self.team_stats[winning_team.name]["wins"] += 1
        else:
            self.team_stats[winning_team.name] = {"wins": 1, "losses": 0, "draws": 0}
        
        if losing_team.name in self.team_stats:
            if result == "Draw":
                self.team_stats[losing_team.name]["draws"] += 1
            else:
                self.team_stats[losing_team.name]["losses"] += 1
        else:
            if result == "Draw":
                self.team_stats[losing_team.name] = {"wins": 0, "losses": 0, "draws": 1}
            else:
                self.team_stats[losing_team.name] = {"wins": 0, "losses": 1, "draws": 0}

    def delete_match(self, match_id):
        if match_id in self.matches:
            match = self.matches[match_id]
            if match.winner != "Draw":
                if match.winner == match.team1.name:
                    self._update_team_stats(match.team1, match.team2, "loss")
                    self._update_team_stats(match.team2, match.team1, "win")
                else:
                    self._update_team_stats(match.team1, match.team2, "win")
                    self._update_team_stats(match.team2, match.team1, "loss")
            else:
                self._update_team_stats(match.team1, match.team2, "draw")
                self._update_team_stats(match.team2, match.team1, "draw")
            del self.matches[match_id]
            print(f"Match {match_id} deleted successfully")
        else:
            print(f"Match {match_id} not found")

    def display_match_details(self, match_id):
        match = self.matches.get(match_id)
        if match:
            print(f"Match ID: {match.match_id}")
            print(f"Team 1: {match.team1.name} (Score: {match.team1_score})")
            print(f"Team 2: {match.team2.name} (Score: {match.team2_score})")
            print(f"Winner: {match.winner}")
        else:
            print(f"Match {match_id} not found")

    def display_team_stats(self):
        print("Team Statistics:")
        for team_name, stats in self.team_stats.items():
            print(f"{team_name} :\t\t Wins - {stats['wins']}, Losses - {stats['losses']}, Draws - {stats['draws']}")

# Example usage
if __name__ == "__main__":
    # Create Match_Result_Tracker instance
    tracker = Match_Result_Tracker()

    # Create teams
    team1 = Team("Mumbai Indians")
    team2 = Team("Chennai Super Kings")
    team3 = Team("Royal Challengers Bangalore")
    team4 = Team("Kolkata Knight Riders")
    team5 = Team("Chennai Super Kings")
    team6 = Team("Royal Challengers Bangalore")

    # Schedule matches
    tracker.create_match(team1, team2)
    tracker.create_match(team3, team4)
    tracker.create_match(team5, team6)

    # Update match scores
    tracker.update_match_score(1, 180, 170)
    tracker.update_match_score(2, 150, 160)
    tracker.update_match_score(3, 200, 190)

    # Display match details
    tracker.display_match_details(1)
    tracker.display_match_details(2)
    tracker.display_match_details(3)
    tracker.display_match_details(4)
    

    # Delete a match
    tracker.delete_match(1)

    # Display match details after deletion
    tracker.display_match_details(1)  
    tracker.display_match_details(2)
    tracker.display_match_details(3)
    tracker.display_match_details(4)
    
    # Display team statistics
    tracker.display_team_stats()

