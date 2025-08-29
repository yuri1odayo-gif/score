import streamlit as st
import math

st.write("ぷにぷにスコアタ")
st.write("スコア計算ツール")

# ========= 単位変換関数 =========
def format_number_jp(x):
    cho = int(x // 10**12)           # 兆の部分
    oku = round((x % 10**12) / 10**8)  # 億の部分（四捨五入）
    parts = []
    if cho > 0:
        parts.append(f"{cho}兆")
    parts.append(f"{oku}億")
    return "".join(parts)

# ========= 入力 =========
y = st.number_input("yマネー（整数のみ）", min_value=0, value=0, step=1, format="%d")

# セッションに履歴リストを用意
if "score_list" not in st.session_state:
    st.session_state.score_list = []

# ========= 計算 =========
result = ""  # 事前に初期化して安全にする

if y == int(y):
    y = int(y)
    x = 10 ** ((y / 0.0011392) ** (1 / 6.497))
    result = format_number_jp(x)
    st.write("あなたのスコアは " + result)
else:
    st.error("⚠️ y は整数を入力してください")

# ========= 保存ボタン =========
if result != "" and st.button("💾 結果を保存"):
    st.session_state.score_list.append(result)
    st.success("スコアを保存しました ✅")

# ========= 履歴表示（常に表示） =========
if st.session_state.score_list:
    st.write("📜 保存したスコア:")
    for w in st.session_state.score_list:
        st.write(w)

# ========= 説明文 =========
st.write("結果的に色々改良しました")
st.write("実際の値と1~2億誤差があります（自分調べ）")
st.write("注意してください　メンテナンス中")