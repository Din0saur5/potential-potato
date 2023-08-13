import pygame
import random
import graphics_module
import sys
import time
# Set colors (you can customize these)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class PygameStream:
    def __init__(self, max_lines=2):
        self.max_lines = max_lines
        self.lines = []

    def write(self, text):
        self.lines.append(str(text))
        if len(self.lines) > self.max_lines:
            self.lines.pop(0)

    def flush(self):
        pass

    def get_last_line(self):
        if self.lines:
            return self.lines
        return ""

# Initialize Pygame
pygame.init()
print("Welcome to the game! what is your character name?")
characterName = input ()  # Print a welcome message at the beginning
# Set the dimensions of the screen (adjust as needed)
screen_width = 650
screen_height = 800
cell_size = 50
grid_size = 13


# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))




# Define the game board as a 2D array
game_board = [[None for _ in range(grid_size+1)] for _ in range(grid_size+1)]
terminal_font = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\PR Viking.ttf", 14)
fpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_forward.png")
bpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_back.png")
rpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_right.png")
lpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_left.png")
player_graphic =[fpimage,bpimage,rpimage,lpimage]

#abilities dictionary

abilities = []
class Ability:
    def __init__(self, name, reach, type, damage, graphic, splash):
        self.name = name
        self.reach = reach
        self.damage = damage
        self.type = type
        self.graphic = graphic
        self.splash = splash
    
def ability_effect(ability, user, target):
        if ability.name == "sword" or \
            ability.name == "bow" or \
            ability.name == "fireball" or \
            ability.name == "piercing shot" or \
            ability.name == "lightning bolt" or \
            ability.name == "bite":
                calculate_attack_damage(ability, user, target)
        elif ability.name == "teleport":
                i = 0
                for i in range(5):
                    row = random.randint(0, grid_size - 2)
                    col = random.randint(0, grid_size - 1)
                    if open_cell(row,col):
                        game_board[user.row][user.col] = None
                        game_board[row][col] = user
                        break
                    else:
                        i +=1
                        print("something when wrong let me try again")
        elif ability.name == "drain":
                calculate_attack_damage(ability,user,target)
                user.current_hp +=7
        elif ability.name == "fear":
                target.status == "scared"
        else:
                 print("not an ability")    
             

sword = Ability("sword",1,"plain",10,"graphic",False)
abilities.append(sword)  
bite = Ability("bite",1,"plain",10,"graphic",False)
abilities.append(bite)     
teleport = Ability("teleport",0,0,"none","graphic",False)
abilities.append(teleport)         
bow = Ability("bow",grid_size,"plain",7,"graphic",False)
abilities.append(bow)
fireball = Ability("fireball",grid_size,"fire",7,"graphic",False)
abilities.append(fireball)
piercing_shot = Ability("piercing shot", grid_size, "plain", 12, "graphic",True)
abilities.append(piercing_shot)
lightning_bolt = Ability("lightning bolt", grid_size, "lightning", 12, "graphic",True)
abilities.append(lightning_bolt)
drain = Ability("drain", 4,"necrotic",12,"graphic",False)
abilities.append(drain)
fear = Ability("fear", 2, "pychic", 0, "graphic", False)
abilities.append(fear)
#enemy dictionary
wolf_dict = {
    "name": "wolf",
    "level": 1,
    "found": "forest",
    "resistance": "none",
    "weakness": "none",
    "max_hp": 50,
    "attack_points": 15,
    "armor_rating": 5,
    "attack_skill_modifier": 2,
    "total_actions": 4,
    "abilities": ["movement", "bite"]
    
}


enemies = []
class Enemy:
    def __init__(self, name, level, found, resistance, weakness, max_hp, attack_points, armor_rating, attack_skill_modifier, total_actions, abilities):
        self.name = name
        self.level = level
        self.found = [found]
        self.resistance = resistance
        self.weakness = weakness
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_points = attack_points
        self.armor_rating = armor_rating
        self.attack_skill_modifier = attack_skill_modifier
        self.abilities = abilities
        self.status = "none"
        self.disabled = None
        self.position = "back"
        self.row = random.randint(0, grid_size - 2)
        self.col = random.randint(0, grid_size - 1)
        self.total_actions = total_actions
        self.actions_left = total_actions


