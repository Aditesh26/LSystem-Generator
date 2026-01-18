import turtle

t = turtle.Turtle()
t.speed(0)
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
rules = {"F": "F+F--F+F"}
print(expand_lsystem("F", rules, 2))

def draw(t, instructions, angle, steps = 5):
    for command in instructions:
        if command == "F":
            t.forward(steps)
        elif command == "+":
            t.right(angle)
        elif command == "-":
            t.left(angle)

draw(t, "F+F--F+F", 60,100)
turtle.done()