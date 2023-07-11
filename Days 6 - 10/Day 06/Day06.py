import turtle


def draw_square(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)

        t.left(90)

        draw_square(turtle.Turtle(), 50)