# Create instances of Enemy class for different enemies
wolf = Enemy(**wolf_dict)
vampire = Enemy("Vampire", 2,"dungeon","necrotic",["radiant","fire"], 70, 20, 17, 3, 4, ["movement", "drain"])
ghost = Enemy("Ghost", 3, ["graveyard","dungeon"],["necrotic","psychic"], ["radiant","fire"], 30, 10, 13, 1, 6, ["movement", "fear"])
#create randomizer spawn  
for _ in range(3):
    enemy_instance = Enemy(**wolf_dict)
    enemies.append(enemy_instance)


# Player and enemy attributes
class Player:
    def __init__(self,characterName):

        self.name =characterName
        self.level = 1
        self.max_hp = 100
        self.current_hp = 100
        self.attack_points = 20
        self.armor_rating = 17
        self.attack_skill_modifier = 3
        self.abilities = ["movement","sword"]
        self.status = "none"
        self.disabled = ["none"]
        self.total_actions = 5
        self.actions_left = 5
        self.position = "forward"
        self.graphic = player_graphic
        self.row = grid_size - 1
        self.col = grid_size // 2
player = Player(characterName)




pygame_stream = PygameStream()
sys.stdout =  pygame_stream

# Function to draw the game board
def draw_board(player):
    
    for row in range(0,grid_size):
        for col in range(0,grid_size):
            if (row + col) % 2 == 0:
                color = WHITE
            else:
                color = GRAY
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
    level = str(player.level) 
    current_hp = str(player.current_hp) 
    max_hp = str(player.max_hp) 
    attack_points = str(player.attack_points) 
    armor_rating = str(player.armor_rating) 
    attack_skill_modifier = str(player.attack_skill_modifier)
    graphics_module.draw_player_info(
    screen, 
    player.name, 
    level, 
    current_hp, 
    max_hp, 
    attack_points, 
    armor_rating, 
    attack_skill_modifier, 
    player.status
    )
  
    







