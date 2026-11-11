# Electric and Magnetic Fields – Summary

> [!info] Sources
> Only Aezri's own course material: formula sheet, Exam B with solution key, the class problems (A–E) with solutions, the electric field problems (Giancoli 19–36) and the book chapters from the course. The label in brackets, e.g. **(G23)** or **(A1)**, tells you where a task comes from.

Back to [[00 Start]]. Words and translations: [[02 Glossary English–German]].

This summary starts from zero. Every level builds on the one before. Do not skip a level: read it, then try the **Check yourself** questions *before* you open the answers. If you get one wrong, read the level again.

> [!tip] How to use this note
> - Tap a grey box like **Answer** to open it.
> - Write the working on paper, exactly like in the exam.
> - Rule of thumb for the exam: **about 1 minute per point**. 43 points → 45 minutes.

---

## Level 0 – The tools you need first

### 0.1 Powers of ten and prefixes
Physics uses very big and very small numbers. We write them with powers of ten:
$3.0 \cdot 10^{4} = 30\,000$ and $2.0 \cdot 10^{-9} = 0.000\,000\,002$.

A **prefix** is a short name for a power of ten:

| Prefix | Symbol | Value |
| --- | --- | --- |
| nano | n | $10^{-9}$ |
| micro | µ | $10^{-6}$ |
| milli | m | $10^{-3}$ |
| centi | c | $10^{-2}$ |
| kilo | k | $10^{3}$ |
| mega | M | $10^{6}$ |

**Method:** first convert to the base unit, then to the target unit.
Example (Exam B, Q1b): $0.45\ \text{mT} = 0.45 \cdot 10^{-3}\ \text{T} = 450 \cdot 10^{-6}\ \text{T} = 450\ \mu\text{T}$.

> [!note] Sanity check
> Going to a **smaller** unit (mT → µT) makes the number **bigger**. Going to a **bigger** unit makes it **smaller**.

### 0.2 Directions on the page
The exam always uses the same six directions: **up, down, left, right**, and two directions you cannot draw flat:
- **⊙ (dot) = out of the page**, towards you. Think of the tip of an arrow flying at you.
- **⊗ (cross) = into the page**, away from you. Think of the feathers at the back of an arrow.

### 0.3 Force and Newton's second law
A **force** is a push or a pull, measured in **newtons (N)**. Newton's second law connects force, mass and acceleration:
$$F = m \cdot a \qquad\Rightarrow\qquad a = \frac{F}{m}$$
**Weight** is the force of gravity: $F_G = m \cdot g$ with $g = 9.81\ \text{m/s}^2$.

> [!question]- Check yourself (Level 0) – Answer
> *From Exam B, question 1b.*
> 1. Convert 3.2·10⁵ N/C into kN/C. → **320 kN/C**
> 2. Convert 1.2·10⁴ nC into mC. → $1.2\cdot10^{4}\cdot10^{-9}\ \text{C} = 1.2\cdot10^{-5}\ \text{C} =$ **1.2·10⁻² mC**
> 3. What does ⊗ mean? → **into the page**

---

## Level 1 – Electric charge and the electric field

### 1.1 Charge
Everything is made of atoms. Atoms contain **protons** (positive charge) and **electrons** (negative charge). Charge is measured in **coulombs (C)**.
- The smallest charge is the **elementary charge** $e = 1.602\cdot10^{-19}\ \text{C}$. A proton has $+e$, an electron $-e$.
- **Like charges repel** (+ and +, − and −). **Opposite charges attract** (+ and −).

### 1.2 What a field is
A charge changes the space around it. Any other charge placed there feels a force. We call this changed space the **electric field** $\vec E$.

Picture it as a map: at every point, an arrow tells you how strongly and in which direction a small **positive test charge** would be pushed.

$$\boxed{E = \frac{F}{q}} \qquad \text{unit: N/C}$$

The field is the **force per coulomb**. If you know the field, you get the force on any charge:
$$F = q \cdot E$$

### 1.3 Direction – the two rules you always need
1. **Force on a positive charge:** in the **same** direction as $\vec E$.
2. **Force on a negative charge:** in the **opposite** direction to $\vec E$.

> [!important] The test charge does not make the field
> The field is created by **other** charges (the *source* charges). If you take the test charge away, the field at that point stays **exactly the same**.

### 1.4 Field of a single point charge
$$\boxed{E = k\,\frac{Q}{r^2}} \qquad k = 8.99\cdot10^{9}\ \text{N m}^2/\text{C}^2$$
- $Q$ = charge that creates the field, $r$ = distance from it **in metres**.
- **Positive** source: field points **away** from it. **Negative** source: field points **towards** it.
- $r^2$ means **inverse square**: double the distance → the field becomes **¼**.

