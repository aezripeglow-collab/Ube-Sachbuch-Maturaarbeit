"""Abbildungen für den Kommentar «Ube» (Abb. 1 bis 4).

Abb. 1  Zeitstrahl des ganzen Projekts (April bis November 2026)
Abb. 2  Arbeitsplan der Ube-Phase: wer wann woran gearbeitet hat
Abb. 3  Aufbau von Kapitel 3 mit allen Behauptungen
Abb. 4  Anbaufläche, Ernte und Ertrag 2010 und 2025 mit eigener Rechnung

Daten für Abb. 1 und 2: unser Arbeitsjournal. Daten für Abb. 4: CPBRD 2026.
"""
import datetime as dt
from pathlib import Path as _P

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path

FONT = "Carlito"
for f in font_manager.findSystemFonts():
    if "Carlito" in f:
        font_manager.fontManager.addfont(f)
plt.rcParams.update({"font.family": FONT, "font.size": 9, "svg.fonttype": "none"})

# Farben: Ube-Violett als Ordinalrampe und Text-Tokens
V_DARK = "#5b2a86"
V_LIGHT = "#a58fd6"
V_WASH = "#efe9f7"
V_WASH2 = "#e2d8f1"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASE = "#c3c2b7"
GRAYFILL = "#f0efec"
GRAYPHASE = "#a9a79d"
HOLIDAY = "#ecebe6"
OUT = str(_P(__file__).resolve().parent.parent / "Abbildungen") + "/"


def D(m, d):
    return dt.date(2026, m, d).toordinal()


def rounded_top_bar(ax, x, w, h, r_pts, color, dashed=False):
    """Säule mit Rundung oben, gerade an der Grundlinie."""
    fig = ax.figure
    bbox = ax.get_window_extent()
    xr = (ax.get_xlim()[1] - ax.get_xlim()[0]) / bbox.width * r_pts * fig.dpi / 72
    yr = (ax.get_ylim()[1] - ax.get_ylim()[0]) / bbox.height * r_pts * fig.dpi / 72
    xr = min(xr, w / 2)
    yr = min(yr, h / 2)
    k = 0.5523
    verts = [
        (x, 0), (x, h - yr),
        (x, h - yr + k * yr), (x + xr - k * xr, h), (x + xr, h),
        (x + w - xr, h),
        (x + w - xr + k * xr, h), (x + w, h - yr + k * yr), (x + w, h - yr),
        (x + w, 0), (x, 0),
    ]
    codes = [Path.MOVETO, Path.LINETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.LINETO,
             Path.CURVE4, Path.CURVE4, Path.CURVE4,
             Path.LINETO, Path.CLOSEPOLY]
    if dashed:
        ax.add_patch(PathPatch(Path(verts, codes), facecolor="white", edgecolor=V_DARK,
                               linewidth=1.0, linestyle=(0, (3, 2)), zorder=3))
    else:
        ax.add_patch(PathPatch(Path(verts, codes), facecolor=color, edgecolor="none", zorder=3))


def relax(ys, gap, lo, hi, it=400):
    """Verschiebt Beschriftungen so wenig wie möglich, bis sie sich nicht mehr überlappen."""
    y = list(ys)
    for _ in range(it):
        moved = False
        for i in range(1, len(y)):
            d = y[i] - y[i - 1]
            if d < gap:
                s = (gap - d) / 2
                y[i - 1] -= s
                y[i] += s
                moved = True
        y = [min(max(v, lo), hi) for v in y]
        if not moved:
            break
    for i in range(1, len(y)):
        if y[i] - y[i - 1] < gap:
            y[i] = y[i - 1] + gap
    return y


