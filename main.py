import turtle
import tkinter as tk

root = tk.Tk()
root.title("L-System Fractal Tree")


controls_frame = tk.Frame(root,width = 300)
controls_frame.pack(side=tk.LEFT, fill=tk.Y)

canvas_frame = tk.Frame(root)
canvas_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(canvas_frame,width = 800,height = 600, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

screen = turtle.TurtleScreen(canvas)
screen.tracer(0,0)

t = turtle.RawTurtle(screen)
t.speed(0)
t.left(90)


root.mainloop()


t = turtle.Turtle()
t.speed(10)
def expand_lsystem(axiom, rules, iterations):
    current = axiom
    for i in range(iterations):
        next_string = ""
        for symbol in current:
            if symbol in rules:
                next_string += rules[symbol]
            else:
                next_string += symbol
        current = next_string
    return current
rules = {
    "X": "F[+X][-X]FX",
    "F": "FF"
}
print(expand_lsystem("F", rules, 2))

def draw(t, instructions, angle, steps = 5):

    history = []

    for command in instructions:
        if command == "F":
            t.forward(steps)
        elif command == "+":
            t.right(angle)
        elif command == "-":
            t.left(angle)
        elif command == "[":
            history.append((t.position(), t.heading()))
        elif command == "]":
            position, heading = history.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()

t.left(90)
s = expand_lsystem("X", rules, 4)
draw(t, s, 25,10)


