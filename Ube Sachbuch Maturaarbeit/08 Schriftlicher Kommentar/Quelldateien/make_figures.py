"""Abbildungen für den Kommentar «Ube» (Abb. 1 bis 3)."""
from pathlib import Path
import datetime as dt
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyBboxPatch, PathPatch, Rectangle
from matplotlib.path import Path

FONT = "Carlito"
for f in font_manager.findSystemFonts():
    if "Carlito" in f:
        font_manager.fontManager.addfont(f)
plt.rcParams.update({"font.family": FONT, "font.size": 9, "svg.fonttype": "none"})

# Farben: Ube-Violett als Ordinalrampe (validiert: hell 2.80:1 auf Weiss) und Text-Tokens
V_DARK = "#5b2a86"     # 2025 / Akzent
V_LIGHT = "#a58fd6"    # 2010
V_WASH = "#efe9f7"     # Flächen in Diagrammen
V_WASH2 = "#e2d8f1"
INK = "#0b0b0b"
INK2 = "#52514e"
MUTED = "#898781"
GRID = "#e1e0d9"
BASE = "#c3c2b7"
GRAYFILL = "#f0efec"
OUT = str(Path(__file__).resolve().parent.parent / "Abbildungen") + "/"


def rounded_top_bar(ax, x, w, h, r_pts, color):
    """Säule mit 4px-Rundung oben, gerade an der Grundlinie."""
    # Radius in Datenkoordinaten umrechnen
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
    ax.add_patch(PathPatch(Path(verts, codes), facecolor=color, edgecolor="none", zorder=3))


def fmt(v, dec=0):
    s = f"{v:,.{dec}f}".replace(",", "'")
    if dec:
        s = s.replace(".", ",") if "'" not in s else s.replace(".", ",")
    return s


