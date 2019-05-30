import turtle

turtle.setup(340,340,340,340)
t = turtle.Pen()
t.speed(0)
t.hideturtle()


def angle(x, y):
    angle_half(x, y, 'left')
    angle_half(x, y, 'right')


def angle_half(x, y, direction):
    if direction == 'left':
        t.setheading(0)
        draw_lines(x + 3, y + 3, 5)
        draw_lines(x + 3, y - 3, 5)
        t.setheading(90)
        draw_lines(x + 3, y + 3, 5)
        t.setheading(-90)
        draw_lines(x + 3, y - 3, 5)
    elif direction == 'right':
        t.setheading(180)
        draw_lines(x - 3, y + 3, 5)
        draw_lines(x - 3, y - 3, 5)
        t.setheading(90)
        draw_lines(x - 3, y + 3, 5)
        t.setheading(-90)
        draw_lines(x - 3, y - 3, 5)


leftScale = -80
rightScale = 80
downScale = -90
upScale = 90


def draw_lines(x, y, distance):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(distance)


# 绘制所有横线
t.setheading(0)
for i in range(10):
    draw_lines(-80, 90-20*i, 80*2)

# 绘制所有竖线
t.setheading(-90)
for i in range(9):
    draw_lines(80-20*i, 90, 90-10)
for i in range(9):
    draw_lines(80-20*i, -10, 90-10)

# 绘制所有斜线
t.setheading(-135)
for i in range(2):
    draw_lines(20, 90-i*140, 1.41*40)
t.setheading(-45)
for i in range(2):
    draw_lines(-20, 90-i*140, 1.41*40)

# 绘制兵炮位置
angle(60, 50)
angle(-60, 50)
angle(60, -50)
angle(-60, -50)
angle(40, 30)
angle(-40, 30)
angle(40, -30)
angle(-40, -30)
angle(0, 30)
angle(0, -30)

angle_half(80, 30, 'right')
angle_half(80, -30, 'right')
angle_half(-80, 30, 'left')
angle_half(-80, -30, 'left')


# 绘制大外框斜线
t.pensize(5)
t.setheading(0)
for i in [95,-95]:
    draw_lines(-85, i, 85*2)
t.left(-90)
for i in [-85, 85]:
    draw_lines(i, 95, 95*2)


turtle.done()