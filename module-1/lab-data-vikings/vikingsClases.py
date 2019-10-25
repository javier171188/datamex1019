
# Soldier


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
            Soldier.__init__(self,health,strength)
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
        Soldier.__init__(self, health, strength)
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
            Saxon.receiveDamage(Viking.atack)
            if Saxon.health <= 0: 
                self.saxonArmy.remove(Saxon)
            return Saxon.receiveDamage(Viking.attack)
        
        def saxonAttack(self):
            Viking.receiveDamage( Saxon.attack)
            if Saxon.health <= 0: 
                self.vikingArmy.remove(Viking)
            return Viking.receiveDamage(Saxon.attack)
        def showStatus(self):
            if saxonArmy == []:
                return 'Vikings have won the war of the century!'
            if vikingArmy == []:
                return 'Saxons have fought for their lives and survive another day...'
            if vikingArmy != [] and saxonArmy != []:
                return 'Vikings and Saxons are still in the thick of battle.'
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
