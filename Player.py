from Skills import *

rest = Rest()
cease_fire = CeaseFire()
string_to_defensive_skill = {"a" : Avoid(), \
    "b" : Block(), \
    "c" : Clash(), \
    "f" : rest, \
    "strike" : rest}
string_to_offensive_skill = {"a" : cease_fire, \
    "b" : cease_fire, \
    "c" : cease_fire, \
    "f" : Shoot(), \
    "strike" : Strike()
    }

class Player():
    def __init__(self, name, max_hp = 20, max_phase = 5, max_shield_hp = 10):
        self.name = name

        self.max_hp = max_hp
        self.hp = max_hp

        self.max_phase = max_phase
        self.phase = max_phase

        self.max_shield_hp = max_shield_hp
        self.shield_hp = max_shield_hp

        self.offense_state = None
        self.defense_state = None

        self.phase = 0
        self.max_phase = max_phase

    def act(self, act_string):
        '''
        Selects the appropriate offensive and defensive moves.
        If the player has insufficient phases / is gaining phases then default (CeaseFire and Rest) is loaded in.
        The offense_state and defense_state for both players will be processed after.
        '''
        if act_string == "+":
            if self.phase < self.max_phase:
                self.phase += 1
            self.offense_state = cease_fire
            self.defense_state = rest
        else:
            self.offense_state = string_to_offensive_skill[act_string]
            if self.offense_state.phase_cost > self.phase:
                self.offense_state = cease_fire
            self.phase -= self.offense_state.phase_cost

            self.defense_state = string_to_defensive_skill[act_string]
            if self.defense_state.phase_cost > self.phase:
                self.defense_state = rest
            self.phase -= self.defense_state.phase_cost

    def __str__(self):
        return f"Player {self.name} : HP: {self.hp} / {self.max_hp}, Shield: {self.shield_hp}" + \
               f" / {self.max_shield_hp}, Phases: {self.phase} / {self.max_phase}"

    
        