import pgzrun
import random
WIDTH=700
HEIGHT=400
fruits=["bagimg","batteryimg","bottleimg","chipsimg","paperimg"]
level=1
players=[]
animations = []
game_over = False
game_complete = False
Final_level = len(fruits)

def display_message(heading, subheading):
    screen.draw.text(heading,center = (WIDTH//2,HEIGHT//2), fontsize = 60)
    screen.draw.text(subheading,center = (WIDTH//2,HEIGHT//2 + 30), fontsize = 30)


def draw():
    screen.fill("sky blue")
    if game_over:
        display_message("You Lost","Try again!!")
    elif game_complete:
        display_message("You won","Well done")
    else:
        for fruit in players:
            fruit.draw()

def handle_gameover():
    global game_over
    game_over = True

def update():
    global players, level
    if len(players) == 0:
        make_players() 
        for fruit in players:
            duration = 10
            fruit.anchor=("center","bottom")
            animation = animate(fruit, duration = duration, y = HEIGHT,on_finished = handle_gameover)
            animations.append(animation)

def make_players():
    global players,fruits,level
    for i in range(level):
        option=random.choice(fruits)
        gap = WIDTH/(level + 1)
        fruit=Actor(option)
        fruit.x=(i + 1)*gap
        players.append(fruit)

def on_mouse_down(pos):
    global players, level, Final_level, animations
    for fruit in players:
        if fruit.collidepoint(pos):
            players.remove(fruit)
            if level == Final_level:
                game_complete = True
            else:
                if not players:
                    level +=1
                    players= []
                    animations=[]



pgzrun.go()
