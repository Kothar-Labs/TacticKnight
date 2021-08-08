from Player import *

class GameState():
    def __init__(self):
        self.player1 = Player("P1")
        self.player2 = Player("P2")

    def one_round(self):
        self.player1.act(input(f"Input {self.player1.name}'s action:"))
        self.player2.act(input(f"Input {self.player2.name}'s action:"))
        self.player1.defense_state.apply_skill_effect(self.player1, self.player2, \
            self.player2.offense_state)
        self.player2.defense_state.apply_skill_effect(self.player2, self.player1, \
            self.player1.offense_state)

    def run_game(self):
        while self.player1.hp > 0 and self.player2.hp > 0:
            self.one_round()
            print(self.player1)
            print(self.player2)

