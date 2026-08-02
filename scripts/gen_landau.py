#!/usr/bin/env python3
"""Wide banner SVG: tilted Landau double well, order parameter driven over the
barrier into the metastable minimum by photoexcitation.

Composition follows the reference screenshot: a single landscape, gradient
stroke running blue -> purple -> red, filled ball in the deeper (left) well,
and a curved arrow arcing over the barrier into the shallower (right) well.
Recoloured for a dark band so the white section title stays legible.
"""
import math

W, H = 2000, 350

# F(eta) = eta^4 - 2 eta^2 + c eta   (c tilts the well, making the left one deeper)
C = 0.35
ETA_LO, ETA_HI = -1.62, 1.60
# The motif is kept compact and centred rather than stretched across the full
# banner: at 2000x350 a full-width landscape flattens into a wave, and a centred
# motif also survives the horizontal crop on narrow screens.
X_LO, X_HI = 650.0, 1350.0
# Y_BOT leaves room for the ball radius so it does not clip the lower edge.
Y_TOP, Y_BOT = 58.0, 300.0

def F(e):
    return e ** 4 - 2 * e * e + C * e

_fs = [F(ETA_LO + i * 0.001) for i in range(int((ETA_HI - ETA_LO) / 0.001) + 1)]
F_MIN, F_MAX = min(_fs), max(_fs)
FSCALE = (Y_BOT - Y_TOP) / (F_MAX - F_MIN)
K = Y_BOT + F_MIN * FSCALE    # y = K - F*FSCALE

def x_of(e):
    return X_LO + (e - ETA_LO) * (X_HI - X_LO) / (ETA_HI - ETA_LO)

def y_of(e):
    return K - F(e) * FSCALE

def minima():
    """Stationary points of 4e^3 - 4e + C."""
    roots, step = [], 0.001
    e = ETA_LO
    prev = 4 * e ** 3 - 4 * e + C
    while e < ETA_HI:
        e += step
        cur = 4 * e ** 3 - 4 * e + C
        if prev == 0 or prev * cur < 0:
            roots.append(e - step / 2)
        prev = cur
    return roots

def curve_path():
    pts, e = [], ETA_LO
    while e <= ETA_HI + 1e-9:
        pts.append(f"{x_of(e):.1f},{y_of(e):.1f}")
        e += 0.005
    return "M " + " L ".join(pts)

stat = minima()
left_min, barrier, right_min = stat[0], stat[1], stat[2]
xl, yl = x_of(left_min), y_of(left_min)
xr, yr = x_of(right_min), y_of(right_min)

svg = []
svg.append(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
    f'preserveAspectRatio="xMidYMid meet" role="img" aria-label="Landau free '
    f'energy double well with the order parameter driven over the barrier by '
    f'photoexcitation">'
)
svg.append('<defs>')
svg.append(
    '<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">'
    '<stop offset="0%" stop-color="#1a3c76"/>'
    '<stop offset="50%" stop-color="#3468b5"/>'
    '<stop offset="100%" stop-color="#1d4585"/></linearGradient>'
)
# blue -> purple -> red along the landscape, as in the reference
svg.append(
    '<linearGradient id="land" x1="0" y1="0" x2="1" y2="0" '
    'gradientUnits="objectBoundingBox">'
    '<stop offset="0%" stop-color="#5566ff"/>'
    '<stop offset="48%" stop-color="#a95fd8"/>'
    '<stop offset="100%" stop-color="#ff4f63"/></linearGradient>'
)
svg.append(
    '<filter id="glow" x="-50%" y="-50%" width="200%" height="200%">'
    '<feGaussianBlur stdDeviation="4" result="b"/>'
    '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>'
    '</filter>'
)
svg.append('</defs>')

svg.append(f'<rect width="{W}" height="{H}" fill="url(#bg)"/>')

# the landscape
svg.append(
    f'<path d="{curve_path()}" fill="none" stroke="url(#land)" stroke-width="14" '
    f'stroke-linecap="round" filter="url(#glow)"/>'
)

# arc over the barrier, from the ball into the shallower well. The second
# control point sits close to the endpoint so the arrow drops steeply into the
# well instead of grazing the curve, as in the reference.
sx, sy = xl + 24, yl - 34
ex, ey = xr - 4, yr - 40
c1 = (xl + 120, 78)
c2 = (xr - 110, 78)
svg.append(
    f'<path d="M {sx:.1f} {sy:.1f} C {c1[0]:.1f} {c1[1]} {c2[0]:.1f} {c2[1]} '
    f'{ex:.1f} {ey:.1f}" fill="none" stroke="#ffffff" stroke-width="9" '
    f'stroke-linecap="round" opacity="0.94"/>'
)
# arrowhead aligned with the outgoing tangent (c2 -> end)
ang = math.degrees(math.atan2(ey - c2[1], ex - c2[0]))
svg.append(
    f'<polygon points="0,0 -46,-27 -46,27" fill="#ffffff" opacity="0.94" '
    f'transform="translate({ex:.1f},{ey:.1f}) rotate({ang:.1f})"/>'
)

# order parameter resting in the deeper minimum
svg.append(f'<circle cx="{xl:.1f}" cy="{yl:.1f}" r="26" fill="#ffffff" filter="url(#glow)"/>')

svg.append('</svg>')

out = "/Users/olivershen/Github/academic_pages/static/media/headers/landau.svg"
with open(out, "w") as f:
    f.write("\n".join(svg) + "\n")
print("wrote", out)
print(f"left min  eta={left_min:+.3f} F={F(left_min):+.3f} at ({xl:.0f},{yl:.0f})")
print(f"barrier   eta={barrier:+.3f} F={F(barrier):+.3f} at ({x_of(barrier):.0f},{y_of(barrier):.0f})")
print(f"right min eta={right_min:+.3f} F={F(right_min):+.3f} at ({xr:.0f},{yr:.0f})")
print(f"arrowhead angle {ang:.1f} deg")
