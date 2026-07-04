# -*- coding: utf-8 -*-
from helpers import SVG, PINK, RED, WHITE

s = SVG()
GREY = "#e9e9e9"

s.text(34, 34, "第8章  構造計算・構造計画", 15, anchor="start", weight="bold")

# column x-bands
c1 = (40, 250)
c2 = (262, 536)
c3 = (548, 760)

# --- column header titles ---
s.rect(c1[0], 70, c1[1]-c1[0], 54)
s.mtext((c1[0]+c1[1])/2, 97, ["令82条各号及び", "令82条の4の計算"], 13, lh=20)
s.rect(c2[0], 70, c2[1]-c2[0], 54)
s.mtext((c2[0]+c2[1])/2, 97, [("許容応力度等計算", "bold", "#000"),
                              "(一次設計+ルート2)"], 13, lh=20)
s.rect(c3[0], 70, c3[1]-c3[0], 54)
s.mtext((c3[0]+c3[1])/2, 97, [("保有水平耐力計算", "bold", "#000"),
                              "(一次設計+ルート3)"], 13, lh=20)

# --- grey route background bands ---
for (a, b) in (c1, c2, c3):
    s.rect(a, 366, b-a, 486, fill=GREY, stroke="#bbbbbb", sw=1)

# --- 一次設計 pink box (center) ---
bx = (300, 560)
s.rect(bx[0], 150, bx[1]-bx[0], 96, fill=PINK)
s.rect(360, 160, 140, 28, fill=WHITE)
s.text(430, 179, "一次設計", 15, weight="bold")
s.mtext(430, 218, [("許容応力度≧生じる応力度", "bold", "#000"),
                   "使用上の支障防止の確認",
                   "屋根ふき材等の構造計算"], 12.5, lh=18)

# --- 耐震二次設計 red dashed boundary ---
s.line(40, 270, 760, 270, dash="7 4", stroke=RED, sw=1.4)
s.text(30, 320, "耐震二次設計", 12, anchor="middle", weight="bold",
       fill=RED)
# rotate label vertically
s.el[-1] = s.el[-1].replace("<text ",
    '<text transform="rotate(-90 30 320)" ')
s.line(48, 288, 48, 366, stroke=RED, sw=1.3)
s.el.append('<line x1="48" y1="360" x2="48" y2="366" stroke="%s" '
            'stroke-width="1.3" marker-end="url(#arR)"/>' % RED)

# --- 規模 diamond + 判断 ---
s.arrow(430, 246, 430, 288)
s.diamond(430, 322, 84, 38)
s.mtext(430, 322, ["規模等による", "耐震計算ルートの", "選択"], 11.5, lh=15)
s.diamond(168, 322, 52, 30)
s.text(168, 326, "判断※", 11.5)
s.line(346, 322, 220, 322)
# 判断 down through col1
s.arrow(168, 352, 168, 762)
# 規模 down to route2/3 (層間変形角 spans both columns)
s.arrow(430, 360, 430, 396)

# route tab labels
s.text(c1[0]+8, 384, "ルート1", 12.5, anchor="start", weight="bold")
s.text(c2[0]+8, 384, "ルート2", 12.5, anchor="start", weight="bold")
s.text(c3[0]+8, 384, "ルート3", 12.5, anchor="start", weight="bold")

# --- 層間変形角 pink (spans route2+3) ---
s.rect(300, 398, 460, 30, fill=PINK)
s.text(530, 418, "層間変形角 ≦ 1/200 ( 1/120)", 13, weight="bold")

# --- 高さ<=31m diamond ---
s.arrow(454, 428, 454, 456)
s.diamond(454, 490, 66, 32)
s.text(454, 494, "高さ≦31m", 12)
s.text(398, 462, "YES", 11)
s.text(516, 462, "NO", 11)
# YES down to 判断
s.arrow(454, 522, 454, 548)
# NO right -> route3
s.poly([(520, 490), (670, 490), (670, 560)], arrow=True)

# --- 判断 diamond (route2) ---
s.diamond(454, 580, 52, 30)
s.text(454, 584, "判断※", 11.5)
s.arrow(454, 610, 454, 636)

# --- 剛性率 box (route2) ---
s.rect(345, 636, 220, 96)
s.mtext(455, 684, [("剛性率≧0.6", "bold", RED),
                   ("偏心率≦0.15", "bold", RED),
                   ("塔状比≦4", "bold", RED)], 13, lh=26)
# fix red numbers only look: keep simple bold black+red mixed -> use black
s.text(455, 740, "OK", 11)
s.arrow(455, 732, 455, 762)

# --- 保有水平耐力 box (route3) ---
s.rect(580, 560, 180, 130, fill=PINK)
s.mtext(670, 612, [("保有水平耐力の確認", "bold", "#000"),
                   "Qu≧Qun"], 13, lh=22)
s.mtext(670, 662, [("転倒の検討", "bold", "#000"),
                   "(塔状比>4 の場合)"], 11.5, lh=18)
# NG arrow route2 -> route3
s.text(572, 643, "NG", 11)
s.arrow(565, 655, 580, 655)
s.arrow(670, 690, 670, 762)

# --- 構造種別に応じた確認 boxes ---
def confirm(cx, y):
    s.rect(cx-80, y, 160, 52)
    s.mtext(cx, y+26, ["構造種別に", "応じた確認"], 12, lh=18)

confirm(168, 762)
confirm(455, 762)
confirm(670, 762)
for cx in (168, 455, 670):
    s.arrow(cx, 814, cx, 838)
    s.text(cx, 852, "END", 12, weight="bold")

# caption + footnote
s.text(430, 878, "耐震計算のフロー", 14, weight="bold")
s.text(34, 900, "※「判断」とは, 設計者の設計方針に基づく判断のことである。",
       12, anchor="start")
s.text(748, 1090, "出題:R07・17", 11.5, anchor="end")
s.text(400, 1108, "- 170 -", 12)

# red arrowhead marker
svg = s.svg().replace("</defs>",
    '<marker id="arR" markerWidth="9" markerHeight="9" refX="7" refY="3" '
    'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L7,3 L0,6 z" '
    'fill="%s"/></marker></defs>' % RED)
open("d2.svg", "w").write(svg)
print("d2 ok")
