import sys
import os

# Get the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)



# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Now you can import the Game_rules class
from src.calander.day_2 import Game_rules, create_rigged_game

def test_calculate_score():
    test_games = [["A", "Y"],[ "B", "X"], ["C", "Z"]]
    game_rules = Game_rules()
    assert game_rules.calculate_score(test_games) == 6
    