
# Soldier
import random

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
       return self.strength

    def receiveDamage(self,damage):
        self.health = self.health - damage



# Viking


class Viking(Soldier):
     def __init__(self, name, health, strength):
            #Soldier.__init__(self,health,strength)
            self.name = name
            self.health = health
            self.strength = strength

     def receiveDamage(self,damage):
          self.health = self.health - damage
          if self.health > 0:
                return self.name + ' has received '+ str(damage) + ' points of damage'
          else:
                return self.name + ' has died in act of combat'

     def battleCry(self):
         return "Odin Owns You All!"

# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        #Soldier.__init__(self, health, strength)
        self.health=health
        self.strength=strength

    def receiveDamage(self,damage):
        self.health = self.health - damage
        if self.health > 0:
                return 'A Saxon has received '+ str(damage) + ' points of damage'
        else:
                return 'A Saxon has died in combat'


# War


class War:
        def __init__(self):
            self.vikingArmy = []
            self.saxonArmy = []


        def addViking(self, Viking):
            self.vikingArmy.append(Viking)

        def addSaxon(self, Saxon):
            self.saxonArmy.append(Saxon)

        def vikingAttack(self):
            s = random.choice(self.saxonArmy)
            v = random.choice(self.vikingArmy)
            s.receiveDamage(v.strength)
            if s.health <= 0:
                self.saxonArmy.remove(s)
            return "A Saxon has died in combat"

        def saxonAttack(self):
            s = random.choice(self.saxonArmy)
            v = random.choice(self.vikingArmy)
            v.receiveDamage(s.strength)
            if v.health <= 0:
                self.vikingArmy.remove(v)
            else:
                return str(v.name) + ' has received '+ str(s.strength) + ' points of damage'
        def showStatus(self):
            if self.saxonArmy == []:
                return 'Vikings have won the war of the century!'
            if self.vikingArmy == []:
                return 'Saxons have fought for their lives and survive another day...'
            if self.vikingArmy != [] and self.saxonArmy != []:
                return 'Vikings and Saxons are still in the thick of battle.'
