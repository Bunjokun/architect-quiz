# -*- coding: utf-8 -*-
from helpers import SVG, PINK, RED, WHITE

s = SVG()

# chapter header
s.text(34, 34, "第13章  合成構造・混合構造", 14, anchor="start", weight="bold")

# title bar
s.rect(40, 54, 560, 34, fill="#8f8f8f", stroke="#8f8f8f")
s.text(52, 78, "4  鉄骨鉄筋コンクリート構造の耐震計算", 17, anchor="start",
       weight="bold", fill="#fff")
s.text(760, 78, "出題:H18", 11.5, anchor="end")

# route column centers
R1, R21, R22, R3 = 150, 360, 520, 690

# --- top scope boxes ---
s.rect(70, 118, 170, 34)
s.text(155, 140, "h≦20m", 13)
s.rect(300, 118, 200, 34)
s.text(400, 140, "20m<h≦31m", 13)
s.rect(560, 118, 200, 34, fill=PINK)
s.text(660, 140, "31m<h≦60m", 13)

# arrows to 一次設計
for cx in (155, 400, 660):
    s.arrow(cx, 152, cx, 176)

# --- 一次設計 bar ---
s.rect(70, 176, 690, 34)
s.text(415, 199, "一 次 設 計", 15, ls="2")

# --- 層間変形角 ---
s.arrow(415, 210, 415, 250)
s.rect(230, 250, 400, 34)
s.text(430, 272, "層間変形角の確認     層間変形角≦1/200", 12.5, weight="bold")

# --- 剛性率/偏心率/塔状比 box ---
s.arrow(415, 284, 415, 322)
s.rect(230, 322, 400, 92)
s.mtext(430, 368, [
    "剛性率の確認     剛性率≧6/10",
    "偏心率の確認     偏心率≦15/100",
    "建築物の塔状比 ≦ 4",
], 12.5, lh=27, anchor="middle")

# --- 構造規定の選択 ---
s.text(415, 442, "Yes", 11)
s.arrow(415, 414, 415, 470)
s.rect(300, 470, 260, 34)
s.text(430, 492, "構造規定の選択", 13, weight="bold")

# --- left rail to Σ box (h<=20m -> ルート1) ---
s.arrow(R1, 210, R1, 440)
s.rect(R1-72, 440, 144, 130)
s.mtext(R1, 500, ["Σ2.5α Aw", "+Σ1.0α Ac", "≧ZWA i", "",
                  "部材のせん", "断設計"], 12, lh=19)

# --- 強度型(1)/(2) : split from 構造規定 bottom ---
s.line(430, 504, 430, 522)
s.poly([(430, 522), (R21, 522), (R21, 560)], arrow=True)
s.poly([(430, 522), (R22, 522), (R22, 560)], arrow=True)
s.rect(R21-70, 560, 140, 32)
s.text(R21, 581, "強度型(1)", 13)
s.rect(R22-70, 560, 140, 32)
s.text(R22, 581, "強度型(2)", 13)

# --- 保有水平耐力 box (right) ---
# box3 rail + No from 剛性率 box both feed 保有
s.arrow(R3, 210, R3, 440)          # box3 rail into 保有 top
s.line(630, 368, R3, 368)          # No merge into rail
s.text(648, 358, "No", 11)
s.rect(R3-78, 440, 156, 150, fill=PINK)
s.mtext(R3, 500, [("保有水平耐力の", "bold", "#000"),
                  ("確認", "bold", "#000"),
                  "Qu≧Qun", "Qun = Ds Fes Qud",
                  ("転倒の検討", "bold", "#000"),
                  "(塔状比>4", "の場合)"], 11, lh=18)

# --- route ovals ---
s.arrow(R1, 570, R1, 636)
s.arrow(R21, 592, R21, 636)
s.arrow(R22, 592, R22, 636)
s.arrow(R3, 590, R3, 636)
for cx, lb in ((R1, "ルート 1"), (R21, "ルート 2-1"),
               (R22, "ルート 2-2"), (R3, "ルート 3")):
    s.oval(cx, 652, 116, 28)
    s.text(cx, 657, lb, 13, weight="bold")

# --- エンド bar ---
for cx in (R1, R21, R22, R3):
    s.arrow(cx, 666, cx, 704)
s.rect(70, 704, 690, 28)
s.text(415, 723, "エ ン ド", 14, ls="2")

# caption
s.text(415, 770, "鉄骨鉄筋コンクリート造建築物の耐震計算フロー", 14,
       weight="bold")
s.text(415, 792, "h:建築物の高さ", 12)

open("d4.svg", "w").write(s.svg())
print("d4 ok")