### 1.5 Field lines
Field lines are a drawing of the field:
- They **start on + charges** and **end on − charges**.
- The arrow on a line shows the direction of $\vec E$.
- **Close lines = strong field**, spread-out lines = weak field.
- Field lines **never cross**.

Single negative charge: straight lines pointing **in**. A + and − pair: curved lines going from + to −, densest between them.

### 1.6 Worked example (exam style)
A test charge $q = +2.0\ \text{nC}$ feels $6.0\cdot10^{-5}\ \text{N}$ to the right.
- $E = F/q = 6.0\cdot10^{-5} / 2.0\cdot10^{-9} = 3.0\cdot10^{4}\ \text{N/C}$, **to the right**.
- A charge of −5.0 nC at the same point: $F = |q|E = 5.0\cdot10^{-9}\cdot3.0\cdot10^{4} = 1.5\cdot10^{-4}\ \text{N}$, **to the left** (negative → opposite).
- Test charge removed: field still $3.0\cdot10^{4}$ N/C to the right.

> [!question]- Check yourself (Level 1) – Answer
> *From your Giancoli problems 19–22 and Exam B.*
> 1. **(G19)** Force on an electron in a field of 2460 N/C pointing east? → $F = eE = 1.602\cdot10^{-19}\cdot2460 =$ **3.94·10⁻¹⁶ N, west** (negative → opposite)
> 2. **(G21)** Field 21.7 cm directly above a charge of 33.0·10⁻⁶ C? → $8.99\cdot10^{9}\cdot33.0\cdot10^{-6}/0.217^2 =$ **6.30·10⁶ N/C, upward** (away from +)
> 3. **(G22)** A downward force of 6.4 N acts on a −7.3 µC charge. Field? → $E = 6.4/7.3\cdot10^{-6} =$ **8.8·10⁵ N/C, up** (negative charge → field opposite to force)
> 4. **(Exam B, Q2a)** Field lines of one negative charge? → **straight radial lines, arrows pointing in**

---

## Level 2 – Two charges: adding fields

### 2.1 Superposition
When there are two charges, each makes its own field. The total field is their **vector sum**. On a straight line this is easy: call right **+** and left **−**, then add with signs.

**Four-step method:**
1. Sketch the charges and the point P. Write the distances in **metres**.
2. At P draw one arrow per charge: **away from +**, **towards −**.
3. Calculate each size with $E = kQ/r^2$.
4. Add with signs. Answer with size, unit and direction.

> [!note] Between two charges
> - **Same signs** (+ and +): the arrows point in **opposite** directions → **subtract**.
> - **Opposite signs** (+ and −): the arrows point the **same** way → **add**.

### 2.2 Where is the field zero?
- **Same signs:** the zero point is **between** them, closer to the **smaller** charge.
- **Opposite signs:** **never between** them. It is **outside**, on the side of the **smaller** charge.

**The fast way** (saves 10 minutes in the exam): at the zero point both fields have the same size. With distances $x$ and $y$ to the two charges:
$$k\frac{Q_1}{x^2} = k\frac{Q_2}{y^2} \quad\Rightarrow\quad \boxed{\frac{x}{y} = \sqrt{\frac{Q_1}{Q_2}}}$$

**Example (Exam B, Q3b):** $Q_1 = +9.0\ \mu\text{C}$, $Q_2 = +1.0\ \mu\text{C}$, 20 cm apart.
$x/y = \sqrt{9} = 3$ and $x + y = 20$ cm → $y = 5$ cm, **$x = 15$ cm from $Q_1$**.

> [!question]- Check yourself (Level 2) – Answer
> *From your Giancoli problems 24, 32 and 34.*
> 1. **(G24)** Field midway between −8.0 µC and +5.8 µC, 6.0 cm apart? → opposite signs → both arrows point towards the negative charge → add: $E = \frac{k}{(0.030)^2}(8.0 + 5.8)\cdot10^{-6} =$ **1.4·10⁸ N/C, towards the negative charge**
> 2. **(G32)** $Q_1 = -32\ \mu\text{C}$ and $Q_2 = +45\ \mu\text{C}$ are 12 cm apart. The field is zero at P, outside, on the side of $Q_1$. How far is P from $Q_1$? → zero point next to the **smaller** charge: $\frac{x+12}{x} = \sqrt{45/32} = 1.186$ → **x ≈ 65 cm**
> 3. **(G34)** The field is zero one third of the way from $Q_1$ to $Q_2$. Ratio $Q_1/Q_2$? → $x/y = 1/2 = \sqrt{Q_1/Q_2}$ → **$Q_1/Q_2 = 1/4$**

