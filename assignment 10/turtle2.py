import turtle

t=turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.speed("fast")
screen = turtle.Screen()
screen.title("suherfe.blog.ir")
t.width(3)
for i in range(8):
   for j in range(8):
      t.forward(100)
      t.right(45)
   t.right(45)
t.hideturtle()

print("Suherfe.blog.ir")