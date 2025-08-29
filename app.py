import streamlit as st
import math

st.write("ぷにぷにスコアタ")
st.write("スコア計算ツール")

# ========= 単位変換関数 =========
def format_number_jp(x):
    cho = int(x // 10**12)           # 兆の部分
    oku = round((x % 10**12) / 10**8)  # 億の部分
    parts = []
    if cho > 0:
        parts.append(f"{cho}兆")
    parts.append(f"{oku}億")
    return "".join(parts)

# ========= 入力 =========
y = st.number_input("yマネー（整数のみ）", min_value=0, value=0, step=1, format="%d")

# ========= 計算 =========
if y = int(y):
    x = 10 ** ((y / 0.0011392) ** (1 / 6.497))
    result = format_number_jp(x)
    st.write("あなたのスコアは " + result)
else:
    st.error("⚠️ y は整数を入力してください")


# ========= 説明文 =========
st.write("結果的に色々改良しました")
st.write("実際の値と1~2億誤差があります（自分調べ）")
st.write("注意してください")