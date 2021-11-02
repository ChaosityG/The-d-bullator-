from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt

print('''Voici les règles:
Tu as 30 sec. dans le minuteur, si le temps est fini, c'est Game Over.
1 Bulle = 32 à 36 points
À chaque 1250 points, tu as 30 sec. de plus.

Commandes:

W: Haut
A: Gauche
S: Bas
D: Droite
Arrow up: Haut
Arrow left: Gauche
Arrow down: Bas
Arrow right: Droite

C'est tout! Maintenant tu peux jouer!

ATTENTION!: Plus le 'display' est grand, plus le jeu mange de ressources.
ATTENTION!: Plus la résolution du 'display' est grande, plus le jeu mange de ressources.''', '\n')
sleep(15)

mode = input('''Quel mode veux-tu ?,
Tape 1 pour le mode: Facile : Celui qui consomme le plus de ressources.
Tape 2 pour le mode: Normal : Conseillé pour les débutant.
Tape 3 pour le mode: Difficile: Celui qui consomme le moins de ressources, Pour se donner un défi, le mode difficile est pour vous!.''')
print('\n')

scr = Tk()
width_scr = scr.winfo_screenwidth()
height_scr = scr.winfo_screenheight()
scr.title("The débullator")
scr.iconbitmap("icon.ico")
c = Canvas(scr, height = height_scr, width = width_scr, bg = 'darkblue')
c.pack()


id_submarine_in = c.create_polygon(5, 5, 5, 25, 30, 15, fill='red')
id_submarine_out = c.create_oval(0, 0, 30, 30, outline='red')
id_submarine_avant = c.create_polygon(5, 5, 5, 5, 30, 15, outline='red')
id_submarine_avant2 = c.create_polygon(5, 5, 5, 5, 30, -7, outline='red')
r_submarine = 15
X_MID = width_scr / 2
Y_MID = height_scr / 2
c.move(id_submarine_in, X_MID, Y_MID)
c.move(id_submarine_out, X_MID, Y_MID)
c.move(id_submarine_avant, X_MID + 20, Y_MID)
c.move(id_submarine_avant2, X_MID + 20, Y_MID + 20)

speed_submarine = 10
def move_submarine(event):
    if event.keysym == 'Up':
        c.move(id_submarine_in, 0, -speed_submarine)
        c.move(id_submarine_out, 0, -speed_submarine)
        c.move(id_submarine_avant, 0, -speed_submarine)
        c.move(id_submarine_avant2, 0, -speed_submarine)
    elif event.keysym == 'Down':
        c.move(id_submarine_in, 0, speed_submarine)
        c.move(id_submarine_out, 0, speed_submarine)
        c.move(id_submarine_avant, 0, speed_submarine)
        c.move(id_submarine_avant2, 0, speed_submarine)
    elif event.keysym == 'Left':
        c.move(id_submarine_in, -speed_submarine, 0)
        c.move(id_submarine_out, -speed_submarine, 0)
        c.move(id_submarine_avant, -speed_submarine, 0)
        c.move(id_submarine_avant2, -speed_submarine, 0)
    elif event.keysym == 'Right':
        c.move(id_submarine_in, speed_submarine, 0)
        c.move(id_submarine_out, speed_submarine, 0)
        c.move(id_submarine_avant, speed_submarine, 0)
        c.move(id_submarine_avant2, speed_submarine, 0)
    elif event.keysym == 'w':
        c.move(id_submarine_in, 0, -speed_submarine)
        c.move(id_submarine_out, 0, -speed_submarine)
        c.move(id_submarine_avant, 0, -speed_submarine)
        c.move(id_submarine_avant2, 0, -speed_submarine)
    elif event.keysym == 's':
        c.move(id_submarine_in, 0, speed_submarine)
        c.move(id_submarine_out, 0, speed_submarine)
        c.move(id_submarine_avant, 0, speed_submarine)
        c.move(id_submarine_avant2, 0, speed_submarine)
    elif event.keysym == 'a':
        c.move(id_submarine_in, -speed_submarine, 0)
        c.move(id_submarine_out, -speed_submarine, 0)
        c.move(id_submarine_avant, -speed_submarine, 0)
        c.move(id_submarine_avant2, -speed_submarine, 0)
    elif event.keysym == 'd':
        c.move(id_submarine_in, speed_submarine, 0)
        c.move(id_submarine_out, speed_submarine, 0)
        c.move(id_submarine_avant, speed_submarine, 0)
        c.move(id_submarine_avant2, speed_submarine, 0)
        
