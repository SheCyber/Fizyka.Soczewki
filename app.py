import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def soczewka(y_in, f):
    y, alpha = y_in
    alpha_out = alpha - y / f if f != 0 else alpha
    return y, alpha_out

def przeslij_promien(x0, y0, alpha0, x1):
    dx = x1 - x0
    return y0 + dx * np.tan(alpha0)

def rysuj_promienie(x, y, d, f1, f2):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axhline(0, color='gray', lw=1, ls='--')
    ax.axvline(0, color='blue', lw=2, label="Soczewka 1")
    ax.axvline(d, color='green', lw=2, label="Soczewka 2")
    ax.axvline(d + y, color='red', lw=2, label="Ekran")
    colors = ['orange', 'magenta', 'purple', 'brown', 'teal', 'olive']
    angles = np.linspace(-0.2, 0.2, 6)
    obrazy = []
    for i, a in enumerate(angles):
        x0, y0, alpha = -x, 0, a
        xs, ys = [x0], [y0]

        x1 = 0
        y1 = przeslij_promien(x0, y0, alpha, x1)
        y1, alpha = soczewka((y1, alpha), f1)
        xs.append(x1); ys.append(y1)

        x2 = d
        y2 = przeslij_promien(x1, y1, alpha, x2)
        y2, alpha = soczewka((y2, alpha), f2)
        xs.append(x2); ys.append(y2)

        x3 = d + y
        y3 = przeslij_promien(x2, y2, alpha, x3)
        xs.append(x3); ys.append(y3)

        ax.plot(xs, ys, color=colors[i])
        obrazy.append(y3)

    ax.plot([x3]*len(obrazy), obrazy, 'rx', label="Obraz(y)")
    ax.legend()
    ax.set_xlim(-x - 10, x3 + 10)
    ax.set_ylim(-2, 2)
    ax.set_xlabel("Oś optyczna (cm)")
    ax.set_ylabel("Odległość od osi (cm)")
    ax.set_title("Symulacja układu dwóch soczewek")
    ax.grid(True)
    return fig

st.title("Symulacja układu dwóch soczewek")

x = st.slider("x (odl. źródła od 1. soczewki)", 10, 200, 70)
y = st.slider("y (odl. ekranu od 2. soczewki)", 10, 150, 60)
d = st.slider("d (odl. soczewek)", 10, 200, 100)
f1 = st.slider("f1 (ogniskowa 1)", -100, 100, 50)
f2 = st.slider("f2 (ogniskowa 2)", -100, 100, 50)

fig = rysuj_promienie(x, y, d, f1, f2)
st.pyplot(fig)
