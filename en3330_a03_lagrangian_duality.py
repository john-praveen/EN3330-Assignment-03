# EN3330 Assignment 03 - PRAVEEN V.V.J. (220491B)
# This one file makes all the graphs used in the report.
# Problem: minimize x^2 subject to x >= 1
# Lagrangian: L(mu, x) = x^2 + mu(1 - x), mu >= 0

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Graphs are saved in an "images" folder next to this file
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
os.makedirs(OUT, exist_ok=True)


# Colours and plot style
C = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100",
     "#e87ba4", "#008300", "#6250d6", "#e34948"]
INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS = "#e1e0d9", "#c3c2b7"
INFEAS = "#e34948"

plt.rcParams.update({
    "font.family": "serif",
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.titlesize": 10.5,
    "axes.labelsize": 10.5,
    "axes.edgecolor": AXIS,
    "axes.labelcolor": INK,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "xtick.color": INK2,
    "ytick.color": INK2,
    "lines.linewidth": 2.0,
    "legend.frameon": False,
    "legend.fontsize": 9,
    "savefig.bbox": "tight",
    "savefig.pad_inches": 0.03,
})


# Lagrangian
def L(mu, x):
    return x**2 + mu * (1 - x)


# Dual function (found in Q1(b))
def d(mu):
    return mu - mu**2 / 4


# Shade the infeasible region x < 1
def shade_infeasible(ax, x0, x1, label=True):
    ax.axvspan(x0, x1, color=INFEAS, alpha=0.07, lw=0)
    ax.axvline(x1, color=INFEAS, lw=1.0, ls="--")
    if label:
        ax.text((x0 + x1) / 2, 0.96, r"infeasible ($x<1$)", transform=ax.get_xaxis_transform(),
                ha="center", va="top", color=INFEAS, fontsize=9)


# Save a graph as a PDF
def save(fig, name):
    fig.savefig(os.path.join(OUT, name))
    plt.close(fig)
    print("saved", name)


# Q1(a): L(mu, x) for mu = 0, 1, 2, 3 and the minimum point x = mu/2 of each curve
x = np.linspace(-1.5, 3.0, 600)
mus = [0, 1, 2, 3]
fig, ax = plt.subplots(figsize=(6.0, 3.9))
shade_infeasible(ax, -1.5, 1.0)
for i, mu in enumerate(mus):
    ax.plot(x, L(mu, x), color=C[i], label=rf"$\mu={mu}$", zorder=3)
    xm = mu / 2
    ax.plot(xm, L(mu, xm), "o", ms=7, color=C[i], mec="white", mew=1.5, zorder=4)
    ax.annotate(rf"$x({mu})={xm:g}$", (xm, L(mu, xm)), xytext=(-0.55 + 0.75 * mu, -0.65),
                fontsize=8.5, color=INK2, ha="center", va="center",
                arrowprops=dict(arrowstyle="-", color=C[i], lw=0.8, shrinkB=4))
ax.set_xlim(-1.5, 3.0)
ax.set_ylim(-1, 7)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$L(\mu,x)=x^2+\mu(1-x)$")
ax.legend(loc="upper center", ncol=4, bbox_to_anchor=(0.5, 1.12), handlelength=1.6,
          columnspacing=1.0)
save(fig, "q1a_lagrangian.pdf")


# Q1(b): dual function d(mu), maximum at mu* = 2
m = np.linspace(0, 5, 400)
fig, ax = plt.subplots(figsize=(6.0, 3.4))
ax.plot(m, d(m), color=C[0], label=r"$d(\mu)=\mu-\mu^2/4$")
ax.axhline(1, color=INK2, lw=1.0, ls="--", label=r"$p^*=f(x^*)=1$")
ax.plot(2, 1, "o", ms=8, color=C[0], mec="white", mew=1.5, zorder=5)
ax.annotate(r"$\mu^*=2,\ d^*=1$", (2, 1), xytext=(2.35, 0.25), fontsize=9.5,
            arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.axvline(2, color=MUTED, lw=0.8, ls=":")
ax.set_xlim(0, 5)
ax.set_ylim(-1.4, 1.5)
ax.set_xlabel(r"$\mu$")
ax.set_ylabel(r"$d(\mu)$")
ax.legend(loc="lower left")
save(fig, "q1b_dual.pdf")


# Q1(c): L(mu, x) for larger mu values and the primal function g(x)
x = np.linspace(-1, 3, 800)
fig, ax = plt.subplots(figsize=(6.0, 3.9))
shade_infeasible(ax, -1, 1.0, label=False)
for i, mu in enumerate([0, 2, 5, 10, 25]):
    ax.plot(x, L(mu, x), color=C[[0, 1, 2, 3, 6][i]], lw=1.1, alpha=0.75,
            label=rf"$L({mu},x)$")
xf = x[x >= 1]
ax.plot(xf, xf**2, color=INK, lw=2.6, label=r"$g(x)=\max_{\mu\geq0}L(\mu,x)$", zorder=5)
# Arrows show g(x) goes to infinity when x < 1
for xa in np.linspace(-0.8, 0.8, 5):
    ax.annotate("", xy=(xa, 10.0), xytext=(xa, 8.6),
                arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
ax.text(0.0, 8.2, r"$g(x)=+\infty$", ha="center", va="top", fontsize=10, color=INK)
ax.text(-0.5, -1.3, r"infeasible ($x<1$)", ha="center", va="center", fontsize=8.5, color=INFEAS)
ax.plot(1, 1, "o", ms=8, color=INK, mec="white", mew=1.5, zorder=6)
ax.annotate(r"$\min_x g(x)=g(1)=1$", (1, 1), xytext=(1.55, -0.6), fontsize=9.5,
            arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
ax.text(1.75, 6.6, r"$g(x)=x^2$", fontsize=10, color=INK, ha="right")
ax.set_xlim(-1, 3)
ax.set_ylim(-2, 10)
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"value")
ax.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.2), fontsize=8.5)
save(fig, "q1c_primal.pdf")


