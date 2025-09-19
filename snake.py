"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def snake_color ():
    """Change snake color."""
    case = randrange(5)
    if case == 0:
        return 'green'
    elif case == 1:
        return 'deep pink'
    elif case == 2:
        return 'cyan'
    elif case == 3:
        return 'yellow'
    elif case == 4:
        return 'black'

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food on a random direction step by step. Inside the boundaries."""
    direction = randrange(4)

    if direction == 0:
        step = vector(10, 0)
    elif direction == 1:
        step = vector(-10, 0)
    elif direction == 2:
        step = vector(0, 10)
    else:
        step = vector(0, -10)

    newPosition = food.copy()
    newPosition.move(step)

    if inside(newPosition):
        food.move(step)



def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
    
    move_food() #We add the function here to move the food step by step

    clear()

    for body in snake:
        square(body.x, body.y, 9, snake_color())

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
