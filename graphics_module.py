import pygame


#Used for all graphics except the main character for right now
#main character doesn't change as of right now I will incoorporate later
# what will go here is the HUD of abilities and health etc
# a function for determining enemy imagry
#

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load custom font (place your font file in the same directory)
pygame.font.init()
custom_font = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\WELLSLEY.TTF", 28)  # Replace with your font file
InfobarO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\player_infobar.png")
def draw_player_info(screen, name, level, currenthp, maxhp, attk, ar, acc, status): #add abilities later
    size = (screen.get_width(),125)   #screen.get_width())    
    location = (0,screen.get_height()-125)
    Infobar =  pygame.transform.smoothscale(InfobarO,size)
    screen.blit(Infobar, location)


    player_name_lvl_life = custom_font.render(f"Player: {name} lvl: {level}  Health: {currenthp} / {maxhp}"  , True, WHITE)
    screen.blit(player_name_lvl_life, (100, screen.get_height() - 110))
    pygame.display.flip()
    player_fight_stats1 = custom_font.render(f"Attack: {attk} Armor Rating: {ar}"  , True, WHITE)
    screen.blit(player_fight_stats1, (175, screen.get_height() - 85))
    pygame.display.flip()
    player_fight_stats2 = custom_font.render(f"Accuracy: {acc} status: {status}"  , True, WHITE)
    screen.blit(player_fight_stats2, (175, screen.get_height() - 60))
    pygame.display.flip()
    

   

   
    # Draw other player information text here

    

