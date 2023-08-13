import pygame
import random

# Initialize Pygame
pygame.init()

input ("Welcome to the game! press enter to start")  # Print a welcome message at the beginning
# Set the dimensions of the screen (adjust as needed)
screen_width = 650
screen_height = 650
cell_size = 50
grid_size = 13

# Set colors (you can customize these)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Define the game board as a 2D array
game_board = [[None for _ in range(grid_size)] for _ in range(grid_size)]

# Player and enemy attributes
player = {
    "type": "player",
    "level": 1,
    "xp": 0,
    "class": "none",
    "maxHP": 100,
    "currentHP": 100,
    "attackPoints": 20,
    "armorRating": 17,
    "attackSkillModifier": 3,
    "abilities": ["movement", "sword"],
    "status": "none",
    "totalActions": 5,
    "actionsLeft": 5,
    "position": "forward",
    "row": (grid_size - 1),
    "col": (grid_size // 2)
}


enemy = {
    "type": "enemy",
    "level": 1,
    "xp": 0,
    "class": "wolf",
    "maxHP": 50,
    "currentHP": 50,
    "attackPoints": 15,
    "armorRating": 5,
    "attackSkillModifier": 2,
    "totalActions": 4,
    "actionsLeft": 4,
    "abilities": ["movement", "bite"],
    "status": "none",
    "position": ["forward"],
    "row": random.randint(0, grid_size - 1),
    "col": random.randint(0, grid_size - 1)
}


# Function to draw the game board
def draw_board():
    for row in range(0,grid_size):
        for col in range(0,grid_size):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = GRAY
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
    pygame.display.flip()

draw_board()

# Set the player's initial position at the bottom row middle column
player_row_start = int(player["row"])
player_col_start = int(player["col"])
game_board[player_row_start][player_col_start] = player


# Place the enemy on the game board
enemy_row_start = int(enemy["row"])
enemy_col_start = int(enemy["col"])
game_board[enemy_row_start][enemy_col_start] = enemy
# Function to draw units on the board

def draw_units():
    for row in range(grid_size):
        for col in range(grid_size):
            unit = game_board[row][col]
            if unit is player:
                pygame.draw.circle(screen, BLUE, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2)
                
            elif unit is enemy:
                pygame.draw.circle(screen, RED, (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), cell_size // 2)
               
draw_units()    
#player movement function
def player_open_cell(row,col): #fix this
      # Check if the destination cell is empty (not occupied by an enemy or object)
     if game_board[row][col] is None:
          return True
     else:
          return False
     
def move_player(row,col):
        player = None
        game_board[row][col] is player
        player["row"], player["col"] = row, col
        return

           

def player_position(): # fix make variable to change output and then fix player range
    player_position_row = int(player["row"])
    player_position_col = int(player["col"])
    global player_attack_position_col
    global player_attack_position_row
    if player["position"] == "forward":
        #forward graphic
        player_attack_position_col = range(player_position_col,player_position_col)
        player_attack_position_row = range(player_position_row)
    elif player["position"] == "back":
        #back graphic
        player_attack_position_col = range(player_position_col,player_position_col)
        player_attack_position_row = range(player_position_row, grid_size)  # Reverse range for rows
    elif player["position"] == "left":
        #left graphic
        player_attack_position_col = range(player_position_col)  # Reverse range for columns
        player_attack_position_row = range(player_position_row, player_position_row)
    elif player["position"] == "right":
        #right graphic
        player_attack_position_col = range(player_position_col, grid_size)
        player_attack_position_row = range(player_position_row, player_position_row)

    return player_attack_position_col, player_attack_position_row

def in_player_range(reach): 
    player_attack_position_col, player_attack_position_row = player_position()
    for row in player_attack_position_row:
        for col in player_attack_position_col:
            if 0 <= row < len(game_board) and 0 <= col < len(game_board[0]):
                if game_board[row][col] is enemy:
                    distance = abs(player["row"] - row) + abs(player["col"] - col)
                    
                    if distance <= reach:
                        return True  # Enemy is within reach
    return False  # No enemy in reach

def perform_player_action():
        actions_left = player["actionsLeft"]
        player_row = int(player["row"])
        player_col = int(player["col"])
        while actions_left > 0:
            print ("Actions left: ", player["actionsLeft"])
            goPos = input ("enter position  ")
            
                    
            if goPos == "w":
                    player["position"]= "forward"
                    
            elif goPos == "a":
                    player["position"]= "left"
                             
            elif goPos == "s":
                    player["position"]= "back"
                  
            elif goPos == "d":
                    player["position"]= "right"
           
            player_position()
            pygame.display.flip()             
            print ("facing " + player["position"])

            player_action = input ("next action?  ")

            if player_action == "w" and player_row > 0:
                    if player_open_cell(player_row - 1, player_col):
                        move_player(player_row - 1, player_col)
                        player["actionsLeft"] -= 1
                        
                    else:
                        print("Cannot move there. The cell is occupied.")

            elif player_action == "s" and player_row < grid_size - 1:
                    if player_open_cell(player_row +1, player_col):
                        move_player(player_row + 1, player_col)
                        player["actionsLeft"] -= 1
                        
                    else:
                        print("Cannot move there. The cell is occupied.")

            elif player_action == "a" and player_col > 0:
                    if player_open_cell(player_row, player_col - 1):
                        move_player(player_row, player_col - 1)
                        player["actionsLeft"] -= 1
                        
                    else:
                        print("Cannot move there. The cell is occupied.")  
                          
            elif player_action == "d" and player_col < grid_size - 1:
                    if player_open_cell(player_row, player_col + 1):
                        move_player(player_row, player_col + 1)
                        player["actionsLeft"] -= 1
                        
                    else:
                        print("Cannot move there. The cell is occupied.")
                    
            elif player_action == "quit":
                pygame.quit() 
                quit()

            elif player_action == "abilities":
                 print (player["abilities"])
                 
            elif player_action == "1":
                    
                    if in_player_range(1) is True:
                        calculate_attack_damage(player, enemy)
                        player["actionsLeft"] -= 1

                        
                    else: 
                        print ("missed, cant kill air")
                        player["actionsLeft"] -= 1

            elif player_action == "2" and "bow" in player["abilities"]:
                    
                    if in_player_range(grid_size) is True:
                        calculate_attack_damage(player, enemy)
                        player["actionsLeft"] -= 1
                        
                    else: 
                        print ("missed, cant kill air")
                        player["actionsLeft"] -= 1
        
                              
                    
        if actions_left == 0:
             print("no actions left ")   
             pygame.display.flip()
             input("press enter to end turn ") 
             player["actionsLeft"]=player["totalActions"]
             
        pygame.display.flip()
     #add a custom function matrix based on object class and level that makes mini animations updates waits half a second updates again and then returns to og position          
   


def calculate_attack_damage(attacker, target):
    attack_roll = random.randint(1, 20)  # Rolling a d20 for luck (truly random)
    attack_total = attack_roll + attacker["attackSkillModifier"]
    defense_total = target["armorRating"]

    if attack_total >= defense_total and attacker:
        # The attack hits
        damage = max(attacker["attackPoints"] - target["armorRating"], 0)
        target["currentHP"] -= damage
        print(f"{attacker['type']} dealt {damage} damage to {target['type']}.")
        pygame.display.flip() 
    else:
        # The attack misses
        print(f"{attacker['class']}'s attack missed {target['type']}.")

    if target["currentHP"] <= 0:
        print(f"{target['type']} was defeated.")
        game_board[target['row']][target['col']] = None
        target["status"] == "dead"
        pygame.display.flip() 
    return
# Function to print user-friendly prompts in the terminal
def print_prompt(message):
    print(f"\n>>> {message}")
 


    # Function to handle enemy's turn
def handle_enemy_turn():
    actions_left = enemy["actionsLeft"]
    enemy_row = int(enemy["row"])
    enemy_col = int(enemy["col"])
    while actions_left > 0:
        # Implement enemy's AI logic here (e.g., move towards the player, attack, etc.)
        move_enemy(enemy_row + random(-1,1), enemy_col + random(-1.1))
        enemy["actionsLeft"] -= 1
    if actions_left == 0:
        print ("enemy turn finished")
        enemy["actionsLeft"]=enemy["totalActions"]
        return

def move_enemy(erow,ecol):
    # Check if the destination cell is empty (not occupied by an enemy or object)
    enemy_row = int(enemy["row"])
    enemy_col = int(enemy["col"])
    if game_board[erow][ecol] is None and 0 < erow < grid_size and 0 < ecol < grid_size and game_board[erow][ecol] != game_board[player["row"]][player["col"]]:
        game_board[enemy_row][enemy_col] = None
        game_board[erow][ecol] is enemy
        enemy["row"], enemy["col"] = erow, ecol
        pygame.display.flip()
    if game_board[erow][ecol] == game_board[player["row"]][player["col"]]:
       calculate_attack_damage(enemy,player)
       pygame.display.flip() 
    else:
         return  

def enemies_on_board():
    for row in range(grid_size):
        for col in range(grid_size):
            if game_board[row][col] is not None and game_board[row][col] is enemy and enemy["status"] != "dead":
                return True
            
    return False


# Main loop
def main_loop():
    while enemies_on_board():
        if player["status"] == "dead":
            print("you're dead x_x")
            print("goodbye")
            return
        else: 
            perform_player_action()
            handle_enemy_turn()
            pygame.display.flip() 
       
        
    #once all eneimes are defeated
    if not enemies_on_board():
        print("Congratulations! You defeated all enemies.")
        input("exit press enter")
               

pygame.display.flip() 
main_loop()
    




#Quit Pygame
pygame.quit()