---

## Level 3 – A charged particle in an electric field

Now we use the field to move something. Take an electron in a field $E$:
1. **Force:** $F = |q|E = eE$.
2. **Direction:** electron is negative → **opposite** to $E$.
3. **Weight:** $F_G = m_e g$ with $m_e = 9.109\cdot10^{-31}$ kg.
4. **Compare:** divide the two. The electric force is usually about $10^{13}$ times bigger → gravity can be ignored.
5. **Acceleration:** $a = F/m$.

**Example (Exam B, Q4):** electron, $E = 500$ N/C pointing up.
$F = 1.602\cdot10^{-19}\cdot500 = 8.0\cdot10^{-17}$ N, **down**. Weight $= 8.9\cdot10^{-30}$ N → about $10^{13}$ times smaller. $a = 8.0\cdot10^{-17}/9.109\cdot10^{-31} = 8.8\cdot10^{13}\ \text{m/s}^2$, down.

> [!note] Proton vs. electron
> A proton has the same size of charge, so it feels the **same size of force** (opposite direction). But it is about **1836 times heavier** ($m_p = 1.673\cdot10^{-27}$ kg), so it accelerates 1836 times less.

> [!question]- Check yourself (Level 3) – Answer
> *From your Giancoli problem 23 and Exam B, Q4.*
> 1. **(G23)** Acceleration of an electron in a field of 756 N/C? → $a = eE/m_e = 1.602\cdot10^{-19}\cdot756/9.11\cdot10^{-31} =$ **1.33·10¹⁴ m/s²**
> 2. **(G23)** How does the direction of the acceleration depend on the field? → **opposite to the field** (negative charge)
> 3. **(Exam B, Q4)** Why can you ignore the electron's weight? → the electric force is about **10¹³ times larger**

---

## Level 4 – Magnetism: magnets, wires and the right-hand rule

### 4.1 Magnets
Every magnet has a **north pole (N)** and a **south pole (S)**. Like poles repel, opposite poles attract. You can never get only one pole.

**Magnetic field lines:**
- Outside the magnet they go from **N to S**, inside from **S to N**. They are **closed loops**.
- The field is strongest near the **poles**, where the lines are densest.
- A compass needle's **N pole points along the field**.

The magnetic field is written $\vec B$ and measured in **tesla (T)**. The Earth's field is about **50 µT**.

### 4.2 A current makes a magnetic field
**Moving charges** (a current, measured in amperes A) create a magnetic field. Around a long straight wire the field lines are **circles**.
$$\boxed{B = \frac{\mu_0 I}{2\pi r}} \qquad \mu_0 = 4\pi\cdot10^{-7}\ \text{T m/A}$$
Shortcut: $\frac{\mu_0}{2\pi} = 2\cdot10^{-7}$, so $B = 2\cdot10^{-7}\cdot\frac{I}{r}$.

> [!important] E and B fall off differently
> - Point charge: $E \propto 1/r^2$ → double the distance → **¼**.
> - Straight wire: $B \propto 1/r$ → double the distance → **½**.

### 4.3 Right-hand rule for a wire
**Point your right thumb along the current. Your curled fingers show the direction of $\vec B$.**
- Current **out of the page** (⊙) → circles run **counterclockwise**.
- Current **into the page** (⊗) → circles run **clockwise**.
- Reverse the current → the field reverses, every compass needle turns 180°.

Compasses around a wire with current **out of the page** (Exam B, Q5): above → **left**, below → **right**, left → **down**, right → **up**.

Horizontal wire, current to the right (Exam B, Q6): **above** the wire the field points **out of the page**, **below** it **into the page**.

### 4.4 Two wires
Same method as for two charges: field of each wire at the point, then add with signs.
- Currents in the **same** direction: between the wires the fields are **opposite** → **subtract**.
- Currents in **opposite** directions: between the wires the fields point the **same** way → **add**.

**Zero point between two same-direction wires:**
$$\frac{I_1}{x} = \frac{I_2}{d - x} \quad\Rightarrow\quad \frac{x}{d-x} = \frac{I_1}{I_2}$$
**No square root here!** (That is only for electric fields, because of $1/r^2$.)

**Example (Exam B, Q7):** 30 A and 10 A, both out of the page, 10 cm apart.
- Midpoint: $B_1 = 2\cdot10^{-7}\cdot30/0.050 = 1.2\cdot10^{-4}$ T (up), $B_2 = 4.0\cdot10^{-5}$ T (down) → **8.0·10⁻⁵ T, up**.
- Zero point: $30(0.10 - x) = 10x$ → **x = 7.5 cm** from the 30 A wire.

