from utils import timer, read_input

RULES = {"A":{"win": "Z","lose":"Y", "draw":"X" }, 
            "B":{"win": "X","lose":"Z", "draw":"Y", },
            "C":{"win": "Y","lose":"X", "draw":"Z", },
            } 

class Game_rules():
    def __init__(self) -> None:
        self.rules = {"A":{"win": "Z","lose":"Y", "draw":"X" }, 
            "B":{"win": "X","lose":"Z", "draw":"Y"},
            "C":{"win": "Y","lose":"X", "draw":"Z"},
            } 
        self.token_score = {"X": 1, "Y": 2, "Z": 3}
        self.score = 0  
        
    #get token player 1 needs to win   
    def get_win_token(self, token):
        return self.rules[token]["win"]
    
    #get token player 1 needs to lose
    def get_lose_token(self, token):
        return self.rules[token]["lose"]
    
    #get token players need to draw
    def get_draw_token(self, token: str) -> str:
        return self.rules[token]["draw"]
    
    def get_score(self, token):
        return self.score
    
    def update_score(self, token, result):
        self.score += self.token_score[token]
        self.score += 3 if result == "draw" else 6 if result == "win" else 0

    def calculate_score(self, games: list[list[str]] ) -> int:
        for opponent_token, player_token in games:
                    #if players draw
                    if self.get_draw_token(opponent_token) == player_token:
                        self.update_score(player_token, "draw")
                    #if player 2 wins    
                    elif self.get_lose_token(opponent_token) == player_token:
                        self.update_score(player_token, "win")
                    #if player 1 wins
                    elif self.get_win_token(opponent_token) == player_token:
                        self.update_score(player_token, "lose")
        return self.score
                    
        
        
def create_rigged_game( games: list[list[str]], game_rules: Game_rules) -> list[list[str],]:
    new_games=[]
    for opponent_token, player_token in games:
        match player_token:
            #need to lose
            case "X":
                new_games.append([opponent_token, game_rules.get_win_token(opponent_token)])
            #need to draw
            case "Y":
                new_games.append([opponent_token, game_rules.get_draw_token(opponent_token)])
            #need to win
            case "Z":
                new_games.append([opponent_token, game_rules.get_lose_token(opponent_token)])
    return new_games

@timer
def main():
    test_games = [["A", "Y"],[ "B", "X"], ["C", "Z"]]

    #part 1
    game_part_1 = Game_rules()
    game_part_2 = Game_rules()
    input_lines = read_input(2).split("\n")
    input_lines.pop()
    input_games = [[char for char in single_game.split()] for single_game in input_lines] 
    part_1_score = game_part_1.calculate_score(input_games)
    
    #part 2
    rigged_games = create_rigged_game(games=input_games, game_rules=game_part_2)
    #print (rigged_games)
    part_2_score = game_part_2.calculate_score(rigged_games)

    print (f"The total score is {part_1_score} for part 1")
    print (f"The total score is {part_2_score} for part 2")

if __name__ == "__main__":
    main()  