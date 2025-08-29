import streamlit as st
import math

st.write("ぷにぷにスコアタ")
st.write("スコア計算ツール")

# ========= 単位変換関数 =========
def format_number_jp(x):
    # 兆の部分
    cho = int(x // 10**12)
    # 億の部分（四捨五入）
    oku = round((x % 10**12) / 10**8)

    parts = []
    if cho > 0:
        parts.append(f"{cho}兆")
    parts.append(f"{oku}億")
    return "".join(parts)

# ========= 入力 =========
y = st.number_input("yマネー（整数のみ）", min_value=0, value=0, step=1, format="%d")


# 整数チェック（念のため）
if y != int(y):
    st.error("⚠️ y は整数を入力してください")
else:
    y = int(y)

# セッションに履歴を用意
if "history" not in st.session_state:
    st.session_state.history = []

    # ========= 計算 =========
    x = 10 ** ((y / 0.0011392) ** (1 / 6.497))

    # ========= 結果表示 =========
    result = format_number_jp(x)
    st.write("あなたのスコアは " + result)

    # ========= 保存ボタン =========
    if st.button("保存"):
        st.session_state.history.append(result)
        st.success("結果を保存しました ✅")

    # ========= 履歴表示 =========
    if st.session_state.history:
        st.write("📜 保存した履歴:")
        for r in st.session_state.history:
            st.write(r)

    # ========= 説明文 =========
    st.write("結果的に色々改良しました")
    st.write("実際の値と1~2億誤差があります（自分調べ）")
    st.write("注意してください")