# ---------------------------------------------------------------- Abb. 3
def abb3():
    data = [
        ("Anbaufläche", "Hektaren", 4744, 2367, 0),
        ("Ernte", "Tonnen", 21906, 12483, 0),
        ("Ertrag pro Hektare", "Tonnen", 4.62, 5.27, 2),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(6.3, 2.9), dpi=300)
    fig.subplots_adjust(left=0.075, right=0.99, top=0.70, bottom=0.11, wspace=0.45)
    for ax, (title, unit, a, b, dec) in zip(axes, data):
        top = max(a, b) * 1.22
        ax.set_xlim(-0.6, 1.6)
        ax.set_ylim(0, top)
        for spine in ("top", "right", "left"):
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(BASE)
        ax.spines["bottom"].set_linewidth(0.8)
        ax.tick_params(axis="y", length=0, labelsize=7.5, labelcolor=MUTED)
        ax.tick_params(axis="x", length=0, labelsize=8.5, labelcolor=INK2, pad=4)
        ax.set_xticks([0, 1], ["2010", "2025"])
        ax.yaxis.grid(True, color=GRID, linewidth=0.6)
        ax.set_axisbelow(True)
        import matplotlib.ticker as mt
        if dec:
            ax.yaxis.set_major_locator(mt.MultipleLocator(2))
            ax.yaxis.set_major_formatter(mt.FuncFormatter(lambda v, p: f"{v:.0f}"))
        else:
            ax.yaxis.set_major_locator(mt.MaxNLocator(4))
            ax.yaxis.set_major_formatter(mt.FuncFormatter(lambda v, p: f"{v:,.0f}".replace(",", "'")))
        fig.canvas.draw()
        w = 0.42
        for i, (val, col) in enumerate(((a, V_LIGHT), (b, V_DARK))):
            rounded_top_bar(ax, i - w / 2, w, val, 3, col)
            lab = f"{val:.2f}".replace(".", ",") if dec else f"{val:,.0f}".replace(",", "'")
            ax.text(i, val + top * 0.025, lab, ha="center", va="bottom", fontsize=8.5,
                    color=INK, fontweight="bold")
        ch = (b - a) / a * 100
        sign = "+" if ch > 0 else "−"
        ax.text(0.0, 1.2, title, transform=ax.transAxes, fontsize=9.5, color=INK, fontweight="bold", va="bottom")
        ax.text(0.0, 1.07, f"in {unit}, {sign}{abs(ch):.0f} % seit 2010", transform=ax.transAxes,
                fontsize=8, color=INK2, va="bottom")
    # Legende (zwei Serien) oben
    lx = 0.06
    fig.text(0.01, 0.95, "Ube auf den Philippinen, 2010 und 2025", fontsize=10, fontweight="bold", color=INK)
    fig.patches.append(Rectangle((0.66, 0.948), 0.014, 0.03, transform=fig.transFigure, color=V_LIGHT, figure=fig))
    fig.text(0.68, 0.951, "2010", fontsize=8.5, color=INK2)
    fig.patches.append(Rectangle((0.74, 0.948), 0.014, 0.03, transform=fig.transFigure, color=V_DARK, figure=fig))
    fig.text(0.76, 0.951, "2025", fontsize=8.5, color=INK2)
    fig.savefig(OUT + "abb3_flaeche_ernte.png", dpi=300, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Abb. 1
def abb1():
    D = lambda m, d: dt.date(2026, m, d).toordinal()
    x0, x1 = D(4, 1), D(11, 27)
    fig, ax = plt.subplots(figsize=(6.3, 2.85), dpi=300)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    ax.set_xlim(x0 - 2, x1)
    ax.set_ylim(-1.42, 1.72)
    ax.axis("off")
    y = 0.0
    # Phasen als Bänder (helle Töne, Punkte tragen die Farbe)
    ax.add_patch(FancyBboxPatch((D(4, 20), y - 0.07), D(8, 24) - D(4, 20), 0.14,
                                boxstyle="round,pad=0,rounding_size=0.07", fc="#d9d7d0", ec="none", zorder=2))
    ax.add_patch(FancyBboxPatch((D(8, 25), y - 0.07), D(11, 10) - D(8, 25), 0.14,
                                boxstyle="round,pad=0,rounding_size=0.07", fc=V_LIGHT, ec="none", zorder=2))
    # Monate direkt unter dem Band
    months = ["April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November"]
    for i, m in enumerate(range(4, 12)):
        ax.plot([D(m, 1), D(m, 1)], [y - 0.12, y - 0.2], color=BASE, lw=0.6)
        ax.text(D(m, 15), y - 0.27, months[i], ha="center", va="top", fontsize=7, color=MUTED)
    # Phasen-Beschriftung direkt unter den Monaten
    ax.text((D(4, 20) + D(8, 24)) / 2, y - 0.52, "Phase 1: Kochbuch «Salu-Salo»", ha="center", va="top",
            fontsize=8.3, color=INK2, fontweight="bold")
    ax.text((D(8, 25) + D(11, 10)) / 2, y - 0.52, "Phase 2: Sachbuch «Ube»", ha="center", va="top",
            fontsize=8.3, color=INK, fontweight="bold")
    # Zeiträume unter der Linie (Ferien, ungefähr)
    for (a, b, lab) in ((D(7, 4), D(8, 9), "Sommerferien: Befragung\nauf den Philippinen (Tim, John)"),
                        (D(9, 26), D(10, 11), "Herbstferien: viel\nam Buch geschrieben")):
        yb = y - 0.9
        ax.plot([a, a, b, b], [yb + 0.07, yb, yb, yb + 0.07], color=MUTED, lw=0.8)
        ax.text((a + b) / 2, yb - 0.07, lab, ha="center", va="top", fontsize=7.2, color=INK, linespacing=1.15)
    xa = D(11, 10)
    # Meilensteine über der Linie: (datum, text, ebene, ausrichtung)
    t1, t2 = 0.98, 1.66
    ms = [
        (D(4, 22), "22.04.\nStart mit dem\nKochbuch", t1, "center"),
        (D(6, 19), "19.06.\nZwischen-\npräsentation", t1, "center"),
        (D(8, 25), "Ende August\nEntscheid\nfür Ube", t1, "right"),
        (D(9, 3), "03.09.\nTeams-Call mit\nFrau Büschlen", t2, "left"),
        (D(10, 20), "Oktober\nInterview statt\nUmfrage", t1, "right"),
        (D(11, 4), "Anfang November\nAntworten von Tita,\nSatz in InDesign", t2, "center"),
        (D(11, 10), "10.11.\nAbgabe", t1, "left"),
    ]
    for (xd, lab, h, al) in ms:
        top_of_leader = h - 0.43
        ax.plot([xd, xd], [y + 0.1, top_of_leader + 0.04], color=BASE, lw=0.7, zorder=1)
        dx = {"center": 0, "right": 1.2, "left": -1.2}[al]
        ax.text(xd + dx, h, lab, ha=al, va="top", fontsize=7.2, color=INK, linespacing=1.15)
    # Punkte mit weissem Ring
    for xd in [m[0] for m in ms]:
        col = INK if xd < D(8, 25) else V_DARK
        ax.plot([xd], [y], marker="o", markersize=5.6, color=col, markeredgecolor="white",
                markeredgewidth=1.3, zorder=4)
    fig.savefig(OUT + "abb1_zeitstrahl.png", dpi=300, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Abb. 2
def box(ax, x, y, w, h, text, fc, tc=INK, fs=8, bold=False, ec="none"):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.12",
                                fc=fc, ec=ec, lw=0.8, zorder=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal", linespacing=1.2, zorder=3, wrap=True)


def arrow(ax, x0, y0, x1, y1):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=0.9, shrinkA=0, shrinkB=0,
                                mutation_scale=8), zorder=1)