# ---------------------------------------------------------------- Abb. 1
EVENTS = [
    # (datum, text, art)   art: k = wichtiger Entscheid/Termin, n = normal, x = Nachricht von aussen
    (D(4, 22), "Start mit Regionen und Gerichten", "k"),
    (D(5, 6), "Projektplan im Arbeitsvertrag", "n"),
    (D(5, 20), "Interviewfragen zur Küche", "n"),
    (D(6, 3), "Begleitkommentar begonnen", "n"),
    (D(6, 10), "Titelblatt: der gedeckte Tisch", "n"),
    (D(6, 17), "Kommentar abgegeben", "n"),
    (D(6, 19), "Zwischenpräsentation", "k"),
    (D(6, 26), "Schriftliche Beurteilung erhalten", "n"),
    (D(7, 3), "Letzter Schultag, Plan für die Ferien", "n"),
    (D(8, 12), "Erstes Treffen: vier Probleme", "n"),
    (D(8, 14), "Viele Kochbücher, keines über Ube", "n"),
    (D(8, 19), "Teams-Call: die Idee mit Ube", "n"),
    (D(8, 21), "Entscheid für das Sachbuch «Ube»", "k"),
    (D(8, 26), "Aufteilung in drei Teile", "n"),
    (D(9, 3), "Teams-Call mit Frau Büschlen", "k"),
    (D(9, 13), "Berichte über den Exportstopp", "x"),
    (D(9, 14), "Treffen wegen des Exportstopps", "n"),
    (D(9, 23), "Drei Leitfragen für Kapitel 3", "n"),
    (D(9, 25), "Leitthese formuliert", "k"),
    (D(9, 30), "Vier Thesen verteilt", "n"),
    (D(10, 6), "Ministerium: 1'000 Hektaren mehr", "x"),
    (D(10, 21), "Zwei Thesen werden zu These 3", "n"),
    (D(10, 23), "Interview statt Umfrage", "k"),
    (D(10, 28), "Familie findet eine Ube-Bäuerin", "n"),
    (D(11, 4), "Titas Antworten, Satz in InDesign", "n"),
    (D(11, 6), "Alle Teile in einem Dokument", "n"),
    (D(11, 10), "Abgabe", "k"),
]


