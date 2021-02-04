import turtle

slowpoke = turtle.Turtle()
slowpoke.shape('turtle')
pokey = turtle.Turtle()
pokey.shape('turtle')


def make_square(the_turtle):
    slowpoke.forward(100)
    slowpoke.right(90)
    slowpoke.forward(100)
    slowpoke.right(90)
    slowpoke.forward(100)
    slowpoke.right(90)
    slowpoke.forward(100)
    slowpoke.right(90)


def make_spiral(the_turtle):
    for i in range(36):
        make_square(the_turtle)
        the_turtle.right(10)


make_spiral(slowpoke)

turtle.mainloop()
