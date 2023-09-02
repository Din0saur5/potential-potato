
"""
i make extensive notes before attempting to write a new part of the code:
my friends told me it would be a good idea to put notes into the code so its easier to follow. 
at some point I will go back through and add smaller notes accross the entirety of the code to lay out extactly whats going on.

heres the notes I wrote before programming this ai model (fun side note: my current job is a dog walker 
so I often type this out on my phone while walking dogs):

turns coutning down 
general:
x-0: movement or (if in range attacks/abilities)
if agg or def not in range get in range (always try to get in range)
if you get in range:
if def use attack once if actions left is 4 or less and twice if greater than 4 then begin evasive manuevers 
if agg attack until turn is over
 

enemy abilities:
1: movement
2: melee attack
3: evasive, defensive or healing
4: long range
5: mid range
6: special 
fighting style (list of weights for logic to choose attack) (add to class)
behavior    (either aggressive or defensive will add switch abilities and low health implications) (add to enemy class)
 I can have them switch from aggro to defensive or rev at a health percent

aggressive: explained above 
defensive: evasive maneuvers: 
Use ability 3 if under full health
Find closest obstacle (lowest hscore)
Check neighbors 
Choose furthest from player (highest h score) 
Create path to cell and go towards it
If cell is reached end turn
if no path attack until turn ends
melee:
  Use aggressive vs defensive
 follow path to player square if len(path) =1 then in-range
If in range 
Face player
If agg then agg
If def then def

long range:
(most in depth)
if not in range:
Make a list of the cells in range 
Make a class for paths with a self. Length
Find paths on all cells in range
Add to class with length
Add to list
Order by smallest .length value path = sorted(paths, key=lambda cell: int(cell.h_score()), reverse=True)
choose lowest length value
return path and append end cell.
follow path 
if cell is reached then in range
face player
agg and def begins here 

if starting in melee range of player:
do the same as if not in range just instead of choosing lowest length value choose the path that has 4 steps 
if one doesnt exist try 3 steps 2 steps else just attack

mid range:
same as long range just with 3 squares
take out the 4 steps and change it to 3 steps

special:
gets in range using in-range algorithm based on reach
use special
for remaining actions use preferred 


functions to make:
tactics function (enemy) -> random weighted choice based on assigned tactics
in range algorithm (pathfinder, player(target), enemy, )
behavior algorithm(actions left, gameboard, enemy, pathfinder, enemy)

items to add to enemy class: preferred_tactic, tactics, behavior, 

"""
import pygame
import pathfinder_module
import random


def tactics(tactics):
    #chooses what kind of movet the entity will make
    tactics_choices = ["melee", "long range", "midrange", "special"]
    tactic = random.choices(tactics_choices,tactics)
    return tactic
def in_range_path(tactic):
    # determines best end cell in attack range for tactic and sets path to that cell
    #melee, since the player cell is in the path we first have to remove the last entry
    path.pop
    return move_path

def behavior(end_cell):
    # when that end cell is reached from 

def enemy_brain():
    current_tactic = tactics()
    in_range_path(current_tactic)