def abb1():
    W, H = 6.3, 7.35
    fig = plt.figure(figsize=(W, H), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    t0, t1 = D(4, 14), D(11, 16)
    ytop, ybot = 0.72, H - 0.18

    def Y(d):
        return ytop + (d - t0) / (t1 - t0) * (ybot - ytop)

    # Monate als feine Bänder mit Namen am linken Rand
    names = {4: "April", 5: "Mai", 6: "Juni", 7: "Juli", 8: "August", 9: "September", 10: "Oktober", 11: "November"}
    for m in range(4, 12):
        a = max(D(m, 1), t0)
        b = min(D(m + 1, 1) if m < 12 else D(12, 31), t1)
        if m % 2 == 0:
            ax.add_patch(Rectangle((0, Y(a)), W, Y(b) - Y(a), fc="#f7f6f3", ec="none", zorder=0))
        ax.plot([0, 0.55], [Y(D(m, 1)), Y(D(m, 1))] if D(m, 1) >= t0 else [Y(a), Y(a)], color=GRID, lw=0.6,
                zorder=1)
        ax.text(0.04, Y(a) + 0.05, names[m], ha="left", va="top", fontsize=7.2, color=MUTED, zorder=2)
    # Schulferien
    for (a, b, lab) in ((D(7, 4), D(8, 9), "Sommerferien"), (D(9, 26), D(10, 11), "Herbstferien")):
        ax.add_patch(Rectangle((0.62, Y(a)), W - 0.62, Y(b) - Y(a), fc=HOLIDAY, ec="none", zorder=0.5))
        ax.text(W - 0.05, Y(b) - 0.05, lab, ha="right", va="bottom", fontsize=7.2, color=MUTED,
                style="italic", zorder=2)
    # Achse: zwei Phasen
    X = 3.15
    ax.plot([X, X], [Y(D(4, 22)), Y(D(8, 21))], color=GRAYPHASE, lw=3.2, solid_capstyle="round", zorder=3)
    ax.plot([X, X], [Y(D(8, 21)), Y(D(11, 10))], color=V_DARK, lw=3.2, solid_capstyle="round", zorder=3)
    # Befragung als Klammer (rechts)
    a, b = Y(D(7, 15)), Y(D(8, 5))
    bx = X + 0.16
    ax.plot([bx + 0.05, bx, bx, bx + 0.05], [a, a, b, b], color=INK2, lw=0.8, zorder=3)
    ax.text(bx + 0.14, (a + b) / 2 - 0.08, "15.07. bis 05.08.", ha="left", va="center", fontsize=7.6,
            color=INK, fontweight="bold", zorder=4)
    ax.text(bx + 0.14, (a + b) / 2 + 0.08, "Befragung auf den Philippinen (Tim, John)", ha="left", va="center",
            fontsize=7.6, color=INK, zorder=4)
    # Ereignisse abwechselnd links und rechts
    left = [e for i, e in enumerate(EVENTS) if i % 2 == 0]
    right = [e for i, e in enumerate(EVENTS) if i % 2 == 1]
    gap = 0.165
    for side, evs in (("L", left), ("R", right)):
        ys = relax([Y(e[0]) for e in evs], gap, ytop - 0.1, ybot + 0.1)
        for (d, txt, kind), yl in zip(evs, ys):
            yt = Y(d)
            col = GRAYPHASE if d < D(8, 21) else V_DARK
            big = kind == "k"
            ax.plot([X], [yt], marker="o", markersize=6.4 if big else 4.2, color=col if kind != "x" else "white",
                    markeredgecolor="white" if kind != "x" else col, markeredgewidth=1.2 if kind != "x" else 1.0,
                    zorder=5)
            sgn = -1 if side == "L" else 1
            x_lab = X + sgn * 0.24
            ax.plot([X + sgn * 0.06, X + sgn * 0.13, x_lab - sgn * 0.02], [yt, yt, yl], color=BASE, lw=0.6,
                    zorder=2)
            date = dt.date.fromordinal(d).strftime("%d.%m.")
            weight = "bold" if big else "normal"
            style = "italic" if kind == "x" else "normal"
            color = INK if kind != "x" else INK2
            if side == "L":
                ax.text(x_lab, yl, date, ha="right", va="center", fontsize=7.6, color=INK, fontweight="bold",
                        zorder=4)
                ax.text(x_lab - 0.43, yl, txt, ha="right", va="center", fontsize=7.6, color=color,
                        fontweight=weight, style=style, zorder=4)
            else:
                ax.text(x_lab, yl, date, ha="left", va="center", fontsize=7.6, color=INK, fontweight="bold",
                        zorder=4)
                ax.text(x_lab + 0.43, yl, txt, ha="left", va="center", fontsize=7.6, color=color,
                        fontweight=weight, style=style, zorder=4)
    # Legende oben
    ly = 0.24
    ax.plot([0.08, 0.38], [ly, ly], color=GRAYPHASE, lw=3.2, solid_capstyle="round")
    ax.text(0.46, ly, "Kochbuch «Salu-Salo»", va="center", fontsize=7.8, color=INK2)
    ax.plot([1.72, 2.02], [ly, ly], color=V_DARK, lw=3.2, solid_capstyle="round")
    ax.text(2.10, ly, "Sachbuch «Ube»", va="center", fontsize=7.8, color=INK2)
    ax.plot([3.13], [ly], marker="o", markersize=6.4, color=INK2, markeredgecolor="white", markeredgewidth=1.2)
    ax.text(3.24, ly, "wichtiger Entscheid oder Termin", va="center", fontsize=7.8, color=INK2)
    ax.plot([5.08], [ly], marker="o", markersize=4.2, color="white", markeredgecolor=INK2, markeredgewidth=1.0)
    ax.text(5.17, ly, "Nachricht", va="center", fontsize=7.8, color=INK2, style="italic")
    ax.add_patch(Rectangle((0.08, ly + 0.17), 0.30, 0.13, fc=HOLIDAY, ec="none"))
    ax.text(0.46, ly + 0.235, "Schulferien", va="center", fontsize=7.8, color=INK2)
    fig.savefig(OUT + "zeitstrahl.png", dpi=300, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Abb. 2
TASKS = [
    # (person, spur, start, ende, text)
    ("Aezri", 0, D(8, 26), D(9, 23), "Teil 1"),
    ("Aezri", 0, D(10, 2), D(10, 30), "These 1 und 2"),
    ("Aezri", 0, D(11, 5), D(11, 9), "Abschluss"),
    ("Aezri", 1, D(10, 23), D(11, 4), "Interview"),
    ("Tim", 0, D(8, 26), D(9, 23), "Teil 2"),
    ("Tim", 0, D(9, 30), D(11, 4), "These 4"),
    ("Tim", 0, D(11, 5), D(11, 9), "Gegenlesen"),
    ("Tim", 1, D(10, 2), D(10, 9), "Rechnungen"),
    ("John", 0, D(8, 26), D(9, 2), "Fragebogen"),
    ("John", 1, D(9, 4), D(9, 16), "Recherche"),
    ("John", 1, D(9, 18), D(9, 23), "Leitfragen"),
    ("John", 0, D(9, 30), D(11, 4), "These 3"),
    ("John", 1, D(11, 4), D(11, 10), "InDesign"),
]
JOINT = [
    (D(8, 21), "Entscheid", 0, "left"),
    (D(8, 26), "Aufteilung", 1, "left"),
    (D(9, 3), "Frau Büschlen", 0, "left"),
    (D(9, 14), "Exportstopp", 1, "left"),
    (D(9, 25), "Leitthese", 0, "left"),
    (D(9, 30), "vier Thesen", 1, "left"),
    (D(10, 21), "These 3 vereint", 0, "left"),
    (D(10, 23), "Interview statt Umfrage", 1, "left"),
    (D(11, 10), "Abgabe", 0, "left"),
]


def abb2():
    W, H = 6.3, 3.12
    fig = plt.figure(figsize=(W, H), dpi=300)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(H, 0)
    ax.axis("off")
    t0, t1 = D(8, 19), D(11, 20)
    x0, x1 = 0.62, W - 0.08

    def Xd(d):
        return x0 + (d - t0) / (t1 - t0) * (x1 - x0)

    rows = [("Aezri", 2), ("Tim", 2), ("John", 2)]
    lane_h, bar_h = 0.26, 0.19
    y = 0.86
    rowy = {}
    for name, lanes in rows:
        rowy[name] = y
        y += lanes * lane_h + 0.12
    yend = y - 0.10
    # Herbstferien
    ax.add_patch(Rectangle((Xd(D(9, 26)), 0.72), Xd(D(10, 11)) - Xd(D(9, 26)), yend - 0.72, fc=HOLIDAY, ec="none",
                           zorder=0))
    ax.text((Xd(D(9, 26)) + Xd(D(10, 11))) / 2, yend + 0.02, "Herbstferien", ha="center", va="top", fontsize=7,
            color=MUTED, style="italic")
    # Monatsachse unten
    ya = yend + 0.20
    ax.plot([x0, x1], [ya, ya], color=BASE, lw=0.8)
    for m, name in ((9, "September"), (10, "Oktober"), (11, "November")):
        ax.plot([Xd(D(m, 1))] * 2, [0.72, ya + 0.06], color=GRID, lw=0.6, zorder=0.6)
        nxt = D(m + 1, 1) if m < 11 else D(11, 10)
        ax.text((Xd(D(m, 1)) + Xd(min(nxt, t1))) / 2, ya + 0.08, name, ha="center", va="top", fontsize=7.5,
                color=INK2)
    for d in range(t0, t1 + 1):
        dd = dt.date.fromordinal(d)
        if dd.weekday() == 0:
            ax.plot([Xd(d)] * 2, [ya, ya + 0.04], color=BASE, lw=0.6)
    ax.text(x0, ya + 0.08, "August", ha="left", va="top", fontsize=7.5, color=INK2)
    # Gemeinsame Termine als feine senkrechte Linien mit Beschriftung oben
    for (d, lab, tier, ha) in JOINT:
        xx = Xd(d)
        yt = 0.16 if tier == 0 else 0.40
        ax.plot([xx, xx], [yt + 0.10, yend], color=V_DARK, lw=0.6, ls=(0, (2, 2)), zorder=1)
        ax.plot([xx], [yt + 0.10], marker="D", markersize=3.6, color=V_DARK, zorder=2)
        ax.text(xx + (0.05 if ha == "left" else -0.05), yt + 0.03, lab, ha=ha, va="bottom", fontsize=7,
                color=INK2, zorder=2)
    # Personen und Balken
    for name, lanes in rows:
        y0 = rowy[name]
        ax.text(0.04, y0 + lanes * lane_h / 2 - 0.03, name, ha="left", va="center", fontsize=8.5,
                color=INK, fontweight="bold")
        ax.plot([0.04, x1], [y0 + lanes * lane_h + 0.08] * 2, color=GRID, lw=0.5, zorder=0.6)
    fig.canvas.draw()
    rend = fig.canvas.get_renderer()
    for (name, lane, a, b, txt) in TASKS:
        yc = rowy[name] + lane * lane_h + lane_h / 2
        xa, xb = Xd(a), Xd(b)
        ax.add_patch(FancyBboxPatch((xa + 0.01, yc - bar_h / 2), xb - xa - 0.02, bar_h,
                                    boxstyle="round,pad=0,rounding_size=0.045", fc=V_LIGHT, ec="none", zorder=3))
        t = ax.text((xa + xb) / 2, yc, txt, ha="center", va="center", fontsize=7.3, color=INK, zorder=4)
        bb = t.get_window_extent(renderer=rend)
        wid_in = bb.width / fig.dpi
        if wid_in > (xb - xa) - 0.06:
            t.remove()
            ax.text(xb + 0.05, yc, txt, ha="left", va="center", fontsize=7.3, color=INK, zorder=4,
                    bbox=dict(boxstyle="square,pad=0.12", fc="white", ec="none"))
    fig.savefig(OUT + "arbeitsplan.png", dpi=300, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Abb. 3
def box(ax, x, y, w, h, text, fc, tc=INK, fs=8, bold=False, ec="none"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                fc=fc, ec=ec, lw=0.9, zorder=2))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc,
                fontweight="bold" if bold else "normal", linespacing=1.25, zorder=3)


def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>,head_length=0.35,head_width=0.18", color=MUTED, lw=0.8,
                                shrinkA=0, shrinkB=0), zorder=1)