# Q2(a)(iv): L(mu, x*) against mu (left) and L(mu*, x) against x (right)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.7))
m = np.linspace(0, 5, 200)
a1.plot(m, L(m, 1.0), color=C[0])
a1.plot(2, 1, "o", ms=8, color=C[0], mec="white", mew=1.5, zorder=5)
a1.annotate(r"$L(\mu^*,x^*)=1$", (2, 1), xytext=(2.3, 1.6), fontsize=9,
            arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
a1.set_xlim(0, 5); a1.set_ylim(0, 3)
a1.set_xlabel(r"$\mu$"); a1.set_ylabel(r"$L(\mu,x^*)$")
a1.set_title(r"$L(\mu,1)=1$ for all $\mu$  (flat)")
xx = np.linspace(-1, 3, 300)
a2.plot(xx, L(2, xx), color=C[1])
a2.plot(1, 1, "o", ms=8, color=C[1], mec="white", mew=1.5, zorder=5)
a2.axhline(1, color=MUTED, lw=0.8, ls=":")
a2.annotate(r"$L(\mu^*,x^*)=1$", (1, 1), xytext=(1.35, 3.4), fontsize=9,
            arrowprops=dict(arrowstyle="->", color=INK2, lw=0.8))
a2.set_xlim(-1, 3); a2.set_ylim(0, 6)
a2.set_xlabel(r"$x$"); a2.set_ylabel(r"$L(\mu^*,x)$")
a2.set_title(r"$L(2,x)=(x-1)^2+1\ \geq 1$")
fig.tight_layout(w_pad=2.0)
save(fig, "q2a_saddle_slices.pdf")


# Q3(b): lines L(mu, x) for x = 0, 1, 2 and their lower envelope
m = np.linspace(0, 5, 400)
fig, ax = plt.subplots(figsize=(6.0, 3.7))
lines ={0: m, 1: np.ones_like(m), 2: 4 - m}
for i, (xv, y) in enumerate(lines.items()):
    ax.plot(m, y, color=C[i], lw=1.4, label=rf"$L(\mu,{xv})$")
env = np.minimum.reduce(list(lines.values()))
ax.plot(m, env, color=INK, lw=3.0, alpha=0.85, label="lower envelope", zorder=4)
ax.plot(m, d(m), color=C[6], lw=1.6, ls="--", label=r"true $d(\mu)=\mu-\mu^2/4$", zorder=5)
for mu, xv in [(0, 0), (2, 1), (4, 2)]:
    ax.plot(mu, d(mu), "o", ms=7, color=C[6], mec="white", mew=1.3, zorder=6)
ax.text(0.55, 0.12, r"$\mu$", fontsize=9, color=C[0])
ax.text(4.3, 1.08, r"$1$", fontsize=9, color=C[1])
ax.text(3.55, -0.85, r"$4-\mu$", fontsize=9, color=C[2])
ax.set_xlim(0, 5); ax.set_ylim(-1.5, 2.5)
ax.set_xlabel(r"$\mu$"); ax.set_ylabel("value")
ax.legend(loc="upper center", ncol=3, bbox_to_anchor=(0.5, 1.2), fontsize=8.5)
save(fig, "q3b_envelope.pdf")


# Values used in Q3(a) and Q2(a)
print("d(0..3) =", [d(mu) for mu in range(4)])
print("L(2,1) =", L(2, 1), " L(mu,1) =", [L(mu, 1) for mu in range(5)])