> [!question]- Check yourself (Level 4) – Answer
> *From your class problems (Giancoli examples 20-9, 20-10 and D1) and Exam B.*
> 1. **(Ex. 20-9)** A wire carries 25 A. Field at 10 cm? → $2\cdot10^{-7}\cdot25/0.10 =$ **5.0·10⁻⁵ T** (about as strong as the Earth's field)
> 2. **(Ex. 20-10)** Two wires 10.0 cm apart: 5.0 A out of the page, 7.0 A into the page. Field at the midpoint? → opposite currents → add: $2.0\cdot10^{-5} + 2.8\cdot10^{-5} =$ **4.8·10⁻⁵ T, up**
> 3. **(D1a)** A power line 8.5 m above the ground carries 95 A. Field at the ground? → $2\cdot10^{-7}\cdot95/8.5 =$ **2.24 µT**, about **4.5 %** of the Earth's field
> 4. **(D1b)** The current flows north-east. Direction of B at the ground? → **north-west**
> 5. **(Exam B, Q5)** Current reversed: what happens to the compass needles? → **all turn by 180°**

---

## Level 5 – Magnetic forces (study problems)

> [!warning] Not on the formula sheet
> These formulas are **not** given in the exam. They appear in your study problems, so learn them by heart.

### 5.1 Force on a current-carrying wire
$$F = B\,I\,L\,\sin\theta$$
$\theta$ = angle between the wire and $\vec B$. At 90° the force is largest ($F = BIL$). Wire parallel to $\vec B$ → **no force**.

**Direction:** point your fingers along the **current**, curl them towards $\vec B$, your **thumb** shows the force.
Example (Giancoli 20-1): current through a wire, B to the right, wire at 60° → force **into the page**, $F = 0.90\cdot30\cdot0.12\cdot\sin60^\circ = 2.8$ N.

### 5.2 Force on a moving charge
$$F = q\,v\,B\,\sin\theta$$
Same right-hand rule with **velocity** instead of current, for a **positive** charge. **Negative charge → reverse the direction.**

The force is always **perpendicular** to the velocity. It changes the direction, never the speed. That is why charges move in **circles**:
$$q v B = \frac{m v^2}{r} \quad\Rightarrow\quad r = \frac{m v}{q B} \qquad T = \frac{2\pi m}{q B}$$
The period $T$ does **not** depend on the speed. This is the idea behind the **cyclotron**.

### 5.3 Useful combinations
- Accelerated through a voltage $U$: $qU = \tfrac12 m v^2$ → $v = \sqrt{2qU/m}$.
- **Velocity selector** ($E$ and $B$ perpendicular): forces cancel when $v = E/B$.
- **Mass spectrometer:** same $q$, $v$, $B$ → $r \propto m$.

### 5.4 Solenoids and electromagnets
A **solenoid** is a long coil. Inside, the field is strong and uniform:
$$B = \frac{\mu_0 N I}{L} = \mu_0 n I \qquad (n = N/L = \text{turns per metre})$$
The area of the coil does **not** matter. Electromagnet: stronger current → stronger field, reversed current → **N and S swap**, and it can be **switched on and off**.

> [!question]- Check yourself (Level 5) – Answer
> *From your class problems A1, B1, C1 and E1.*
> 1. **(A1)** 160 m of wire, 150 A, Earth's field 5.0·10⁻⁵ T at 65° to the wire. Force? → $5.0\cdot10^{-5}\cdot150\cdot160\cdot\sin65^\circ =$ **1.09 N**
> 2. **(B1)** A positive charge moving right in B into the page feels a force up. Which way for a **negative** charge? → **down**
> 3. **(C1)** First cyclotron: 11 cm diameter, protons at 3.93·10⁶ m/s. Which B? → $B = \frac{mv}{qr} = \frac{1.67\cdot10^{-27}\cdot3.93\cdot10^{6}}{1.602\cdot10^{-19}\cdot0.055} =$ **0.745 T** (radius = half the diameter!)
> 4. **(E1a)** Solenoid: number of loops tripled, length doubled. B? → $\times 3/2$ → **B → 3/2 B**

---

## Exam checklist

- [ ] **Every number has a unit.** Without a unit there is no point.
- [ ] **Every direction has a short reason**, e.g. "negative charge, so opposite to E".
- [ ] All distances converted to **metres** before calculating.
- [ ] Arrows drawn **before** adding fields.
- [ ] Zero point: **square root** for charges, **no root** for wires.
- [ ] Keep going after a mistake: a correct method with a wrong earlier result still scores points.

More practice with instant feedback: the learning system linked in [[00 Start]].
