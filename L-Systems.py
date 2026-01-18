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


def draw(t, instructions, angle, steps = 5):

    history = []

    depth = 0

    for command in instructions:
        if command == "F":
            t.forward(steps)
        elif command == "+":
            t.right(angle)
        elif command == "-":
            t.left(angle)
        elif command == "[":
            history.append((t.position(), t.heading()))
            depth+=1
        elif command == "]":
            position, heading = history.pop()
            t.penup()
            t.setposition(position)
            t.setheading(heading)
            t.pendown()
        t.pencolor(0, max(0.3, 1 - depth * 0.1), 0)



def generate():
    t.clear()
    t.penup()
    t.home()
    t.setheading(90)
    t.pendown()

    rules = {
        "X": "F[+X][-X]FX",
        "F": "FF"
    }

    try:
        axiom = axiom_entry.get()
        iterations = int(iter_entry.get())
        angle = float(angle_entry.get())
        steps = int(step_entry.get())
    except ValueError:
        print("Invalid input")
        return

    if iterations > 7:
        print("Warning: High iteration count may freeze the app")
        return
    s = expand_lsystem(axiom, rules, iterations)
    draw(t, s, angle, steps)
    
    screen.update()

def reset():
    t.clear()
    t.penup()
    t.home()
    t.setheading(90)
    t.pendown()
    screen.update()
    



tk.Label(controls_frame, text="Axiom").pack(pady=(10, 0))
axiom_entry = tk.Entry(controls_frame)
axiom_entry.pack()
axiom_entry.insert(0, "X")


tk.Label(controls_frame, text="Iterations").pack(pady=(10, 0))
iter_entry = tk.Entry(controls_frame)
iter_entry.pack()
iter_entry.insert(0, "4")


tk.Label(controls_frame, text="Angle").pack(pady=(10, 0))
angle_entry = tk.Entry(controls_frame)
angle_entry.pack()
angle_entry.insert(0, "25")


tk.Label(controls_frame, text="Step Size").pack(pady=(10, 0))
step_entry = tk.Entry(controls_frame)
step_entry.pack()
step_entry.insert(0, "5")


tk.Label(controls_frame, text="Rules").pack(pady=(10, 0))
rules_text = tk.Text(controls_frame, height=5, width=25)
rules_text.pack()

rules_text.insert(
    "1.0",
    "X:F[+X][-X]FX\nF:FF"
)



generate_btn = tk.Button(
    controls_frame,
    text="Generate",
    command= generate
)
generate_btn.pack(pady=20)

reset_btn = tk.Button(
    controls_frame,
    text="Reset",
    command= reset
)
reset_btn.pack(pady=10)

root.mainloop()