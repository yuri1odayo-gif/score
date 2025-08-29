import streamlit as st
import math

st.write("ぷにぷにスコアタ")
st.write("スコア計算ツール")

# ========= 単位変換関数 =========
def format_number_jp(x):
    # 兆の部分
    cho = int(x // 10**12)
    # 億の部分（兆を引いた残りから計算）
    oku = int((x % 10**12) // 10**8)

    if cho > 0:
        if oku > 0:
            return f"{cho}兆{oku}億"
        else:
            return f"{cho}兆"
    elif oku > 0:
        return f"{oku}億"
    else:
        return f"{x:,.0f}"

# ========= 入力 =========
y = st.number_input("yマネー（整数のみ）", min_value=0, value=13000, step=1, format="%d")

# 整数チェック（念のため）
if y != int(y):
    st.error("⚠️ y は整数を入力してください")
else:
    y = int(y)

    # ========= 計算 =========
    x = 10 ** ((y / 0.0011392) ** (1 / 6.497))

    # ========= 結果表示 =========
    st.write(f"約 {format_number_jp(x)} ", fontsize=20)