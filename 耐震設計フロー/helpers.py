# -*- coding: utf-8 -*-
"""SVG drawing helpers for A4-portrait seismic-calc flowcharts."""

W, H = 794, 1123  # A4 portrait px
FONT = "Noto Sans CJK JP, sans-serif"
PINK = "#f7dede"
RED = "#e8534e"
WHITE = "#ffffff"


class SVG:
    def __init__(self, w=W, h=H):
        self.w, self.h = w, h
        self.el = []

    def rect(self, x, y, w, h, fill=WHITE, stroke="#000", sw=1.3, dash=None, rx=0):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        rr = f' rx="{rx}"' if rx else ""
        self.el.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}{rr}/>'
        )

    def oval(self, cx, cy, w, h, fill=PINK, stroke="#000", sw=1.3):
        self.el.append(
            f'<rect x="{cx-w/2}" y="{cy-h/2}" width="{w}" height="{h}" rx="{h/2}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def diamond(self, cx, cy, hw, hh, fill=WHITE, stroke="#000", sw=1.3):
        pts = f"{cx},{cy-hh} {cx+hw},{cy} {cx},{cy+hh} {cx-hw},{cy}"
        self.el.append(
            f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
        )

    def line(self, x1, y1, x2, y2, sw=1.3, dash=None, stroke="#000"):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.el.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}/>'
        )

    def arrow(self, x1, y1, x2, y2, sw=1.3, stroke="#000"):
        self.el.append(
            f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" marker-end="url(#ar)"/>'
        )

    def poly(self, pts, sw=1.3, stroke="#000", arrow=False):
        p = " ".join(f"{x},{y}" for x, y in pts)
        m = ' marker-end="url(#ar)"' if arrow else ""
        self.el.append(
            f'<polyline points="{p}" fill="none" stroke="{stroke}" '
            f'stroke-width="{sw}"{m}/>'
        )

    def text(self, x, y, s, size=13, anchor="middle", weight="normal",
             fill="#000", ls=None):
        lsp = f' letter-spacing="{ls}"' if ls else ""
        self.el.append(
            f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'text-anchor="{anchor}" font-weight="{weight}" fill="{fill}"{lsp}>'
            f'{esc(s)}</text>'
        )

    def mtext(self, cx, cy, lines, size=13, anchor="middle", weight="normal",
              fill="#000", lh=None, x=None):
        """Multi-line text vertically centered on cy. lines: list of str or
        (str, weight, fill) tuples."""
        if lh is None:
            lh = size + 4
        n = len(lines)
        y0 = cy - (n - 1) * lh / 2 + size / 3
        xx = cx if x is None else x
        for i, ln in enumerate(lines):
            if isinstance(ln, tuple):
                s, w, f = (ln + ("normal", fill))[:3] if len(ln) < 3 else ln
                self.text(xx, y0 + i * lh, s, size, anchor, w, f)
            else:
                self.text(xx, y0 + i * lh, ln, size, anchor, weight, fill)

    def svg(self):
        body = "\n".join(self.el)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" '
            f'height="{self.h}" viewBox="0 0 {self.w} {self.h}">\n'
            f'<defs><marker id="ar" markerWidth="9" markerHeight="9" refX="7" '
            f'refY="3" orient="auto" markerUnits="strokeWidth">'
            f'<path d="M0,0 L7,3 L0,6 z" fill="#000"/></marker></defs>\n'
            f'<rect width="{self.w}" height="{self.h}" fill="#fff"/>\n'
            f'{body}\n</svg>'
        )


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