# Function to draw units on the board
def draw_units():

    
    for row in range(grid_size):
        for col in range(grid_size):
            unit = game_board[row][col]
            image_size = (cell_size,cell_size)
            image_reset = (0,0)
            if unit is player:   #front back right left
                location = (col*50,row*50)
                if player.position == "back":
                    fpimageS = pygame.transform.scale(player_graphic[0],image_reset)
                    rpimageS = pygame.transform.scale(player_graphic[2],image_reset)
                    lpimageS = pygame.transform.scale(player_graphic[3],image_reset)
                    bpimageS = pygame.transform.scale(player_graphic[1],image_size)
                    screen.blit(bpimageS, location) 
                    pygame.display.flip()
                elif player.position == "forward":
                    bpimageS = pygame.transform.scale(bpimage,image_reset)
                    rpimageS = pygame.transform.scale(rpimage,image_reset)
                    lpimageS = pygame.transform.scale(lpimage,image_reset)
                    fpimageS = pygame.transform.scale(fpimage,image_size)
                    screen.blit(fpimageS, location)
                    pygame.display.flip()
                elif player.position == "left":
                    fpimageS = pygame.transform.scale(fpimage,image_reset)
                    rpimageS = pygame.transform.scale(rpimage,image_reset)
                    bpimageS = pygame.transform.scale(bpimage,image_reset)
                    lpimageS = pygame.transform.scale(lpimage,image_size)
                    screen.blit(lpimageS, location)
                    pygame.display.flip()
                elif player.position == "right":
                    # Draw triangle for player
                    fpimageS = pygame.transform.scale(fpimage,image_reset)
                    bpimageS = pygame.transform.scale(bpimage,image_reset)
                    lpimageS = pygame.transform.scale(lpimage,image_reset)
                    rpimageS = pygame.transform.scale(rpimage,image_size)
                    screen.blit(rpimageS, location)
                    pygame.display.flip()
            elif unit in enemies:
                if unit.position == "forward":
                        triangle_vertices = [
                            (col * cell_size + cell_size // 2, row * cell_size),           # Top vertex
                            (col * cell_size, row * cell_size + cell_size),                 # Bottom-left vertex
                            (col * cell_size + cell_size, row * cell_size + cell_size),     # Bottom-right vertex
                            ]
                        pygame.draw.polygon(screen, RED, triangle_vertices)
                        pygame.display.flip()
                elif unit.position == "back":
                    
                        triangle_vertices = [
                            (col * cell_size + cell_size // 2, row * cell_size),           # Top vertex
                            (col * cell_size, row * cell_size + cell_size),                 # Bottom-left vertex
                            (col * cell_size + cell_size, row * cell_size + cell_size),     # Bottom-right vertex
                            ]
                        pygame.draw.polygon(screen, RED, triangle_vertices)
                        pygame.display.flip()
                elif unit.position == "left":
                        triangle_vertices = [
                            (col * cell_size + cell_size // 2, row * cell_size),           # Top vertex
                            (col * cell_size, row * cell_size + cell_size),                 # Bottom-left vertex
                            (col * cell_size + cell_size, row * cell_size + cell_size),     # Bottom-right vertex
                            ]
                        pygame.draw.polygon(screen, RED, triangle_vertices)
                        pygame.display.flip()
                elif unit.position == "right":
                    # Draw triangle for player
                        triangle_vertices = [
                            (col * cell_size + cell_size // 2, row * cell_size),           # Top vertex
                            (col * cell_size, row * cell_size + cell_size),                 # Bottom-left vertex
                            (col * cell_size + cell_size, row * cell_size + cell_size),     # Bottom-right vertex
                            ]
                        pygame.draw.polygon(screen, RED, triangle_vertices)
                        pygame.display.flip()
    
    terminal_text = terminal_font.render(str(pygame_stream.get_last_line()), True, WHITE)
    clear_term_loc = (0,650,400,25)
    clear_term = pygame.draw.rect(screen,BLACK,clear_term_loc)
    pygame.display.update(clear_term)
    screen.blit(terminal_text, (10, 650))
    pygame.display.flip()


def handle_events():
    if player.status != "none":
        print(player.status)
       
    for player.actions_left in range(player.total_actions):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                handle_key_event(event.key)
                pygame.display.flip()
        
    
def handle_key_event(key):
        
    if key == pygame.K_UP:
            move_direction(player, "forward")
    elif key == pygame.K_LEFT:
            move_direction(player, "left")
    elif key == pygame.K_DOWN:
            move_direction(player, "back")
    elif key == pygame.K_RIGHT:
            move_direction(player, "right")
    elif key == pygame.K_w:
            player.position = "forward"
            draw_board(player)
            draw_units()
            pygame.display.flip()
    elif key == pygame.K_a:
            player.position = "left"
            draw_board(player)
            draw_units()
            pygame.display.flip()
    elif key == pygame.K_s:
            player.position = "back"
            draw_board(player)
            draw_units()
            pygame.display.flip()
    elif key == pygame.K_d:
            player.position = "right"
            draw_board(player)
            draw_units()
            pygame.display.flip()
    elif key == pygame.K_1:
            use_ability(player, player.abilities[1])
    elif key == pygame.K_2:
            use_ability(player, player.abilities[2])
    elif key == pygame.K_3:
            use_ability(player, player.abilities[3])
    elif key == pygame.K_4:
            use_ability(player, player.abilities[4])    
    elif key == pygame.K_5:
            use_ability(player, player.abilities[5])
    elif key == pygame.K_6:
            use_ability(player, player.abilities[6])
    elif key == pygame.K_7:
            use_ability(player, player.abilities[7])
    elif key == pygame.K_8:
            use_ability(player, player.abilities[8])
    elif key == pygame.K_9:
            use_ability(player, player.abilities[9])                        
    elif key == pygame.K_q:
            print(player.abilities)
    elif key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
    draw_board(player)
    draw_units()
    pygame.display.flip()

def check_status(entity):
    if entity.status == "none":
        return
    if entity.status == "scared":
        rangeA = range(1, len(entity.abilities)) 
        for indexA in rangeA:
            ability_name = entity.abilities[indexA]
            entity.disabled.append(ability_name)

    
#movement function
def open_cell(row,col): 
      # Check if the destination cell is empty (not occupied by an enemy or object)
     if game_board[row][col] is None and row in range(grid_size) and col in range(grid_size): 
          return True
     else:
          return False
     
def move_direction(entity, direction):
    row = entity.row
    col = entity.col
    if "movement" in entity.abilities:
        if direction == "forward":
            if open_cell(row - 1, col):
                
                game_board[row][col] = None
                entity.row -= 1
                game_board[entity.row][entity.col] = entity
                entity.actions_left -= 1 
                        
            else:
                print("Cannot move there.")    
        elif direction == "left":
            if open_cell(row, col- 1):
                
                game_board[row][col] = None
                entity.col -= 1
                game_board[entity.row][entity.col] = entity
                entity.actions_left -= 1
                           
            else:
                print("Cannot move there.")
            
        elif direction == "back":
            if open_cell(row + 1, col):
                game_board[row][col] = None
                entity.row += 1
                game_board[entity.row][entity.col] = entity
                entity.actions_left -= 1
                
            else:
                print("Cannot move there.")
            
        elif direction == "right":
            if open_cell(row, col+1):
                game_board[row][col] = None
                entity.col += 1
                game_board[entity.row][entity.col] = entity
                entity.actions_left -= 1
                
                         
            else:
                print("Cannot move there.")
        draw_board(player)
        draw_units()
        pygame.display.flip()
    else:
         print(entity.name + " can't move")   


def in_range(attacker, ability): 
    enemies_in_range = []
    
    if attacker.position == "back":
        for row in range(attacker.row, attacker.row + ability.reach +1):
            target = game_board[row][attacker.col]
            if target is None:
                 continue
            elif target in enemies:
                 enemies_in_range.append(target)
                
            else:
                 continue
    elif attacker.position == "forward":
        for row in range(attacker.row - ability.reach, attacker.row):
            target = game_board[row][attacker.col]
            if target is None:
                 continue
            elif target in enemies:
                 enemies_in_range.append(target)   
            else:
                 continue
                    
    elif attacker.position == "right":
        for col in range(attacker.col, attacker.col + ability.reach +1):
            target = game_board[attacker.row][col]
            if target is None:
                 continue
            elif target in enemies:
                 enemies_in_range.append(target)     
            else:
                continue
    elif attacker.position == "left":
        for col in range(attacker.col - ability.reach, attacker.col):
            target = game_board[attacker.row][col]
            if target is None:
                 continue
            elif target in enemies:
                 enemies_in_range.append(target)
            else:
                 continue       
    if not enemies_in_range:
         return None
    else:    
        return enemies_in_range

def use_ability(user, ability_name):
    
    for ability in abilities:
        if ability.name == ability_name: 
            
            if ability.reach > 0:
                enemies_in_range = in_range(user, ability)
                if not in_range(user, ability):
                        print("No enemies in range")
                        return
                else:
                    user.actions_left -= 1
                    if ability.splash:
                        for target in enemies_in_range:
                            if ability_success(user, target):
                                print("Hit!")
                                ability_effect(ability, user, target)
                            else:
                                print("Miss!")    
                    else:
                            if ability_success(user, enemies_in_range[0]):
                                print("Hit!")
                                ability_effect(ability,user,enemies_in_range[0])            
                            else:
                                print("Miss!")
                
            elif ability.reach == 0:
                 ability_effect(ability,user,user)
       
            else:
                print("ability not unlocked")
      
    return 
        
def ability_success(attacker, target):
        attack_roll = random.randint(1, 20)  # Rolling a d20 for luck (truly random)
        attack_total = attack_roll + attacker.attack_skill_modifier
        defense_total = target.armor_rating
        if attack_total > defense_total:
             return True
        else:
             return False

def calculate_attack_damage(ability, attacker, target):
  
        # The attack hits
        if ability.type == target.weakness:
            damage = attacker.attack_points + (ability.damage *1.5) 
            target.current_hp -= damage
            print(f"{attacker.name} dealt {damage} damage to {target.name}. Seemed extremely effective!")
             
        elif ability.type == target.resistance:
            damage = attacker.attack_points + (ability.damage*0.5)
            target.current_hp -= damage
            print(f"{attacker.name} dealt {damage} damage to {target.name}. Seemed to have very little effect!")
            
        else:
            damage = (attacker.attack_points) + ability.damage
            target.current_hp -= damage
            print(f"{attacker.name} dealt {damage} damage to {target.name}.")
               
    
        if target.current_hp <= 0:
            print(f"{target.name} was defeated.")
            game_board[target.row][target.col] = None
            target.status == "dead"
            draw_board(player)
            draw_units()
            pygame.display.flip()
             
        return

# Function to print user-friendly prompts in the terminal
def print_prompt(message):
    print(f"\n>>> {message}")
 


    # Function to handle enemy's turn

#def handle_enemy_turn(enemies):
    for enemy in enemies:
        for enemy.actions_left in range(enemy.total_actions):

            if enemy.name == "wolf" and enemy.status != "dead":
                player_row, player_col = player.row, player.col
                enemy_row, enemy_col = enemy.row, enemy.col
            
                distance = abs(player_row - enemy_row) + abs(player_col - enemy_col)
            
            if distance ==  1 :
                if player_row < enemy_row:
                    enemy.positon = "back"
                elif player_row > enemy_row:
                    enemy.positon = "forward"
                if player_col < enemy_col:
                    enemy.positon = "left"
                elif player_col > enemy_col:
                    enemy.positon = "right"
                    
                enemy.actions_left -= 1                
                continue
            else:
                # Move towards the player
                if player_row < enemy_row:
                    if open_cell(enemy_row -1,enemy_col):
                        enemy_row -=1
                        enemy.actions_left -= 1
                        game_board[enemy.row][enemy.col] = None
                        enemy.row, enemy.col = enemy_row, enemy_col
                        game_board[enemy.row][enemy.col] = enemy
                        pygame.display.flip() 
                        continue
                elif player_row > enemy_row:
                    if open_cell(enemy_row+1,enemy_col):
                        enemy_row += 1
                        enemy.actions_left -= 1
                        game_board[enemy.row][enemy.col] = None
                        enemy.row, enemy.col = enemy_row, enemy_col
                        game_board[enemy.row][enemy.col] = enemy
                        pygame.display.flip() 
                        continue           
                elif player_col < enemy_col:
                    if open_cell(enemy_row,enemy_col-1):
                        enemy_col -= 1
                        enemy.actions_left -= 1
                        game_board[enemy.row][enemy.col] = None
                        enemy.row, enemy.col = enemy_row, enemy_col
                        game_board[enemy.row][enemy.col] = enemy
                        pygame.display.flip() 
                        continue
                elif player_col > enemy_col:
                    if open_cell(enemy_row,enemy_col-1):    
                        enemy_col += 1
                        enemy.actions_left -= 1
                        game_board[enemy.row][enemy.col] = None
                        enemy.row, enemy.col = enemy_row, enemy_col
                        game_board[enemy.row][enemy.col] = enemy
                        pygame.display.flip() 
                        continue
                                       
                else:
                    for i in range(100): 
                        enemy_row_oof = enemy_row + random.randomint( -1,1)
                        enemy_col_oof = enemy_col + random.randomint( -1,1)
                        if open_cell(enemy_row_oof ,enemy_col_oof):            
                            enemy_row = enemy_row_oof
                            enemy_col = enemy_row_oof
                            enemy.actionsleft =0
                            game_board[enemy.row][enemy.col] = None
                            enemy.row, enemy.col = enemy_row, enemy_col
                            game_board[enemy.row][enemy.col] = enemy
                            pygame.display.flip()                            
                            continue
                        else:
                            i+= 1
                

                    
                    

        if enemy.actions_left == 0:
            enemy.status = "none"
            enemy.disabled = None
            break


def enemies_on_board():
    pygame.display.flip()
    for row in range(grid_size):
        for col in range(grid_size):
            enemy = game_board[row][col]
            if enemy in enemies:
                return True
    
    return False        

    


# Main loop
def main_loop():
    running = True
    draw_board(player) 
    # Set the player's initial position at the bottom row middle column
    game_board[player.row][player.col] = player
    # Place the enemy on the game board
    for enemy in enemies:
        game_board[enemy.row][enemy.col] = enemy
    draw_units()
    

    while running:     
        
        if player.status == "dead":
            print("You're dead x_x")
            print("Goodbye")
            running = False
        else:
            check_status(player)
            handle_events() 
           
            #handle_enemy_turn(enemies)
                
            player.status = "none"
            player.disabled = None
            player.actions_left = player.total_actions # New function to handle events
            for enemy in enemies:
                enemy.status = "none"
                enemy.disabled = None
                enemy.actions_left = enemy.total_actions
                            
            running = True

            if not enemies_on_board():
                print("Congratulations! You defeated all enemies.")
                print("press esc to exit")
                running = False
        
        
    pygame.display.flip()
            
    pygame.display.flip() 


main_loop()
    




#Quit Pygame
pygame.quit()
sys.exit