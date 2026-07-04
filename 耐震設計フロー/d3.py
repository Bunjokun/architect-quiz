# -*- coding: utf-8 -*-
from helpers import SVG, PINK, RED, WHITE

s = SVG()

# chapter header bar
s.rect(34, 22, 200, 20, fill="#c9c9c9", stroke="#c9c9c9")
s.text(40, 37, "第10章  鉄骨構造", 12.5, anchor="start")
# title
s.rect(34, 50, 300, 26, fill="#8f8f8f", stroke="#8f8f8f")
s.text(44, 69, "6  鉄骨造の耐震計算", 16, anchor="start", weight="bold",
       fill="#fff")

# 1. 方針
s.text(34, 100, "1. 耐震計算の方針", 13.5, anchor="start", weight="bold")
s.mtext(34, 138, [
    "  鉄骨造建築物は, 部材の座屈や, 部材間の接合部の破壊が生じない限り, 鋼材の優れた特性により, 靱性に富む構",
    "造物となり得る。そのため, 部材の座屈と接合部の破断の防止により, 鋼素材の本来の特性を生かして十分な耐震性",
    "を発揮できるように設計することが鋼構造設計の最も重要なことである。",
], 11.5, lh=17, anchor="start", x=34)

# 2. フロー
s.text(34, 192, "2. 耐震計算のフロー", 13.5, anchor="start", weight="bold")

# columns centers
C = [112, 256, 400, 544, 688]

# --- top scope boxes ---
s.rect(46, 212, 424, 28)
s.text(258, 231, "高さ≦16m, 階数≦3", 12.5)
s.rect(478, 212, 132, 28)
s.text(544, 231, "高さ≦31m", 12.5)
s.rect(618, 212, 142, 28)
s.text(689, 231, "31m<高さ≦60m", 12)

# --- 一次設計 bar ---
for cx in (258, 544, 689):
    s.arrow(cx, 240, cx, 256)
s.rect(46, 256, 714, 26)
s.text(403, 274, "一 次 設 計", 14, ls="2")

# 耐震二次設計 vertical label (right margin)
s.text(775, 470, "耐震二次設計", 11.5, weight="bold")
s.el[-1] = s.el[-1].replace("<text ",
    '<text transform="rotate(90 775 470)" ')

# --- criteria boxes A,B,C ---
s.rect(C[0]-62, 300, 124, 118)
s.mtext(C[0], 359, ["高さ≦13m", "軒高≦9m", ("階数≦3", "bold", "#000"),
                    "スパン≦6m", "延べ面積≦500㎡"], 11, lh=20)
s.rect(C[1]-64, 300, 128, 118)
s.mtext(C[1], 359, ["高さ≦13m", "軒高≦9m", ("階数≦2", "bold", "#000"),
                    "スパン≦12m", "延べ面積≦500㎡",
                    "(平家の場合", "≦3,000㎡)"], 10.5, lh=15)
s.rect(C[2]-64, 300, 128, 118)
s.mtext(C[2], 359, [("高さ≦16m", "bold", "#000"), ("階数≦3", "bold", "#000"),
                    ("スパン≦6m", "bold", "#000"), "延べ面積≦500㎡"], 11, lh=22)

# arrows from 一次設計 to A/B/C and cols 4,5
for cx in C[:3]:
    s.arrow(cx, 282, cx, 300)
s.arrow(C[3], 282, C[3], 424)
s.arrow(C[4], 282, C[4], 424)

# --- 層間変形角 boxes (col3,4,5) ---
s.rect(C[2]-64, 424, 128, 46)
s.mtext(C[2], 447, ["層間変形角≦1/200", ("(≦1/120緩和はない)", "normal", RED)],
        10.5, lh=17)
s.rect(C[3]-64, 424, 128, 46)
s.text(C[3], 451, "層間変形角≦1/200", 11)
s.rect(C[4]-64, 424, 128, 46)
s.text(C[4], 451, "層間変形角≦1/200", 11)

# arrow A -> confirm (col1, no diamond)
s.arrow(C[0], 418, C[0], 648)
# arrow B -> diamond (col2, no 層間)
s.arrow(C[1], 418, C[1], 520)
# col3 層間 -> diamond
s.arrow(C[2], 470, C[2], 520)
# col4 層間 -> diamond
s.arrow(C[3], 470, C[3], 512)
# col5 層間 -> 保有
s.arrow(C[4], 470, C[4], 500)

# --- diamonds ---
s.diamond(C[1], 552, 58, 32)
s.text(C[1], 556, "偏心率≦0.15", 11)
s.diamond(C[2], 552, 58, 32)
s.text(C[2], 556, "偏心率≦0.15", 11)
s.diamond(C[3], 552, 72, 42)
s.mtext(C[3], 552, [("剛性率≧0.6", "normal", RED),
                    ("偏心率≦0.15", "normal", RED),
                    ("塔状比≦4", "normal", RED)], 10.5, lh=15)

# --- 保有水平耐力 box (col5) ---
s.rect(C[4]-64, 500, 128, 120, fill=PINK)
s.mtext(C[4], 548, [("保有水平耐力の確認", "bold", "#000"), "Qu≧Qud",
                    ("転倒の検討", "normal", "#000"),
                    "(塔状比>4の場合)"], 10.5, lh=17)

# Yes down from diamonds -> confirm
for cx in (C[1], C[2]):
    s.text(cx+12, 636, "Yes", 10.5, anchor="start")
    s.arrow(cx, 584, cx, 648)
s.text(C[3]+16, 636, "Yes", 10.5, anchor="start")
s.arrow(C[3], 594, C[3], 648)
s.arrow(C[4], 620, C[4], 648)

# --- No routing: single low bus into 保有水平耐力 ---
BUS = 614
s.line(C[1]+58, 552, C[1]+58, BUS)   # col2 drop  (x=314)
s.line(C[2]+58, 552, C[2]+58, BUS)   # col3 drop  (x=458)
s.line(C[3]+72, 552, C[3]+72, BUS)   # col4 drop  (x=616)
s.arrow(C[1]+58, BUS, C[4]-64, BUS)  # bus -> 保有 left edge (x=624)
s.text(C[1]+62, 544, "No", 10.5, anchor="start")
s.text(C[2]+62, 544, "No", 10.5, anchor="start")
s.text(C[3]+76, 544, "No", 10.5, anchor="start")

# --- confirm boxes ---
for cx in C:
    s.rect(cx-64, 648, 128, 50)
    s.mtext(cx, 673, ["耐震計算ルート", "に応じた確認"], 11, lh=17)
    s.arrow(cx, 698, cx, 720)

# --- route ovals ---
labels = ["ルート1-1", "ルート1-2", "ルート1-3", "ルート2", "ルート3"]
for cx, lb in zip(C, labels):
    s.oval(cx, 736, 108, 28)
    s.text(cx, 741, lb, 12.5, weight="bold")

s.text(403, 786, "鉄骨造   耐震計算のフロー", 14, weight="bold")

open("d3.svg", "w").write(s.svg())
print("d3 ok")
