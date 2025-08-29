import streamlit as st
import math

st.write("ぷにぷにスコアタ")
st.write("スコア計算ツール")

# ========= 単位変換関数 =========
def format_number(n):
    if n >= 10**12:
        return f"{n/10**12:.3f}兆"
    elif n >= 10**8:
        return f"{n/10**8:.3f}億"
    else:
        return f"{n:,.0f}"  # それ以下はカンマ区切りの整数

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