def abb2():
    fig, ax = plt.subplots(figsize=(6.3, 5.0), dpi=300)
    fig.subplots_adjust(left=0.01, right=0.99, top=0.99, bottom=0.01)
    W, H = 12.0, 9.6
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    # Leitfrage
    box(ax, 0.3, 8.45, 11.4, 0.95,
        "Leitfrage: Inwiefern verändert der internationale Ube-Trend die traditionelle Bedeutung,\nVerwendung und Produktion von Ube auf den Philippinen?",
        GRAYFILL, fs=8.2)
    arrow(ax, 6, 8.45, 6, 8.08)
    # Leitthese
    box(ax, 0.3, 7.1, 11.4, 0.95,
        "Leitthese: Die Philippinen verlieren beim Ube-Boom nicht ihre Kultur,\nsondern die Kontrolle über sie.",
        V_DARK, tc="white", fs=8.6, bold=True)
    # Kontrolle-Definition
    ax.text(6, 6.86, "Kontrolle heisst: wer an Ube verdient und wer bestimmt, wofür Ube in der Welt steht",
            ha="center", va="top", fontsize=7.4, color=INK2, style="italic")
    # Teilfragen
    cols = [(0.3, 5.35, "Geld", "Verdienen die Philippinen\nam Boom mit?"),
            (5.85, 2.9, "Bedeutung", "Bedeutet Ube den Menschen\nnoch dasselbe?"),
            (8.95, 2.75, "Produktion", "Kann die Produktion\nwieder wachsen?")]
    for (x, w, head, q) in cols:
        arrow(ax, x + w / 2, 6.5, x + w / 2, 6.18)
        box(ax, x, 5.15, w, 1.0, "", V_WASH, fs=7.9)
        ax.text(x + w / 2, 5.88, head, ha="center", va="center", fontsize=8.2, color=INK, fontweight="bold", zorder=3)
        ax.text(x + w / 2, 5.47, q, ha="center", va="center", fontsize=7.9, color=INK, linespacing=1.2, zorder=3)
    # Thesen
    th = [(0.3, 2.55, "These 1\nDas Ube-Paradox", 0.3 + 5.35 / 2),
          (3.1, 2.55, "These 2\nMatcha oder Quinoa?", 0.3 + 5.35 / 2),
          (5.85, 2.9, "These 3\nVom Lebensmittel\nzum Bild", 5.85 + 1.45),
          (8.95, 2.75, "These 4\nMehr Felder allein\nreichen nicht", 8.95 + 1.375)]
    for (x, w, t, src) in th:
        arrow(ax, src, 5.15, x + w / 2, 4.62)
        head, rest = t.split("\n", 1)
        box(ax, x, 3.5, w, 1.1, "", "white", fs=8, ec=V_LIGHT)
        ax.text(x + w / 2, 4.33, head, ha="center", va="center", fontsize=8.2, color=INK, fontweight="bold", zorder=3)
        ax.text(x + w / 2, 3.93 if "\n" not in rest else 3.86, rest, ha="center", va="center", fontsize=7.9,
                color=INK, linespacing=1.2, zorder=3)
    # Schema
    ax.text(0.3, 3.18, "Schema jeder These", fontsize=7.6, color=INK2, fontweight="bold", va="center")
    steps = ["drei\nBehauptungen", "Begründung\nund Belege", "Einwände\nprüfen", "Fazit mit\nangepasster These"]
    sx, sw, gap = 0.3, 2.55, 0.4
    for i, s in enumerate(steps):
        x = sx + i * (sw + gap)
        box(ax, x, 2.05, sw, 0.85, s, V_WASH2, fs=7.8)
        if i < len(steps) - 1:
            arrow(ax, x + sw + 0.04, 2.475, x + sw + gap - 0.04, 2.475)
    arrow(ax, 6, 2.05, 6, 1.42)
    box(ax, 2.6, 0.45, 6.8, 0.95, "Was bleibt von unserer Leitthese?\nAntworten auf die drei Teilfragen und Grenzen",
        V_DARK, tc="white", fs=8.2, bold=True)
    fig.savefig(OUT + "abb2_thesenschema.png", dpi=300, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    abb1()
    abb2()
    abb3()
    print("ok")
