import turtle
t = turtle.Pen()
t.shape('turtle')
t.color('Red')
t.stamp()
move = 30
for i in range (12):
    move+=30
    t.right(move)
    t.penup()
    t.forward(75)
    t.pendown()
    t.forward(50)
    t.penup()
    t.forward(25)
    t.stamp()
    t.home()
    
    