def abb3():
    W, H = 12.0, 9.45
    fig, ax = plt.subplots(figsize=(6.3, 6.3 * H / W), dpi=300)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    box(ax, 0.3, 8.5, 11.4, 0.85,
        "Leitfrage: Inwiefern verändert der internationale Ube-Trend die traditionelle Bedeutung,\nVerwendung und Produktion von Ube auf den Philippinen?",
        GRAYFILL, fs=8.2)
    arrow(ax, 6, 8.5, 6, 8.22)
    box(ax, 0.3, 7.35, 11.4, 0.85,
        "Leitthese: Die Philippinen verlieren beim Ube-Boom nicht ihre Kultur,\nsondern die Kontrolle über sie.",
        V_DARK, tc="white", fs=8.6, bold=True)
    ax.text(6, 7.17, "Kontrolle heisst: wer an Ube verdient und wer bestimmt, wofür Ube in der Welt steht",
            ha="center", va="top", fontsize=7.4, color=INK2, style="italic")
    cols = [(0.3, 5.35, "Geld", "Verdienen die Philippinen\nam Boom mit?"),
            (5.85, 2.9, "Bedeutung", "Bedeutet Ube den Menschen\nnoch dasselbe?"),
            (8.95, 2.75, "Produktion", "Kann die Produktion\nwieder wachsen?")]
    for (x, w, head, q) in cols:
        arrow(ax, x + w / 2, 6.92, x + w / 2, 6.67)
        box(ax, x, 5.75, w, 0.9, "", V_WASH, fs=7.9)
        ax.text(x + w / 2, 6.43, head, ha="center", va="center", fontsize=8.2, color=INK, fontweight="bold", zorder=3)
        ax.text(x + w / 2, 6.04, q, ha="center", va="center", fontsize=7.9, color=INK, linespacing=1.15, zorder=3)
    th = [(0.3, 2.6, "These 1", "Das Ube-Paradox", 0.3 + 5.35 / 2,
           ["knapper, obwohl die\nNachfrage steigt", "der Boom gefährdet\nseine Grundlage", "vor allem andere\nverdienen daran"]),
          (3.05, 2.6, "These 2", "Matcha oder Quinoa?", 0.3 + 5.35 / 2,
           ["als Rohstoff-\nlieferant verlieren", "Erfolg hängt an\nHerkunft und Ansehen", "Verarbeitung\nim eigenen Land"]),
          (5.85, 2.9, "These 3", "Vom Lebensmittel zum Bild", 5.85 + 1.45,
           ["im Westen zählt\ndie Farbe", "auf den Philippinen\nein Schatz", "die Pflanze gerät\naus dem Blick"]),
          (8.95, 2.75, "These 4", "Mehr Felder allein\nreichen nicht", 8.95 + 1.375,
           ["mehr Fläche ist\nVoraussetzung", "ohne Pflanzgut\nbleiben Felder leer", "der Anbau muss\nsich lohnen"])]
    top, bot = 5.43, 2.18
    for (x, w, head, title, src, claims) in th:
        arrow(ax, src, 5.75, x + w / 2, top + 0.02)
        box(ax, x, bot, w, top - bot, "", "white", ec=V_LIGHT)
        ax.text(x + w / 2, top - 0.24, head, ha="center", va="center", fontsize=8.2, color=INK,
                fontweight="bold", zorder=3)
        ax.text(x + w / 2, top - 0.64 if "\n" in title else top - 0.56, title, ha="center", va="center",
                fontsize=7.8, color=INK, linespacing=1.1, zorder=3)
        cy = top - 1.28
        for i, c in enumerate(claims):
            box(ax, x + 0.12, cy - 0.29, w - 0.24, 0.64, "", V_WASH, fs=7)
            ax.text(x + 0.27, cy + 0.03, str(i + 1), ha="center", va="center", fontsize=7.4, color=V_DARK,
                    fontweight="bold", zorder=3)
            ax.text(x + w / 2 + 0.08, cy + 0.03, c, ha="center", va="center", fontsize=7.0, color=INK,
                    linespacing=1.1, zorder=3)
            cy -= 0.78
    ax.text(0.3, 1.98, "Bei jeder These", fontsize=7.6, color=INK2, fontweight="bold", va="center")
    steps = ["drei Behauptungen\nbegründen und belegen", "Einwände suchen\nund prüfen", "Fazit mit\nangepasster These"]
    sx, sw, gap = 0.3, 3.5, 0.45
    for i, s in enumerate(steps):
        xx = sx + i * (sw + gap)
        box(ax, xx, 1.1, sw, 0.7, s, V_WASH2, fs=7.8)
        if i < len(steps) - 1:
            arrow(ax, xx + sw + 0.05, 1.45, xx + sw + gap - 0.05, 1.45)
    arrow(ax, 6, 1.1, 6, 0.87)
    box(ax, 2.6, 0.05, 6.8, 0.8, "Was bleibt von unserer Leitthese?\nAntworten auf die drei Teilfragen und Grenzen",
        V_DARK, tc="white", fs=8.2, bold=True)
    fig.savefig(OUT + "thesenschema.png", dpi=300, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Abb. 4
def abb4():
    data = [
        ("Anbaufläche", "Hektaren", 4744, 2367, 0, None),
        ("Ernte", "Tonnen", 21906, 12483, 0, 25019),
        ("Ertrag pro Hektare", "Tonnen", 4.62, 5.27, 2, None),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(6.3, 3.05), dpi=300, gridspec_kw={"width_ratios": [2, 3, 2]})
    fig.subplots_adjust(left=0.075, right=0.99, top=0.70, bottom=0.17, wspace=0.42)
    for ax, (title, unit, a, b, dec, cf) in zip(axes, data):
        vals = [a, b] + ([cf] if cf else [])
        top = max(vals) * 1.22
        n = len(vals)
        ax.set_xlim(-0.6, n - 0.4)
        ax.set_ylim(0, top)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(BASE)
        ax.spines["bottom"].set_linewidth(0.8)
        ax.tick_params(axis="y", length=0, labelsize=7.5, labelcolor=MUTED)
        ax.tick_params(axis="x", length=0, labelsize=8.2, labelcolor=INK2, pad=4)
        labels = ["2010", "2025"] + (["Rechnung"] if cf else [])
        ax.set_xticks(range(n), labels)
        ax.yaxis.grid(True, color=GRID, linewidth=0.6)
        ax.set_axisbelow(True)
        if dec:
            ax.yaxis.set_major_locator(mt.MultipleLocator(2))
            ax.yaxis.set_major_formatter(mt.FuncFormatter(lambda v, p: f"{v:.0f}"))
        else:
            ax.yaxis.set_major_locator(mt.MaxNLocator(4))
            ax.yaxis.set_major_formatter(mt.FuncFormatter(lambda v, p: f"{v:,.0f}".replace(",", "'")))
        fig.canvas.draw()
        w = 0.42
        for i, val in enumerate(vals):
            if i == 2:
                rounded_top_bar(ax, i - w / 2, w, val, 3, None, dashed=True)
                lab = "≈ 25'000"
            else:
                rounded_top_bar(ax, i - w / 2, w, val, 3, V_LIGHT if i == 0 else V_DARK)
                lab = f"{val:.2f}".replace(".", ",") if dec else f"{val:,.0f}".replace(",", "'")
            ax.text(i, val + top * 0.025, lab, ha="center", va="bottom", fontsize=8.3, color=INK,
                    fontweight="bold")
        ch = (b - a) / a * 100
        sign = "+" if ch > 0 else "−"
        ax.text(0.0, 1.2, title, transform=ax.transAxes, fontsize=9.5, color=INK, fontweight="bold", va="bottom")
        ax.text(0.0, 1.07, f"in {unit}, {sign}{abs(ch):.0f} % seit 2010", transform=ax.transAxes,
                fontsize=8, color=INK2, va="bottom")
        if cf:
            ax.text(2, -top * 0.13, "Ertrag 2025 auf der\nFläche von 2010", ha="center", va="top", fontsize=6.8,
                    color=INK2, linespacing=1.1)
    fig.text(0.01, 0.95, "Ube auf den Philippinen, 2010 und 2025", fontsize=10, fontweight="bold", color=INK)
    fig.patches.append(Rectangle((0.555, 0.948), 0.014, 0.03, transform=fig.transFigure, color=V_LIGHT, figure=fig))
    fig.text(0.575, 0.951, "2010", fontsize=8.3, color=INK2)
    fig.patches.append(Rectangle((0.63, 0.948), 0.014, 0.03, transform=fig.transFigure, color=V_DARK, figure=fig))
    fig.text(0.65, 0.951, "2025", fontsize=8.3, color=INK2)
    fig.patches.append(Rectangle((0.705, 0.948), 0.014, 0.03, transform=fig.transFigure, fc="white", ec=V_DARK,
                                 lw=0.8, ls=(0, (2, 1.5)), figure=fig))
    fig.text(0.725, 0.951, "eigene Rechnung", fontsize=8.3, color=INK2)
    fig.savefig(OUT + "flaeche_ernte.png", dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    _P(OUT).mkdir(exist_ok=True)
    abb1()
    abb2()
    abb3()
    abb4()
    print("ok")
