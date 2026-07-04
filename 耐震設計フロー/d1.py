# -*- coding: utf-8 -*-
from helpers import SVG, PINK, RED, WHITE

s = SVG()
CX = 400

# --- header / title ---
s.text(34, 34, "第7章  一次設計", 15, anchor="start", weight="bold")
s.text(34, 60, "耐震計算のフロー(超高層建築物等の構造計算, 限界耐力計算を除く)",
       14, anchor="start", weight="bold")

# --- right rail (一次設計 bracket) ---
s.line(760, 110, 760, 300)
s.arrow(760, 217, 470, 217)                 # into 応力度計算 box
s.rect(690, 150, 78, 26, fill=PINK)
s.text(729, 167, "一次設計", 12)

# --- スタート ---
s.rect(CX-58, 78, 116, 26)
s.text(CX, 95, "スタート", 13)
s.arrow(CX, 104, CX, 116)

# --- 応力計算 (+ 荷重・外力 label) ---
s.rect(CX-58, 116, 116, 26)
s.text(CX, 133, "応力計算", 13)
s.rect(120, 116, 110, 26)
s.text(175, 133, "荷重・外力", 12)
s.line(230, 129, CX-58, 129)
s.arrow(CX, 142, CX, 152)

# --- 荷重外力の組合せ ---
s.rect(CX-108, 152, 216, 42)
s.mtext(CX, 173, ["荷重・外力の組合せに", "よる長期と短期の応力"], 12, lh=17)
s.arrow(CX, 194, CX, 204)

# --- 応力度計算 (+ 許容応力度 label) ---
s.rect(CX-70, 204, 140, 26)
s.text(CX, 221, "応力度計算", 13)
s.rect(88, 204, 180, 26)
s.text(178, 221, "許容応力度≧生じる応力度", 11.5)
s.line(268, 217, CX-70, 217)
s.arrow(CX, 230, CX, 244)

# --- dashed box ---
s.rect(CX-128, 244, 256, 50, dash="4 3")
s.mtext(CX, 269, ["・使用上の支障防止の確認", "・屋根ふき材等の構造計算"], 12, lh=18,
        anchor="start", x=CX-116)
s.arrow(CX, 294, CX, 316)

# --- 規模等 diamond ---
s.diamond(CX, 372, 96, 52)
s.mtext(CX, 372, ["規模等による", "耐震計算ルートの", "選択"], 12, lh=17)

# 耐震二次設計 label (red) on right
s.rect(678, 452, 104, 26, fill=RED)
s.text(730, 469, "耐震二次設計", 12.5, fill="#fff", weight="bold")

# left branch 不要 -> 判断
s.text(300, 362, "不要", 12)
s.arrow(CX-96, 372, 236, 372)
s.diamond(180, 372, 58, 34)
s.text(180, 376, "判断※", 12)
s.text(180, 424, "(より詳細な検討)", 11)
# down from 判断 to route1 box
s.arrow(180, 406, 180, 726)

# down 必要
s.text(CX+16, 440, "必要", 12)
s.arrow(CX, 424, CX, 452)

# --- 層間変形角 (pink) ---
s.rect(CX-130, 452, 260, 46, fill=PINK)
s.mtext(CX, 475, [("層間変形角の確認", "bold", "#000"),
                  "層間変形角≦1/200(1/120)"], 12.5, lh=19)
s.arrow(CX, 498, CX, 534)

# --- 高さ<=31m diamond ---
s.diamond(CX, 574, 74, 40)
s.text(CX, 578, "高さ≦31m", 12.5)
s.text(540, 560, "No", 12)
# No -> right rail down to route3
s.line(CX+74, 574, 600, 574)
s.text(CX+16, 618, "Yes", 12)
s.arrow(CX, 614, CX, 640)

# --- 判断 diamond ---
s.diamond(CX, 676, 62, 36)
s.text(CX, 680, "判断※", 12)
s.text(610, 680, "(より詳細な検討)", 11, anchor="start")
s.line(CX+62, 676, 600, 676)

