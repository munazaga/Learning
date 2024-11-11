import random

#Player class
class Player:
    def __init__ (self):
        self.max_HP = 30
        self.level = 1
        self.damage = 5
        self.heal = 3
        self.current_HP = self.max_HP
        self.charges = {"heal": 3, "fireball": 3}
        
    def attack (self, enemy):
        print (f"You attack the enemy for {self.damage} damage")    
        enemy.take_Damage(self.damage)
        
    def block (self, enemy_attack):
        blocked_damage = enemy_attack // 2
        print (f"You defend and you take {blocked_damage} damage")
        self.current_HP -= blocked_damage
        
    def healing (self):
        if self.charges["heal"] > 0:
            scaling_heal = (self.current_HP // 10) + self.heal  
            self.current_HP = min(self.current_HP + scaling_heal, self.max_HP)
            print (f"You heal {scaling_heal} HP.")
            self.charges["heal"] -= 1 
        else:
            print ("You are out of healing charges.")
            
    def fireball (self, enemy):
        if self.charges["fireball"] > 0:
            fireball_damage = self.damage * 2
            print (f"You cast a fireball for {fireball_damage} damage.")
            enemy.take_Damage(fireball_damage)
            self.charges["fireball"] -= 1
        else:
            print ("You are out of fireball charges.")
        
    def levelUp(self):
        print (f"\nYou have leveled up! Your level is now {self.level}")
        print ("1. Increase attack")
        print ("2. Increase Max HP")
        print ("3. Increase healing")

        while True:
            choice = input ("What would you like to do? Choose 1, 2 or 3.\n").strip()
            if choice == "1":
                self.damage += 5
                print ("You have increased your attack by 5.")
                break
            elif choice == "2":
                self.max_HP += 5
                self.current_HP += 5  
                print ("You have increased your max HP by 5.")
                break
            elif choice == "3":
                self.heal += 2
                print ("You have increased your healing by 2.")
                break
            else:
                print ("Invalid choice. Try again.")    
        
class Enemy:
    def __init__ (self, level):
        self.HP = 30
        self.attack_Power = 5 * level
        
    def take_Damage (self, damage):
        self.HP = max(0, self.HP - damage)   
        
    def enemy_attack (self, player):
        print (f"The enemy attacks you for {self.attack_Power} damage.")
        player.current_HP = max(0, player.current_HP - self.attack_Power)
    
    def enemy_block (self, player_Action):
        if player_Action == "fireball":
            Player.fireball()
        else:
            print (f"The enemy defends and takes no damage.")
        
    def counter_magic (self, player_Action, player):
        if player_Action == "heal":
            self.HP += player.scaling_heal
            print (f"The enemy counters magic and heals for {player.scaling_heal} HP.")
        elif player_Action == "fireball":
            print ("The enemy counters fireball and takes no damage.")
            
    def perform_Action (self, player):
        action = random.choice(["attack", "defend", "counter magic"])
        if action == "attack":
            self.enemy_attack(player)
        elif action == "defend":
            self.enemy_block()
        elif action == "counter magic":
            self.counter_magic(self, player)

class Game:
    def __init__ (self):
        self.playerA = Player()

    def game_Loop (self):
        while self.playerA.current_HP > 0:
            enemy = Enemy(self.playerA.level)
            print (f"You are level {self.playerA.level}")
            
            while enemy.HP > 0 and self.playerA.current_HP > 0:
                self.display_Stats(enemy)
                player_Action = input("You can choose to Attack, Defend, Heal or Fireball\n").lower()
                if player_Action == "attack":
                    self.playerA.attack(enemy)
                elif player_Action == "defend":
                    self.playerA.block(enemy)
                elif player_Action == "heal":
                    self.playerA.healing()
                elif player_Action == "fireball":
                    self.playerA.fireball(enemy)
                else:
                    print ("Invalid move. Try again.")
                    
                if enemy.HP > 0:    
                    enemy.perform_Action(self.playerA)
                else:
                    self.playerA.levelUp()
                    self.regain_Charges()
            
            if self.playerA.current_HP <= 0:
                print ("YOU DIED.")
                break

    def display_Stats (self, enemy):
        print (f"Your HP is: {self.playerA.current_HP}/{self.playerA.max_HP}, Enemy HP is: {enemy.HP}")
        print (f"You have {self.playerA.charges['heal']} healing charges and {self.playerA.charges['fireball']} fireball charges.")
    
    def regain_Charges (self):
        if random.random() < 0.5:
            self.playerA.charges["heal"] += 1
            print ("You have regained a healing charge.")
        if random.random() < 0.3:
            self.playerA.charges["fireball"] += 1
            print ("You have regained a fireball charge.")
        if random.random() < 0.05:
            self.player_HP = self.player_max_HP
            print ("You have regained full HP.")
        
game = Game()
game.game_Loop()
