class Skill():
    def __init__(self, name, phase_cost = 0):
        self.name = name
        self.phase_cost = phase_cost
    
    def apply_skill_effect(self, user):
        pass

class DefensiveSkill(Skill):
    def __init__(self, name, phase_cost = 0):
        super().__init__(name, phase_cost)

    def apply_skill_effect(self, user, target, offensive_skill):
        '''
        Stub code for apply_skill_effect
        Note that the user is the one who uses the defensive skill,
        and the target is the one who uses attacks him/her
        offensive_skill is the skill that this defensive skill is dealing with.
        '''
        pass

class Rest(DefensiveSkill):
    def __init__(self):
        super().__init__("Rest", 0)

    def apply_skill_effect(self, user, target, offensive_skill):
        offensive_skill.damage_target(user, offensive_skill.damage, offensive_skill.hit_times)

class Avoid(DefensiveSkill):
    '''
    Avoid skill object.
    '''

    def __init__(self):
        super().__init__("Avoid", 0)

    def apply_skill_effect(self, user, target, offensive_skill):
        '''
        Halves the hit_times of the offensive_skill by 2, rounding down, 
        then applies offensive_skill with the modified hit_times
        '''
        hit_times = offensive_skill.hit_times
        if offensive_skill.damage_type == "spinning":
            offensive_skill.damage_target(user, offensive_skill.avoid_damage, hit_times)
        elif offensive_skill.damage_type == "unavoidable":
            offensive_skill.damage_target(user, offensive_skill.damage, hit_times)
        else:
            hit_times //= 2
            offensive_skill.damage_target(user, offensive_skill.damage, hit_times)

class Block(DefensiveSkill):
    def __init__(self):
        super().__init__("Block", 0)

    def apply_skill_effect(self, user, target, offensive_skill):
        '''
        Applies offensive_skill under the condition that the target of the offensive
        skill is blocking.
        '''
        if offensive_skill.damage_type == "unblockable":
            offensive_skill.damage_target(user, offensive_skill.damage, \
                offensive_skill.hit_times, blocked = False)
        elif offensive_skill.damage_type == "electric":
            offensive_skill.damage_target(user, offensive_skill.effective_damage, \
                offensive_skill.hit_times, blocked = False)
        else:
            offensive_skill.damage_target(user, offensive_skill.damage, \
            offensive_skill.hit_times, blocked = True)

class Clash(DefensiveSkill):
    def __init__(self):
        super().__init__("Clash", 1)

    def apply_skill_effect(self, user, target, offensive_skill):
        '''
        Applies offensive_skill under the condition that the target of the offensive
        skill is clashing.
        '''
        if offensive_skill.damage_type == "melee":
            offensive_skill.damage_target(target, offensive_skill.damage, \
                offensive_skill.hit_times)
        elif offensive_skill.damage_type == "electric":
            offensive_skill.damage_target(user, offensive_skill.effective_damage, \
                offensive_skill.hit_times)
        else:
            offensive_skill.damage_target(user, offensive_skill.damage, \
                offensive_skill.hit_times)

    
class OffensiveSkill(Skill):
    def __init__(self, name, phase_cost = 0):
        super().__init__(name, phase_cost)
        self.damage = 0
        self.hit_times = 0
        self.damage_type = "ranged"

    def damage_target(self, target, damage, hit_times, blocked = False):
        '''
        Stub code for damage_target method.
        This is always called in a DefensiveSkill object.
        Specifically, the skill damages ``target`` with amount ``damage`` * ``hit_times, considering
        whether the ``target`` has ``blocked``. 
        '''
        if blocked:
            target.shield_hp -= damage * hit_times
            if target.shield_hp < 0:
                target.hp += target.shield_hp
                target.shield_hp = 0
        else:
            target.hp -= damage * hit_times
            if target.hp < 0:
                target.hp = 0
        pass

class CeaseFire(OffensiveSkill):
    def __init__(self):
        super().__init__("CeaseFire", 0)

class Shoot(OffensiveSkill):
    def __init__(self):
        super().__init__("Shoot", 0)
        self.damage = 1
        self.hit_times = 1
        
class Strike(OffensiveSkill):
    def __init__(self):
        super().__init__("Strike", 0)
        self.damage = 2
        self.hit_times = 1
        self.damage_type = "melee"

class MultiArrow(OffensiveSkill):
    def __init__(self):
        super().__init__("Multi Arrow", 1)
        self.damage = 1
        self.hit_times = 3
        self.damage_type = "ranged"

class SplashingArrow(OffensiveSkill):
    def __init__(self):
        super().__init__("Splashing Arrow", 1)
        self.damage = 0
        self.effective_damage = 4
        self.hit_times = 1
        self.damage_type = "spinning"

class ElectricArrow(OffensiveSkill):
    def __init__(self):
        super().__init__("Electric Arrow", 1)
        self.damage = 0
        self.effective_damage = 4
        self.hit_times = 1
        self.damage_type = "electric"
    
class ArrowStorm(OffensiveSkill):
    def __init__(self):
        super().__init__("Arrow Storm", 2)
        self.damage = 1
        self.hit_times = 5

class RicochetShot(OffensiveSkill):
    def __init__(self):
        super().__init__("Arrow of Wisdom", 3)
        self.damage = 6
        self.hit_times = 1
        self.damage_type = "unavoidable"

class EagleEyeAssault(OffensiveSkill):
    def __init__(self):
        super().__init__("Eagle Eye Assault", 5)
        self.damage = 3
        self.hit_times = 5