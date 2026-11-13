# Cheat Sheet: welche Formel wann?

Zurück zu [[00 Start]]. Ausführlich: [[05 Formelkarte für die Prüfung]].

**So benutzt du es:** Lies die Frage und suche die **Signalwörter** (englisch, wie in der Prüfung). Die Tabelle sagt dir, welche Formel du nimmst.

---

## 1. Gesucht: elektrisches Feld E (Einheit N/C)

| Signalwörter in der Frage | Gegeben | Formel |
| --- | --- | --- |
| "a **test charge** … **experiences a force** …", "find the **electric field**" | Kraft F und Ladung q | $E = F/q$ |
| "field … **cm from / above** a charge", "**point charge**" | Ladung Q und Abstand r | $E = kQ/r^2$ (r in **m**!) |
| "**accelerates** at … m/s²", "find the electric field" | Beschleunigung a | **zuerst** $F = m\cdot a$, **dann** $E = F/q$ |
| "**midway** between", "at the **midpoint**", zwei Ladungen | zwei Ladungen, Abstand | $E = kQ/r^2$ **zweimal**, dann gleiche Richtung **addieren**, entgegengesetzt **subtrahieren** |
| "where is the field **zero**" | zwei Ladungen | $x/y = \sqrt{Q_1/Q_2}$, dann **Blöcke** (Verhältnis + 1) |

## 2. Gesucht: Kraft F (Einheit N)

| Signalwörter | Gegeben | Formel |
| --- | --- | --- |
| "**force on** a charge / electron / proton **in an electric field**" | Feld E | $F = q\cdot E$ |
| "**compare** it with its **weight**" | Masse m | $F_G = m\cdot g$, dann **F ÷ F_G** (meist ≈ 10¹³ → Gewicht vernachlässigbar) |
| "**wire / line / rail** carries a **current** … in a **magnetic field**", "force on the wire" | B, I, Länge L, Winkel | $F = B\cdot I\cdot L\cdot\sin\theta$ |
| "a charge **moves at** … m/s in a **magnetic field**", "Lorentz force" | q, v, B | $F = q\cdot v\cdot B\cdot\sin\theta$ |
| "**float** / **hover** / balance" | Masse | Kraft nach oben **=** Gewicht: $qE = mg$ oder $BIL = mg$ |

## 3. Gesucht: Beschleunigung a (Einheit m/s²)

| Signalwörter | Formel |
| --- | --- |
| "what is the **acceleration**" | zuerst die Kraft F ausrechnen, dann $a = F/m$ (Richtung = wie die Kraft) |

## 4. Gesucht: Magnetfeld B (Einheit T)

| Signalwörter | Gegeben | Formel |
| --- | --- | --- |
| "**long, straight wire**", "**power line**", "… m / cm **from** the wire" | Strom I und Abstand r | $B = 2\cdot10^{-7}\cdot I / r$ (durch r **teilen**!) |
| "**at what distance** … as strong as the Earth's field (50 µT)" | I und B | $r = 2\cdot10^{-7}\cdot I / B$ (50 µT = 5.0·10⁻⁵ T) |
| "**two wires**", "midpoint" | zwei Ströme | $B = 2\cdot10^{-7}\cdot I/r$ **zweimal**, Pfeile zeichnen, addieren/subtrahieren |
| "where is B **zero**" (zwei Leiter) | zwei Ströme | $x/y = I_1/I_2$ (**ohne Wurzel!**), dann Blöcke |
| "**solenoid**", "**coil**", "**loops**", "windings" | N, I, L oder n | $B = \mu_0 N I / L = \mu_0 n I$ (n pro **Meter**: 3/cm = 300/m) |
| "**circular** motion", "**radius**", "**cyclotron**", "**diameter**" | m, v, q, r | $B = \dfrac{m v}{q r}$ (Durchmesser **halbieren**!) |
| "is **tripled / doubled / halved** … what happens to B" (Spule) | Änderungen | B ∝ N · I / L: oben N und I, unten L, **Fläche egal** |
| "**Earth's field** … total field … direction / angle" | B_Erde und B_Spule | Pythagoras / tan θ = B₁ / B₂ (E3) |

## 5. Gesucht: Radius, Geschwindigkeit, Masse (Level 5)

| Signalwörter | Formel |
| --- | --- |
| "**radius** of the circle", "how big is the circle" | $r = \dfrac{m v}{q B}$ |
| "**accelerated through a voltage** of … V" | $q U = \tfrac12 m v^2$ → $v = \sqrt{2qU/m}$ (zuerst v, dann weiterrechnen) |
| "**velocity filter / selector**", "passes **straight** through" | $v = E/B$ |
| "**mass spectrometer**", "mystery element" | gleiche q, v, B → r ∝ m: $m_2 = m_1 \cdot r_2 / r_1$ |
| "how long for **half a circle**" (cyclotron) | $T/2 = \dfrac{\pi m}{q B}$ |

## 6. Gesucht: Richtung (keine Formel, eine Regel)

| Signalwörter | Regel |
| --- | --- |
| "**direction** of the field" (Ladung) | **+** → weg, **−** → hin |
| Kraft / Beschleunigung eines **Elektrons** | **entgegengesetzt** zu E ("negative charges go against the field") |
| "**compass**", Strom **⊙ out of / ⊗ into the page** | ⊙ → gegen den Uhrzeigersinn ↺, ⊗ → im Uhrzeigersinn ↻ |
| Leiter **in** der Ebene (Strom →), "**below / above** the line" | oben ⊙ **out**, unten ⊗ **into** (Strom ← umgekehrt). Antwort immer into/out! |
| "direction of the **force**" (Leiter oder Ladung in B) | 1. **Ausschliessen** (F ⟂ v und ⟂ B) → 2. **Hand** oder **Kreis** right → up → out → right → 3. **negativ? umkehren!** |
| "**find B**" (v und F gegeben) | gleich: ausschliessen → 2 Möglichkeiten testen |
| "current is **reversed**" | alles dreht sich um, Kompassnadeln um 180° |
| "two wires, **attract or repel**" | gleiche Stromrichtung → **ziehen sich an**, entgegengesetzt → **stossen sich ab** |

## 7. Skizzen und Wissensfragen (ohne Rechnung)

| Signalwörter | Antwort |
| --- | --- |
| "sketch the **field lines**", **negative** charge | gerade Linien, Pfeile **zur Ladung hin** |
| Feldlinien **+ und −** | von + nach −, am dichtesten **zwischen** den Ladungen, kreuzen sich nie |
| "**+Q and −3Q**" | −3Q bekommt **3-mal mehr** Linien |
| "**bar magnets**" | aussen **N → S**, geschlossene Schleifen, am stärksten **nahe den Polen** |
| "test charge is **removed**" | Feld bleibt **gleich** (es kommt von den anderen Ladungen) |
| "**electromagnet** … current increased / reversed / advantage" | stärker (B ∝ I) / Pole tauschen / **ein- und ausschaltbar** |

---

## Einheiten (ohne Einheit kein Punkt!)
**E** → N/C · **B** → T · **F** → N · **a** → m/s² · **r, L** → m

## Nach jedem Resultat
☐ Einheit ☐ Richtung mit Begründung ☐ Minus im Exponenten ☐ cm → m ☐ negativ umgekehrt? ☐ Durchmesser → Radius
