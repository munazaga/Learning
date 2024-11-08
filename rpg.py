import random

#Possible moves
moves = ["attack", "defend", "heal", "fireball"]
charges = {"heal": 3, "fireball": 3}

#Starting stats
player_Max_HP = 30
player_HP = player_Max_HP 
enemy_HP = 30
player_Level = 1
damage = 5
enemy_Damage = int (player_HP / 5)
heal = 3


#Functions
def levelUp():
    global player_Max_HP , player_HP, player_Level, damage, heal
    player_Level += 1
    print (f"\nYou have leveled up! Your level is now {player_Level}")
    print ("1. Increase attack")
    print ("2. Increase Max HP")
    print ("3. Increase healing")

    while True:
        choice = input ("What would you like to do? Choose 1, 2 or 3.\n").strip()
        if choice == "1":
            damage += 5
            print ("You have increased your attack by 5.")
            break
        elif choice == "2":
            player_Max_HP += 5
            player_HP += 5  
            print ("You have increased your max HP by 5.")
            break
        elif choice == "3":
            heal += 2
            print ("You have increased your healing by 2.")
            break
        else:
            print ("Invalid choice. Try again.")

#Game loop    
while player_HP > 0:
    print (f"\nYour level is {player_Level}.")
    enemy_HP = player_Level * 5
    
    #Battle Loop
    while player_HP > 0 and enemy_HP > 0:
        print (f"You have {player_HP} HP. The enemy has {enemy_HP} HP.")
        player_Move = input("You can choose to Attack, Defend , Heal or Fireball\n").lower()
        if player_Move not in moves:
            print ("Invalid move. Try again.")
            continue
        #Enemy actions are random    
        enemy_Move = random.choice(["attack", "defend", "counter magic"])
        
        #Player actions
        
        if player_Move == "attack":
            if enemy_Move == "defend":
                print ("You attack but the enemy defends. You both take no damage.")
            else:
                enemy_HP -= damage
                print (f"You attack and the enemy {enemy_Move}. The enemy takes {damage} damage.")
                
        elif player_Move == "defend":
            print (f"You defend and the enemy {enemy_Move}. You both take no damage.")
        
        elif player_Move == "heal":
            if charges["heal"] == 0:
                print ("You are out of healing charges.")
                continue
            if enemy_Move == "attack":
                player_HP = min(player_HP + heal, player_Max_HP)
                print (f"You heal {heal} damage.")
                charges["heal"] -= 1
            elif enemy_Move == "counter magic":
                enemy_HP += heal
                print (f"You heal and the enemy counters magic. The enemy heals {heal} damage.")
                charges["heal"] -= 1
            else:
                player_HP = min(player_HP + heal, player_Max_HP)
                print (f"You heal and the enemy defends. You heal {heal} damage.")
                charges["heal"] -= 1
        
        elif player_Move == "fireball":
            if charges["fireball"] == 0:
                print ("You are out of fireball charges.")
                continue
            if enemy_Move == "counter magic":
                print ("You fireball but the enemy counters magic. The enemy takes no damage.")
                charges["fireball"] -= 1
            else:
                enemy_HP -= damage*2
                print (f"You fireball and {enemy_Move}. The enemy takes {damage} damage.")
                charges["fireball"] -= 1
        
        #Enemy actions
        
        if enemy_Move == "attack" and player_Move != "defend":
            player_HP -= enemy_Damage
            print (f"The enemy attacks. You take {enemy_Damage} damage.")  
        
    if player_HP > 0:
        print (f"\nFOE VANQUISHED.")
        levelUp()
        
        if random.random() <= 0.5:
            charges["heal"] += 1
            print (f"You gain 1 healing charge from killing the foe.")
        if random.random() <= 0.3:
            charges["fireball"] += 1
            print  (f"You gain 1 fireball charge from killing the foe.")
        if random.random() <= 0.2:
            player_HP = min(player_HP + 5, player_Max_HP)
            print (f"You gain 5 HP from eating the desecrated corpse.")
    else:
        print (f"\nYOU HAVE DIED.")
        break     
