# Dungeon and dragon

# Character, Warrior, Archer, Wizard, Dragon

# name, hp, power, armor, spd, ability, 
import random

class Character():
    # constructor, init/begin/start
    def __init__(self, name, hp, power, armor, spd, weapon):
        self.name = name
        self.hp = hp
        self.power = power
        self.armor = armor
        self.spd = spd
        self.weapon = weapon
    
    def print_info(self):
        print("--name:", self.name)
        print("--hp:", self.hp)
        print("--power:", self.power)
        print("--armor:", self.armor)
        print("--spd:", self.spd)
        print("--weapon:", self.weapon)


    def strike(self,enemy):
        print(self.name, "strikes", enemy.name, 'with', self.weapon)

        critical = random.randint(1,10) <= 2
        if critical:
            print("It's a CRITICAL HIT!!!")
            bonus_dmg = 1.5
        else:
            bonus_dmg = 1
        
        dmg = self.power*bonus_dmg - enemy.armor

        # hp_lost = 0 if enemy.hp-dmg <0 else enemy.hp-dmg

        if enemy.hp-dmg<0:
            hp_lost = 0
        else:
            hp_lost = enemy.hp-dmg


        print(enemy.name+"'s HP went down from",enemy.hp, "to", hp_lost)
        enemy.hp-= dmg

        

    def ability(self, ability_name):
        # auto_heal, increase_atk, increase_armor, 
        if ability_name =="auto_heal":
            self.hp+=30
            print("auto heal activated, hp")
        if ability_name =="increase_atk":
            pass
        if ability_name =="increase_armor":
            pass
    



# order
Jame = Character('Jame',200, 30, 20, 10, 'axe')
Helen = Character('Helen',100, 30, 20, 20, 'bow')

while Jame.hp >0 and Helen.hp>0:
    if Jame.spd > Helen.spd:
        Jame.strike(Helen)
        Helen.strike(Jame)

    else:
        Helen.strike(Jame)
        Jame.strike(Helen)