c.bind_all('<Key>', move_submarine)

id_bubble = list()
r_bubble = list()
speed_bubble = list()
R_MIN_BUBBLE = 10
R_MAX_BUBBLE = 30
SPEED_BUBBLE_MAX = 10
GAP = 100

def create_bubble():
    x = width_scr + GAP
    y = randint(0, height_scr)
    r = randint(R_MIN_BUBBLE, R_MAX_BUBBLE)
    id_1 = c.create_oval(x - r, y - r, x + r, y + r, outline='white')
    id_bubble.append(id_1)
    r_bubble.append(r)
    speed_bubble.append(randint(1, SPEED_BUBBLE_MAX))

def move_bubble():
    for i in range(len(id_bubble)):
        c.move(id_bubble[i], -speed_bubble[i], 0)

def find_coords(num_id):
    pos = c.coords(num_id)
    x = (pos[0] + pos[2]) / 2
    y = (pos[1] + pos[3]) / 2
    return x, y

def delete_bubble(i):
    del r_bubble[i]
    del speed_bubble[i]
    c.delete(id_bubble[i])
    del id_bubble[i]

BUBBLE_COUNTER = 0

def erase_bubble():
    global BUBBLE_COUNTER
    for i in range(len(id_bubble)-1, -1, -1):
        x, y = find_coords(id_bubble[i])
        if x < -GAP:
            delete_bubble(i)
            BUBBLE_COUNTER -= 1

def distance(id_1, id_2):
    x1, y1 = find_coords(id_1)
    x2, y2 = find_coords(id_2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def collision():
    points = 0
    for bubble in range(len(id_bubble)-1, -1, -1):
        if distance(id_submarine_out, id_bubble[bubble]) < (r_submarine + r_bubble[bubble]):
            points += (r_bubble[bubble] + speed_bubble[bubble])
            delete_bubble(bubble)
    return points

c.create_text(100, 30, text='Time remaining', fill='white')
c.create_text(200, 30, text='Score', fill='white')
text_time = c.create_text(100, 50, fill='white')
text_score = c.create_text(200, 50, fill='white')
def show_score(score):
    c.itemconfig(text_score, text=str(score))
def show_time(time_remain):
    c.itemconfig(text_time, text=str(time_remain))

LUCK_BUBBLE = 3
BUBBLE_LIMIT = 250

if mode == "1":
    LUCK_BUBBLE = 1
    BUBBLE_LIMIT = 350
elif mode == "2":
    LUCK_BUBBLE = 3
    BUBBLE_LIMIT = 250
elif mode == "3":
    LUCK_BUBBLE = 4
    BUBBLE_LIMIT = 200


TIME_LIMIT = 30
SCORE_BONUS = 1250
score = 0
bonus = 0
endgame = time() + TIME_LIMIT 

# MAIN GAME LOOP 
while time() < endgame:
     if randint(1, LUCK_BUBBLE) == 1 and BUBBLE_COUNTER <= BUBBLE_LIMIT:
         create_bubble()
         BUBBLE_COUNTER += 1
     move_bubble()
     erase_bubble()
     score += collision()
     if (int(score/SCORE_BONUS)) > bonus:
         bonus += 1
         endgame += TIME_LIMIT
     show_score(score)
     show_time(int(endgame - time()))
     scr.update()

c.create_text(X_MID, Y_MID - 100, text='GAME OVER', fill='white', font=('Helvetica', 30))
c.create_text(X_MID, Y_MID - 70, text='Score : ' + str(score), fill='white')
c.create_text(X_MID, Y_MID - 50, text='Bonus time : ' + str(bonus*TIME_LIMIT), fill='white') 

btn_cls = Button(scr, text = "Close", command = scr.destroy, font = ('Helvetica', 10), bg='white')
btn_cls.place(x = X_MID - 21, y = Y_MID - 35)
# Every bubble costs from 32 to 36 points.
