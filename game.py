
import turtle
import math
from time import *
from timeit import default_timer as timer
import time



wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Game")
wn.setup(700, 700)
wn.tracer(0)
wn.bgpic("./image/giphy.gif")


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("./image/block.gif")
        self.shape("./image/block.gif")
        self.color("white")
        self.penup()
        self.speed(3)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("./image/zombie.gif")
        self.shape("./image/zombie.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a ** 2) + (b ** 2))

        if distance < 5:
            return True
        else:
            return False


class Treasure(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        v = self.getscreen()
        v.register_shape("./image/treasure.gif")
        self.shape("./image/treasure.gif")
        self.color("gold")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x, y)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()




level = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP XXXXXXX            XXXXX",
    "X  XXXXXXX   XXXXXX   XXXXX",
    "X       XX   XXXXXX   XXXXX",
    "XT      XX   XXX         XX",
    "XXXXXX  XX   XXX         XX",
    "XXXXXX  XX   XXXXXX    XXXX",
    "XXXXXX  XX      XXX    XXXX",
    "X  XXX          XXT    XXXX",
    "X  XXX   XXXXXXXXXXXXXXXXXX",
    "X           XXXXXXXXXXXXXXX",
    "XT                   XXXXXX",
    "XXXXXXXXXXXXX     XXXXX   X",
    "XXXXXXXXXXXXXXXX  XXXXX   X",
    "XXX    XXXXXXXXX          X",
    "XXX                       X",
    "XXX              TXXXXXXXXX",
    "XXXXXXXXXXXXX   XXXXXXXXXXX",
    "XXXXXXXXXXXXX             X",
    "XX   XXXXXT               X",
    "XX    XXXXXXXXXXXX    XXXXX",
    "XX     YXXXXXXXXXX    XXXXX",
    "XX           XXX          X",
    "XX                        X",
    "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
]

treasures = []

level.append(level_1)


def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            elif character == "P":
                player.goto(screen_x, screen_y)
            elif character == "T":
                treasures.append(Treasure(screen_x, screen_y))


def Starttime():
    treasure.destroy()
    treasures.remove(treasure)
    wn.update()

    start_timer = time()

    struct = localtime(start_timer)

    turtle.onscreenclick(None)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(10, 300)
    turtle.color("red")
    turtle.clear()


pen = Pen()
player = Player()

walls = []

setup_maze(level[1])

turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")

Gold_left = 6
wn.tracer(0)

def check_Time(start, end):
    print(f'Start = {start}')
    print(f'End = {end}')

end=0
start = 0
temp = 0
no_golds = 0
flag = True
while (flag == True):
    for treasure in treasures:
        my_start = time.time()
        if player.is_collision(treasure):
            player.gold += treasure.gold
            Gold_left = Gold_left - 1
            no_golds = Gold_left
            if player.gold == 100:
                print("hi")
                end = time.time()
                temp = end
                turtle.goto(10, 300)
                turtle.color("blue")
                pass
            else:
                start = time.time()
                print("Begin")
                turtle.clear()
                turtle.goto(150, 300)
                turtle.write("Player Score:{}".format(player.gold), align="right", font=(0.0000001))
                turtle.goto(2000, 2000)
                treasure.destroy()
                wn.update()


        wn.update()
        start = time.time()
        print(f'start:{start}')
        print(start - temp)
        print(f"NO of golds...........{no_golds}")
        print(f"NO of player.gold...........{player.gold}")


        if(start - end < 9999999):
            turtle.speed(0)
            turtle.penup()
            turtle.goto(-180,310)
            turtle.color("blue")
            my_time = ('%.2f' % float(start-end))
            print(f'My test value ........{my_time}')
            y = round(int(start -end),2)
            turtle.write(f'Timer : {my_time}', align="right", font=(20))
            turtle.clear()

            if(y>14):
                if(player.gold<400):
                    turtle.goto(10, 300)
                    turtle.color("red")
                    turtle.write("You Have Lost", align="left", font=(20))
                    time.sleep(2)
                    flag = False
            if (y<=60):
                if(player.gold==600):
                    turtle.goto(10, 300)
                    turtle.color("red")
                    turtle.write("You Have Won !!!!!!", align="left", font=(20))
                    time.sleep(2)
                    flag = False

       