# merge vertical to route3 (材料強度/保有水平耐力)
s.arrow(600, 574, 600, 786)
s.arrow(CX, 712, CX, 740)

# ================= bottom three boxes =================
# route1 box (left)
s.rect(66, 726, 228, 214)
s.mtext(80, 826, [
    "○木造", "   階数≦3", "   高さ≦16m",
    "○鉄骨造", "   階数≦3", "   高さ≦16m",
    "   地震力の割増し(C₀≧0.3)",
    "   及び筋かい端部・接合部の破",
    "   断防止等",
    "○鉄筋コンクリート造及び鉄骨鉄",
    "   筋コンクリート造", "   高さ≦20m",
    "   壁量・柱量の確保",
    "   部材のせん断破壊防止  等",
], 11, lh=13.7, anchor="start", x=76)

# route2 box (middle)
s.rect(300, 706, 244, 254)
s.mtext(422, 730, [("剛性率・偏心率等の確認", "bold", "#000"),
                   "剛性率≧0.6(6/10)", "偏心率≦0.15(15/100)"], 11.5, lh=17)
s.mtext(312, 838, [
    "○木造",
    "  筋かいを含む階の応力の割増し。",
    "  筋かいの破断の防止。柱,梁,接",
    "  合部の急激な耐力低下の防止",
    "○鉄骨造",
    "  筋かい架構の応力の割増し,筋かい",
    "  端部・接合部の破断防止,局部座屈",
    "  等の防止及び柱脚部の破壊防止等",
    "○鉄筋コンクリート造及び鉄骨鉄筋",
    "  コンクリート造",
    "  壁量・柱量の確保",
    "  部材のせん断破壊防止   等",
], 10.5, lh=13.2, anchor="start", x=308)
s.text(422, 953, "建築物の塔状比≦4", 11.5, weight="bold")

# route3 box (right)
s.rect(566, 786, 202, 40, fill=PINK)
s.mtext(667, 806, [("材料強度", "normal", "#000"),
                   "構造特性係数 Ds  形状係数 Fes"], 10.5, lh=15)
s.line(566, 806, 768, 806, dash="3 3")
s.arrow(667, 826, 667, 840)
s.rect(566, 840, 202, 96, fill=PINK)
s.mtext(667, 888, [("保有水平耐力の確認", "bold", "#000"),
                   "Qu≧Qun",
                   "Qun = Ds Fes Qud",
                   ("転倒の検討", "normal", "#000"),
                   "(塔状比>4の場合)"], 11, lh=17)

# NG arrow route2 -> route3
s.text(556, 878, "NG", 11)
s.arrow(544, 888, 566, 888)

# ================= route ovals =================
s.arrow(180, 940, 180, 978)
s.oval(180, 994, 92, 26)
s.text(180, 999, "ルート 1", 13, weight="bold")
s.arrow(422, 960, 422, 978)
s.text(410, 973, "OK", 11)
s.oval(422, 994, 92, 26)
s.text(422, 999, "ルート 2", 13, weight="bold")
s.arrow(667, 936, 667, 978)
s.oval(667, 994, 92, 26)
s.text(667, 999, "ルート 3", 13, weight="bold")

# エンド bar
s.arrow(180, 1007, 180, 1024)
s.arrow(422, 1007, 422, 1024)
s.arrow(667, 1007, 667, 1024)
s.rect(66, 1024, 702, 26)
s.text(400, 1041, "エ  ン  ド", 14, ls="2")

# footnote
s.mtext(34, 1082, [
    "※判断とは設計者の設計方針に基づく判断のことである。例えば, 規模としては, ルート2を適用可能な高さ31m以",
    "  下の建築物であっても, より詳細な検討を行う設計法であるルート3を適用する判断等のことを示している。",
], 10.5, lh=15, anchor="start", x=34)

open("d1.svg", "w").write(s.svg())
print("d1 ok")
