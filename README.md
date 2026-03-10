# L-Systems Fractal Tree 🌿

An interactive fractal tree generator built with Python, using **L-Systems** (Lindenmayer Systems) to produce beautiful plant-like structures rendered in a GUI.

---

## 📁 Project Structure

```
├── L-Systems.py     # Main app — L-system engine, turtle renderer, tkinter GUI
└── README.md        # Project documentation
```

---

## ⚙️ Requirements

- Python 3.8+
- No external libraries — uses only the Python standard library (`turtle`, `tkinter`)

---

## 🛠️ Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <project-folder>
   ```

2. **Run the app**
   ```bash
   python L-Systems.py
   ```

---

## 🖥️ How It Works

An **L-System** is a formal grammar that rewrites symbols iteratively using production rules. Each symbol maps to a drawing instruction:

| Symbol | Action                        |
|--------|-------------------------------|
| `F`    | Move forward (draw a line)    |
| `+`    | Turn right by the given angle |
| `-`    | Turn left by the given angle  |
| `[`    | Save current position/heading |
| `]`    | Restore position/heading      |

After expanding the axiom through the rules N times, the resulting string is passed to a turtle renderer that draws the fractal.

---

## 🎛️ GUI Controls

| Control        | Description                                              |
|----------------|----------------------------------------------------------|
| **Axiom**      | The starting symbol string (e.g. `X`)                   |
| **Iterations** | How many times to apply the rules (keep ≤ 7)            |
| **Angle**      | Branching angle in degrees (e.g. `25`)                  |
| **Step Size**  | Length of each forward step in pixels                   |
| **Rules**      | Production rules, one per line in `KEY:VALUE` format    |
| **Generate**   | Expand and draw the L-system                            |
| **Reset**      | Clear the canvas                                        |
| **Go to Center** | Move the turtle to the center of the canvas           |
| **Go to Bottom** | Move the turtle to the bottom of the canvas           |

---

## 🌱 Default Example

The app loads with a classic fractal tree preset:

```
Axiom:      X
Iterations: 4
Angle:      25°
Rules:
  X : F[+X][-X]FX
  F : FF
```

---

## 💡 Tips

- Try different angles (e.g. `90` for a grid-like structure, `60` for a snowflake)
- Iterations above **7** are blocked to prevent freezing
- Branch depth affects color — deeper branches are darker green

---

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
