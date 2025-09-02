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

    # ========= 計算 =========
    x = 10 ** ((y / 0.0011392) ** (1 / 6.497))

    # ========= 結果表示 =========
    result = format_number_jp(x)
    st.write("あなたのスコアは")
    
    show_result = st.checkbox("結果を表示する", value =False)

    if show_result:
        nakami = f"{result}"
    else :
        nakami = "非表示"
        
    #========= 四角の枠　=========
    st.markdown(
    f"""
    <div style='border: 2px solid black; padding: 10px; border-radius:5px;'>
        {nakami}
    </div>
    """,
    unsafe_allow_html=True
)
    # ========= 説明文 =========
    st.write("結果的に色々改良しました")
    st.write("実際の値と1~2億誤差があります（自分調べ）")
    st.write("注意してください")