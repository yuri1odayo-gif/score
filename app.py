import streamlit as st
import math

st.write("ぷにぷにスコアタ")
st.write("スコア計算ツール")

# ========= 単位変換関数 =========
def format_number_jp(x):
    # 兆の部分
    cho = (x // 10**12)
    # 億の部分
    oku = (x % 10**12) // 10**8
    # 万の部分
    man = (x % 10**8) // 10**4
    # 1の部分
    ichi = int(x % 10**4)

    parts = []
    if cho > 0:
        parts.append(f"{cho}兆")
    if oku > 0:
        parts.append(f"{oku}億")
    if man > 0:
        parts.append(f"{man}万")
    parts.append(f"{ichi}")
    return "".join(parts)

# ========= 入力 =========
y = st.number_input("yマネー（整数のみ）", min_value=0, value=0, step=1, format="%d")

# 整数チェック（念のため）
if y != int(y):
    st.error("⚠️ y は整数を入力してください")
else:
    y = int(y)

    # ========= 計算 =========
    x = 10 ** ((y / 0.0011392) ** (1 / 6.497))

    # ========= 結果表示 =========
    result = format_number_jp(int(x))
    st.write(result)